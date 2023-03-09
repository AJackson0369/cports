pkgname = "boost"
pkgver = "1.81.0"
pkgrel = 0
hostmakedepends = ["pkgconf"]
makedepends = [
    "zlib-devel", "libbz2-devel", "liblzma-devel", "libzstd-devel",
    "icu-devel", "python-devel", "linux-headers"
]
provides = [f"boost{pkgver[:-2]}={pkgver}-r{pkgrel}"]
pkgdesc = "Free peer-reviewed portable C++ source libraries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSL-1.0"
url = "https://boost.org"
source = f"https://boostorg.jfrog.io/artifactory/main/release/{pkgver}/source/boost_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "205666dea9f6a7cfed87c7a6dfbeb52a2c1b9de55712c9c1a87735d7181452b6"
tool_flags = {"CXXFLAGS": ["-std=c++14"]}
# FIXME: odd failures, but seems test-related
options = ["!check", "!cross"] # i don't dare touch this yet

# libs have semi-auto-generated subpkgs using this array
# needs to be updated with new libs regularly
_libs = [
    "atomic", "chrono", "container", "context", "contract", "coroutine",
    "date_time", "fiber", "filesystem", "graph", "iostreams", "json", "locale",
    "log_setup", "log", "math", "nowide", "prg_exec_monitor", "program_options",
    "python", "random", "regex", "serialization", "stacktrace_addr2line",
    "stacktrace_basic", "stacktrace_noop", "system", "thread", "timer",
    "type_erasure", "unit_test_framework", "url", "wave", "wserialization",
]

match self.profile().arch:
    case "ppc64le" | "ppc64":
        _arch, _abi = "power", "sysv"
    case "aarch64":
        _arch, _abi = "arm", "aapcs"
    case "x86_64":
        _arch, _abi = "x86", "sysv"
    case "riscv64":
        _arch, _abi = "riscv", "sysv"
    case _:
        broken = f"Unknown CPU architecture: {self.profile().arch}"

def init_configure(self):
    self._pyver = self.do(
        "pkgconf", "--modversion", "python3", capture_output = True
    ).stdout.decode().strip()

def _call_b2(self, *args):
    self.do(
        self.chroot_cwd / "b2", f"-j{self.make_jobs}",
        f"--user-config={self.chroot_cwd}/user-config.jam",
        f"--prefix={self.chroot_destdir}/usr",
        "release",
        f"python={self._pyver}",
        "toolset=clang",
        "cxxflags=" + self.get_cxxflags(shell = True),
        "linkflags=" + self.get_ldflags(shell = True),
        "threading=multi",
        "debug-symbols=off",
        "runtime-link=shared",
        "link=shared,static",
        "--layout=system",
        *args
    )

def do_build(self):
    self.do(
        self.chroot_cwd / "bootstrap.sh",
        f"--prefix={self.chroot_destdir}/usr",
        f"--with-python=/usr/bin/python",
        f"--with-python-root=/usr"
    )

    with open(self.cwd / "user-config.jam", "w") as cf:
        cf.write(f"""
using clang : : {self.get_tool("CXX")} : <cxxflags>"{self.get_cxxflags(shell = True)}" <linkflags>"{self.get_ldflags(shell = True)}" <warnings-as-errors>"off" ;
using python : {self._pyver} : /usr/bin/python3 : /usr/include/python{self._pyver} : /usr/lib/python{self._pyver} ;
""")

    _call_b2(self)

def do_install(self):
    # install b2 globally
    self.install_bin("tools/build/src/engine/b2")

    # install boost itself
    _call_b2(self, "install")

    # install Boost.Build files
    self.install_dir("usr/share/b2")

    for f in (self.cwd / "tools/build").glob("*"):
        self.cp(f, self.destdir / "usr/share/b2", recursive = True)

    for f in (self.destdir / "usr/share/b2").rglob("*.orig"):
        f.unlink()

    self.rm(self.destdir / "usr/share/b2/src/engine/b2")

    self.install_dir("etc")

    with open(self.destdir / "etc/site-config.jam", "w") as sc:
        sc.write("""# System-wide configuration file for Boost.Build.

using clang ;
""")

    self.install_license("LICENSE_1_0.txt")

def do_check(self):
    self.do(
        "python", "test_all.py", "--default-bjam",
        wrksrc = "tools/build/test",
        env = {
            "PATH": f"{self.chroot_cwd}/tools/build/src/engine:/usr/bin"
        }
    )

@subpackage(f"boost-build")
def _jam(self):
    self.pkgdesc = f"{pkgdesc} (Boost.Build framework)"
    self.depends = [f"boost={pkgver}-r{pkgrel}"]
    self.provides = [f"boost{pkgver[:-2]}-build={pkgver}-r{pkgrel}"]

    return ["usr/bin/b2", "etc/site-config.jam", "usr/share/b2"]

@subpackage(f"boost-devel")
def _devel(self):
    self.depends = [f"boost={pkgver}-r{pkgrel}"] + makedepends
    self.provides = [f"boost{pkgver[:-2]}-devel={pkgver}-r{pkgrel}"]

    return self.default_devel()

def _gen_libp(libname):
    @subpackage(f"libboost_{libname}")
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({libname})"
        self.depends = [f"boost={pkgver}-r{pkgrel}"]

        return [f"usr/lib/libboost_{libname}*.so.*"]

for blib in _libs:
    _gen_libp(blib)
