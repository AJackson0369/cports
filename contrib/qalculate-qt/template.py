pkgname = "qalculate-qt"
# match to libqalculate
pkgver = "5.2.0.1"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_use_env = True
hostmakedepends = [
    "gmake",
    "pkgconf",
    "qt6-qtbase-devel",
    "qt6-qttools",
]
makedepends = [
    "libqalculate-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Qt frontend for libqalculate"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://qalculate.github.io"
source = f"https://github.com/Qalculate/qalculate-qt/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c9dd4b7b3c6a9f857db9f04b469b2becd4047a0782bdf507469b0491152bbf07"


def do_configure(self):
    # TODO: build style these
    self.do(
        "qmake6",
        "PREFIX=/usr",
        f"QMAKE_CFLAGS={self.get_cflags(shell=True)}",
        f"QMAKE_CXXFLAGS={self.get_cxxflags(shell=True)}",
        f"QMAKE_LFLAGS={self.get_ldflags(shell=True)}",
    )


def init_install(self):
    self.make_install_args += [f"INSTALL_ROOT={self.chroot_destdir}"]
