pkgname = "zip"
pkgver = "3.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "zips"
make_use_env = True
hostmakedepends = ["gmake"]
depends = ["unzip"] # zip -T
pkgdesc = "Create/update ZIP files compatible with pkzip"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Info-ZIP"
url = "http://infozip.sf.net"
source = f"$(SOURCEFORGE_SITE)/infozip/{pkgname}30.tar.gz"
sha256 = "f0e8bb1f9b7eb0b01285495a2699df3a4b766784c1765a8f1aeedf63c0806369"
tool_flags = {
    "CFLAGS": ["-DLARGE_FILE_SUPPORT"]
}
# no test suite
options = ["!check"]

def do_build(self):
    cfl = self.get_cflags(shell = True)
    ldfl = self.get_ldflags(shell = True)

    self.make.build([
        "-f", "unix/Makefile", "prefix=/usr", "LOCAL_ZIP=" + cfl,
        "CC=" + self.get_tool("CC"), "CPP=" + self.get_tool("CC") + " -E",
        "LFLAGS2=" + cfl + " " + ldfl,
    ])

def do_install(self):
    self.make.install([
        "-f", "unix/Makefile", "PREFIX=/usr",
        "DESTDIR=" + str(self.chroot_destdir),
    ])

    self.install_license("LICENSE")

# FIXME visibility
hardening = ["!vis"]
