pkgname = "kate"
pkgver = "25.04.1"
pkgrel = 1
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knewstuff-devel",
    "ktexteditor-devel",
    "ktextwidgets-devel",
    "kuserfeedback-devel",
    "kwallet-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "qtkeychain-devel",
]
depends = ["konsole"]
pkgdesc = "KDE Advanced Text Editor"
license = "LGPL-2.1-or-later"
url = "https://apps.kde.org/kate"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kate-{pkgver}.tar.xz"
sha256 = "820f0412a8485472844ea83881c47e1b90093ce3e2729e6910f9d3593fe530aa"
hardening = ["vis"]
# no idea
options = ["!check"]


# for kwrite to not pull in kate
@subpackage("kate-libs")
def _(self):
    return self.default_libs()


@subpackage("kate-kwrite")
def _(self):
    self.subdesc = "KWrite"
    self.provides = [self.with_pkgver("kwrite")]
    return [
        "usr/bin/kwrite",
        "usr/share/icons/hicolor/*/apps/kwrite.*",
        "usr/share/applications/org.kde.kwrite.desktop",
        "usr/share/metainfo/org.kde.kwrite.appdata.xml",
    ]
