pkgname = "opusfile"
pkgver = "0.12"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libogg-devel", "opus-devel", "openssl-devel"]
pkgdesc = "Library for opening, seeking, and decoding .opus files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.opus-codec.org"
source = f"http://downloads.xiph.org/releases/opus/{pkgname}-{pkgver}.tar.gz"
sha256 = "118d8601c12dd6a44f52423e68ca9083cc9f2bfe72da7a8c1acb22a80ae3550b"

def post_install(self):
    self.rm(self.destdir / "usr/share", recursive = True)
    self.install_license("COPYING")

@subpackage("opusfile-static")
def _static(self):
    return self.default_static()

@subpackage("opusfile-devel")
def _devel(self):
    return self.default_devel()
