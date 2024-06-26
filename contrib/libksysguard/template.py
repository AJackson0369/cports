pkgname = "libksysguard"
pkgver = "6.1.1"
pkgrel = 0
build_style = "cmake"
# some bug in the cmake files seems to not set this to on
# configure_args = ["-DBUILD_NETWORK_PLUGIN=ON"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "libcap-progs",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kauth-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kjobwidgets-devel",
    "knewstuff-devel",
    "kpackage-devel",
    "kservice-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "libcap-devel",
    "libnl-devel",
    "libpcap-devel",
    "libsensors-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE system monitor library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later AND (GPL-2.0-only OR GPL-3.0-only)"
url = "https://api.kde.org/plasma/libksysguard/html"
source = f"$(KDE_SITE)/plasma/{pkgver}/libksysguard-{pkgver}.tar.xz"
sha256 = "bc1ed804373865d3de51e5e1cf7ad11c4b71ea131110a3940725b04332caee52"
file_modes = {
    "usr/libexec/ksysguard/ksgrd_network_helper": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/libexec/ksysguard/ksgrd_network_helper": {
        "security.capability": "cap_net_raw+ep",
    },
}
# FIXME: cfi crashes plasma-systemmonitor on launch in libKSysGuardSensors.so
hardening = ["vis", "!cfi"]


@subpackage("libksysguard-devel")
def _devel(self):
    return self.default_devel()
