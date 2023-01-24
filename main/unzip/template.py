pkgname = "unzip"
pkgver = "6.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "unzips"
make_check_target = "test"
make_use_env = True
hostmakedepends = ["gmake"]
makedepends = ["libbz2-devel"]
pkgdesc = "List, test and extract compressed files in a ZIP archive"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Info-ZIP"
url = "http://infozip.sf.net"
source = f"$(SOURCEFORGE_SITE)/infozip/{pkgname}60.tar.gz"
sha256 = "036d96991646d0449ed0aa952e4fbe21b476ce994abc276e49d30e686708bd37"
tool_flags = {
    "CFLAGS": [
        "-DWILD_STOP_AT_DIR", "-DLARGE_FILE_SUPPORT", "-DUNICODE_SUPPORT",
        "-DUNICODE_WCHAR", "-DUTF8_MAYBE_NATIVE", "-DNO_LCHMOD",
        "-DDATE_FORMAT=DF_YMD", "-DUSE_BZIP2", "-DNATIVE",
    ]
}
hardening = ["vis", "cfi"]

def do_build(self):
    cfl = self.get_cflags(shell = True)
    ldfl = self.get_ldflags(shell = True)

    self.make.build([
        "-f", "unix/Makefile", "prefix=/usr", "LF2=", "LOCAL_UNZIP=" + cfl,
        "CC=" + self.get_tool("CC"), "CFLAGS=" + cfl,
        "LFLAGS1=" + cfl + " " + ldfl,
        "D_USE_BZ2=-DUSE_BZIP2", "L_BZ2=-lbz2"
    ])

def do_check(self):
    self.make.check(["-f", "unix/Makefile"])

def do_install(self):
    self.make.install([
        "-f", "unix/Makefile", "prefix=" + str(self.chroot_destdir / "usr"),
        "INSTALL_PROGRAM=install"
    ])

    # hardlink
    self.rm(self.destdir / "usr/bin/zipinfo")
    self.install_link("unzip", "usr/bin/zipinfo")

    self.install_dir("usr/share")
    self.mv(self.destdir / "usr/man", self.destdir / "usr/share")

    self.install_license("LICENSE")
