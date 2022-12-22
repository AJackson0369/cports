# this package exists so that we can build harfbuzz (and cairo, which harfbuzz
# needs); after that we can build real freetype with harfbuzz support and get
# better hinting - do not actually use this package in a regular system
pkgname = "freetype-bootstrap"
pkgver = "2.12.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dbrotli=disabled",
    "-Dharfbuzz=disabled",
    "-Dbzip2=disabled",
    "-Dzlib=disabled",
    "-Dpng=disabled",
    "-Dtests=disabled",
    "-Dmmap=enabled",
    "-Ddefault_library=shared",
]
hostmakedepends = ["meson", "pkgconf"]
# conflict with the real stuff
depends = ["!freetype", "!freetype-devel"]
# provide lowest possible version
provides = ["so:libfreetype.so.6=0"]
pkgdesc = "Font rendering engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "FTL OR GPL-2.0-or-later"
url = "https://freetype.org"
source = f"$(NONGNU_SITE)/freetype/freetype-{pkgver}.tar.xz"
sha256 = "4766f20157cc4cf0cd292f80bf917f92d1c439b243ac3018debf6b9140c41a7f"
options = ["!lto", "!scanshlibs"]

def post_install(self):
    self.install_license("LICENSE.TXT")
    self.install_license("docs/FTL.TXT")

# FIXME visibility
hardening = ["!vis"]
