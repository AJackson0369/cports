pkgname = "mozjs91"
pkgver = "91.13.0"
pkgrel = 0
build_wrksrc = "js/src"
build_style = "gnu_configure"
configure_args = [
    "--disable-jemalloc", "--disable-strip", "--disable-tests",
    "--disable-optimize", "--disable-debug", "--enable-ctypes",
    "--enable-readline", "--enable-shared-js", "--enable-system-ffi",
    "--with-intl-api", "--with-system-icu", "--with-system-nspr",
    "--with-system-zlib", "--enable-hardening", "--enable-release",
]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "gmake", "pkgconf", "python", "python-setuptools", "python-six",
    "perl", "gm4", "gawk", "rust", "cargo",
]
makedepends = [
    "icu-devel", "libffi-devel", "nspr-devel", "python-devel",
    "zlib-devel", "libedit-devel", "rust-std", "linux-headers",
]
pkgdesc = "Mozilla JavaScript interpreter and library (91.x)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://www.mozilla.org/firefox"
# can't include ppc jit yet, interactive interpreter segfaults
# (i guess because of lack of ion?)
source = f"$(MOZILLA_SITE)/firefox/releases/{pkgver}esr/source/firefox-{pkgver}esr.source.tar.xz"
sha256 = "53be2bcde0b5ee3ec106bd8ba06b8ae95e7d489c484e881dfbe5360e4c920762"
debug_level = 1 # make the debug size not explode
tool_flags = {
    "LDFLAGS": ["-Wl,-z,stack-size=1048576"]
}
env = {
    "RUST_TARGET": self.profile().triplet,
    "PYTHON": "/usr/bin/python",
    "SHELL": "/usr/bin/sh",
    "MAKE": "gmake",
    "AWK": "gawk",
    "M4": "gm4",
}
# dependencies are not crossable for now and it's probably tricky
options = ["!cross"]
exec_wrappers = [
    ("/usr/bin/llvm-objdump", "objdump"),
    ("/usr/bin/llvm-readelf", "readelf"),
]

def init_configure(self):
    self.env["AC_MACRODIR"] = str(
        self.chroot_builddir / f"{pkgname}-{pkgver}/build/autoconf"
    )

def pre_configure(self):
    with open(self.cwd / "configure", "w") as cfg:
        (self.cwd / "../../build/autoconf/autoconf.sh").chmod(0o755)
        self.do(
            "/usr/bin/sh",
            self.chroot_cwd / "../../build/autoconf/autoconf.sh",
            "--localdir={self.chroot_cwd}", "configure.in",
            stdout = cfg
        )
    (self.cwd / "configure").chmod(0o755)

def post_install(self):
    self.rm(self.destdir / "usr/lib/libjs_static.ajs")
    # it has correct soname but not the right file name
    self.mv(
        self.destdir / "usr/lib/libmozjs-91.so",
        self.destdir / "usr/lib/libmozjs-91.so.0"
    )
    self.install_link("libmozjs-91.so.0", "usr/lib/libmozjs-91.so")

def do_check(self):
    self.do(
        "python", "jit-test/jit_test.py", "-s", "-t", "2400", "--no-progress",
        "../../js/src/dist/bin/js", "basic"
    )

@subpackage("mozjs91-devel")
def _devel(self):
    # include the interactive interpreter
    return self.default_devel(extra = ["usr/bin"])
