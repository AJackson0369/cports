pkgname = "juk"
pkgver = "25.04.2"
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
    "kcompletion-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kjobwidgets-devel",
    "knotifications-devel",
    "kstatusnotifieritem-devel",
    "ktextwidgets-devel",
    "kwallet-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "phonon-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "taglib-devel",
]
# TODO: can't play anything without a phonon backend (vlc)
pkgdesc = "KDE music player and manager"
license = "GPL-2.0-only"
url = "https://juk.kde.org"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/juk-{pkgver}.tar.xz"
sha256 = "e404d37b0ea44b9272035d7135124ffb6ce7052926c4ae365c157df245e0426e"
