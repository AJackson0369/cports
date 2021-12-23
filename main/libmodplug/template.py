pkgname = "libmodplug"
pkgver = "0.8.9.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-static"]
hostmakedepends = ["pkgconf"]
pkgdesc = "MOD playing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "http://modplug-xmms.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/modplug-xmms/{pkgname}-{pkgver}.tar.gz"
sha256 = "457ca5a6c179656d66c01505c0d95fafaead4329b9dbaa0f997d00a3508ad9de"

@subpackage("libmodplug-static")
def _static(self):
    return self.default_static()

@subpackage("libmodplug-devel")
def _devel(self):
    return self.default_devel()
