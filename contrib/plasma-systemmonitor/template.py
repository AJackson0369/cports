pkgname = "plasma-systemmonitor"
pkgver = "6.1.1"
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
    "kconfig-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "kitemmodels-devel",
    "knewstuff-devel",
    "kpackage-devel",
    "kservice-devel",
    "libksysguard-devel",
    "qt6-qtdeclarative-devel",
]
depends = [
    "kquickcharts",
    "ksystemstats",
]
pkgdesc = "KDE System Resource Usage Monitor"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://apps.kde.org/plasma-systemmonitor"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-systemmonitor-{pkgver}.tar.xz"
sha256 = "738162c98e6508a3eaa10361edfba7e0e6cd77f797e995f366e42aa52d40e9e3"
# FIXME: cfi crash on launch
hardening = ["vis", "!cfi"]
