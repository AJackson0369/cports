pkgname = "firefox-esr"
pkgver = "102.5.0"
pkgrel = 0
make_cmd = "gmake"
hostmakedepends = [
    "pkgconf", "zip", "nasm", "yasm", "cargo", "rust", "python", "cbindgen",
    "llvm-devel", "clang-devel", "nodejs", "gettext-tiny", "automake",
    "libtool", "gmake",
]
makedepends = [
    "rust-std", "nss-devel", "nspr-devel", "gtk+3-devel", "icu-devel",
    "dbus-devel", "glib-devel", "libpulse-devel", "pixman-devel",
    "freetype-devel", "libjpeg-turbo-devel", "libpng-devel", "libwebp-devel",
    "libevent-devel", "libnotify-devel", "libvpx-devel", "libvorbis-devel",
    "libogg-devel", "libtheora-devel", "libxt-devel", "libxcomposite-devel",
    "libxscrnsaver-devel", "pipewire-jack-devel", "ffmpeg-devel",
    "alsa-lib-devel", "mesa-devel", "libffi-devel", "zlib-devel",
    # XXX: https://bugzilla.mozilla.org/show_bug.cgi?id=1532281
    "dbus-glib-devel",
]
depends = ["hicolor-icon-theme"]
pkgdesc = "Mozilla Firefox web browser (ESR)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND MPL-2.0"
url = "https://www.mozilla.org/firefox"
# TODO: ppc64le JIT
source = f"$(MOZILLA_SITE)/firefox/releases/{pkgver}esr/source/firefox-{pkgver}esr.source.tar.xz"
sha256 = "017dd44b1285913f477074802707a4c76ed1a28270ec5a327bbb76574cc057d8"
debug_level = 1 # defatten, especially with LTO
tool_flags = {
    "LDFLAGS": ["-Wl,-rpath=/usr/lib/firefox", "-Wl,-z,stack-size=2097152"]
}
env = {
    "MAKE": "/usr/bin/gmake",
    "SHELL": "/usr/bin/sh",
    "BUILD_OFFICIAL": "1",
    "MOZILLA_OFFICIAL": "1",
    "USE_SHORT_LIBNAME": "1",
    "MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE": "system",
    "MOZ_APP_REMOTINGNAME": "Firefox",
    "MOZBUILD_STATE_PATH": f"/builddir/{pkgname}-{pkgver}/.mozbuild",
    # firefox checks for it by calling --help
    "CBUILD_BYPASS_STRIP_WRAPPER": "1",
}
# needs to be investigated
options = ["!lto", "!cross"]
exec_wrappers = [
    ("/usr/bin/llvm-objdump", "objdump"),
    ("/usr/bin/llvm-readelf", "readelf"),
]

if self.profile().endian == "big":
    broken = "broken colors, needs patching, etc."

def post_extract(self):
    self.cp(
        self.files_path / "stab.h", "toolkit/crashreporter/google-breakpad/src"
    )

def post_patch(self):
    from cbuild.util import cargo

    for crate in [
        "target-lexicon", "target-lexicon-0.9.0", "packed_simd_2",
        "authenticator", "bindgen", "nix",
    ]:
        cargo.clear_vendor_checksums(
            self, crate, vendor_dir = "third_party/rust"
        )

def init_configure(self):
    from cbuild.util import cargo

    env["AS"] = self.get_tool("CC")
    env["MOZ_MAKE_FLAGS"] = f"-j{self.make_jobs}"
    env["RUST_TARGET"] = self.profile().triplet
    # use all the cargo env vars we enforce
    env.update(cargo.get_environment(self))

def do_configure(self):
    self.rm("objdir", recursive = True, force = True)
    self.mkdir("objdir")

    extra_opts = []

    match self.profile().arch:
        case "x86_64" | "aarch64":
            extra_opts += ["--disable-elf-hack", "--enable-rust-simd"]

    self.do(
        self.chroot_cwd / "mach", "configure",
        "--prefix=/usr",
        "--libdir=/usr/lib",
        "--host=" + self.profile().triplet,
        "--target=" + self.profile().triplet,
        "--enable-linker=lld",
        "--enable-release",
        "--enable-optimize=" + self.get_cflags(shell = True),
        "--disable-install-strip",
        "--disable-strip",
        # system libs
        "--with-system-pixman",
        "--with-system-ffi",
        "--with-system-nspr",
        "--with-system-nss",
        "--with-system-jpeg",
        "--with-system-zlib",
        "--with-system-libevent",
        "--with-system-libvpx",
        "--with-system-icu",
        # no apng support
        "--without-system-png",
        # wasi currently not ready
        "--without-wasm-sandboxed-libraries",
        # features
        "--enable-dbus",
        "--enable-jack",
        "--enable-ffmpeg",
        "--enable-pulseaudio",
        "--enable-necko-wifi",
        "--enable-default-toolkit=cairo-gtk3-wayland",
        "--enable-audio-backends=pulseaudio",
        # disabled features
        "--disable-crashreporter",
        "--disable-profiling",
        "--disable-jemalloc",
        "--disable-tests",
        "--disable-updater",
        "--disable-alsa",
        # browser options
        "--enable-official-branding",
        "--enable-application=browser",
        "--allow-addon-sideload",
        # conditional opts
        *extra_opts, wrksrc = "objdir"
    )

def do_build(self):
    self.do(self.chroot_cwd / "mach", "build", wrksrc = "objdir")

def do_install(self):
    self.do(self.chroot_cwd / "mach", "install", wrksrc = "objdir", env = {
        "DESTDIR": str(self.chroot_destdir)
    })

    self.install_file(
        self.files_path / "vendor.js",
        "usr/lib/firefox/browser/defaults/preferences"
    )
    self.install_file(
        "taskcluster/docker/firefox-snap/firefox.desktop",
        "usr/share/applications"
    )

    # icons
    for sz in [16, 22, 24, 32, 48, 128, 256]:
        self.install_file(
            f"browser/branding/official/default{sz}.png",
            f"usr/share/icons/hicolor/{sz}x{sz}/apps", name = "firefox.png"
        )

    # https://bugzilla.mozilla.org/show_bug.cgi?id=658850
    self.rm(self.destdir / "usr/lib/firefox/firefox-bin")
    self.install_link("firefox", "usr/lib/firefox/firefox-bin")

def do_check(self):
    # XXX: maybe someday
    pass
