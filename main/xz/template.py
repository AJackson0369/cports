pkgname = "xz"
pkgver = "5.4.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "XZ compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:xz"
url = "https://tukaani.org/xz"
source = f"https://tukaani.org/xz/xz-{pkgver}.tar.bz2"
sha256 = "dd172acb53867a68012f94c17389401b2f274a1aa5ae8f84cbfb8b7e383ea8d3"
options = ["bootstrap"]

def post_install(self):
    self.install_license("COPYING")
    self.rm(self.destdir / "usr/share/doc", recursive = True)
    for tool in [
        "xzgrep", "xzfgrep", "xzegrep", "lzgrep", "lzfgrep", "lzegrep",
        "xzdiff", "lzdiff", "xzcmp", "lzcmp", "xzless", "xzmore",
        "lzless", "lzmore"
    ]:
        self.rm(self.destdir / "usr/bin" / tool)
        self.rm(self.destdir / "usr/share/man/man1" / (tool + ".1"))
        for lang in (self.destdir / "usr/share/man").iterdir():
            if lang.name == "man1":
                continue
            self.rm(lang / "man1" / (tool + ".1"), force = True)

@subpackage("liblzma")
def _lib(self):
    self.pkgdesc = "XZ-format compression library"

    return self.default_libs()

@subpackage("liblzma-devel")
def _devel(self):
    self.pkgdesc = "XZ-format compression library (development files)"

    return self.default_devel()
