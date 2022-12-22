pkgname = "desktop-file-utils"
pkgver = "0.26"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libglib-devel"]
triggers = ["/usr/share/applications"]
pkgdesc = "Utilities to manage desktop entries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://freedesktop.org/wiki/Software/desktop-file-utils"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "b26dbde79ea72c8c84fb7f9d870ffd857381d049a86d25e0038c4cef4c747309"

# FIXME visibility
hardening = ["!vis"]
