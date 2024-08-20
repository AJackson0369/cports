pkgname = "kservice"
pkgver = "6.5.0"
pkgrel = 0
build_style = "cmake"
# flaky tests when parallel
make_check_args = ["-j1"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Plugin framework for desktop services"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kservice/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kservice-{pkgver}.tar.xz"
sha256 = "48cdd204bc9fb9282c37b6bcc2364f7dbc124057547ddb6b1471988b464cf8bd"
hardening = ["vis"]


@subpackage("kservice-devel")
def _(self):
    self.depends += ["kconfig-devel", "kcoreaddons-devel"]

    return self.default_devel()
