pkgname = "kpublictransport"
pkgver = "25.04.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ki18n-devel",
    "networkmanager-qt-devel",
    "protobuf-devel",
    "qt6-qtdeclarative-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "KDE library for accessing public transport information"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kpublictransport/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kpublictransport-{pkgver}.tar.xz"
)
sha256 = "04786ba7e86bd54a11bc64c318cd6b9ffb91787ea6892c0330ce7ccc0570b2a8"


@subpackage("kpublictransport-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel", "zlib-ng-compat-devel"]
    return self.default_devel()
