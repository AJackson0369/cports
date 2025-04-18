pkgname = "libkdepim"
pkgver = "25.04.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kldap-devel",
    "kcompletion-devel",
    "ki18n-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE PIM common library"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://api.kde.org/kdepim/libkdepim/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkdepim-{pkgver}.tar.xz"
sha256 = "c36a50f85201a6f5393d896e472bf5fe99656b8c76cae8e3facf878b17766b7d"


@subpackage("libkdepim-devel")
def _(self):
    return self.default_devel()
