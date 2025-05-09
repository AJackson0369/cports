pkgname = "kpimtextedit"
pkgver = "25.04.1"
pkgrel = 0
build_style = "cmake"
# hangs
make_check_args = ["-E", "richtextcomposertest"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcodecs-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "ktextaddons-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
    "sonnet-devel",
    "syntax-highlighting-devel",
]
pkgdesc = "KDE PIM textedit class"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/kdepim/kpimtextedit/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kpimtextedit-{pkgver}.tar.xz"
)
sha256 = "dbe8060425220e1b6202ec39e31f8ec96e606fdf66dcbb2c39978947deea77be"


@subpackage("kpimtextedit-devel")
def _(self):
    return self.default_devel()
