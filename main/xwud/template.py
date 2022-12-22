pkgname = "xwud"
pkgver = "1.0.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel"]
pkgdesc = "X image displayer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.gz"
sha256 = "262171b0c434966ddbbe8a54afb9615567ad74d4cc2e823e14e51e099ec3ab0d"

def post_install(self):
    self.install_license("COPYING")

# FIXME visibility
hardening = ["!vis"]
