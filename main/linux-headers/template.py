pkgname = "linux-headers"
pkgver = "5.15.5"
pkgrel = 0
make_cmd = "gmake"
hostmakedepends = ["gmake", "perl"]
pkgdesc = "Linux API headers for userland development"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://www.kernel.org"
source = f"$(KERNEL_SITE)/kernel/v{pkgver[0]}.x/linux-{pkgver}.tar.xz"
sha256 = "e9565a301525ac81c142ceb832f9053dd5685e107dbcf753d0de4c58bc98851f"
hardening = ["!vis"]
# nothing to test
options = ["!check"]

match self.profile().arch:
    case "x86_64": _arch = "x86_64"
    case "aarch64": _arch = "arm64"
    case "ppc64le" | "ppc64": _arch = "powerpc"
    case "riscv64": _arch = "riscv"
    case _:
        broken = f"Unknown CPU architecture: {self.profile().arch}"

def do_build(self):
    from cbuild.util import make

    mk = make.Make(self, jobs = 1)

    tcfl = self.get_cflags(shell = True)
    tlfl = self.get_ldflags(shell = True)
    tcc = self.get_tool("CC")
    with self.profile("host"):
        hcfl = self.get_cflags(shell = True)
        hlfl = self.get_ldflags(shell = True)
        hcc = self.get_tool("CC")

    mk.invoke("mrproper", [
        "ARCH=" + _arch,
        "CC=" + tcc,
        "HOSTCC=" + hcc,
        "CFLAGS=" + tcfl,
        "HOSTCFLAGS=" + hcfl,
        "LDFLAGS=" + tlfl,
        "HOSTLDFLAGS=" + hlfl,
        "headers"
    ])

    # remove extra files and drm headers
    for fn in self.find(".", ".*", files = True):
        self.rm(fn)

    self.rm("usr/include/Makefile")
    self.rm("usr/include/drm", recursive = True)

def do_install(self):
    self.install_files("usr/include", "usr")
