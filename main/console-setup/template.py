pkgname = "console-setup"
pkgver = "1.228"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "build-linux"
make_install_target = "install-linux"
hostmakedepends = [
    "bdfresize",
    "font-unifont-bdf",
    "fonts-dejavu-otf",
    "gmake",
    "mandoc",
    "otf2bdf",
    "perl",
    "perl-xml-parser",
]
depends = ["kbd"]
pkgdesc = "Console font and keymap setup program"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND custom:console-setup"
url = "https://salsa.debian.org/installer-team/console-setup"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "98f5511fe0882a55fcc07378e872c949ee25a4717c82310c1691f46470765bb0"
# no tests
options = ["bootstrap", "!check"]


def pre_build(self):
    self.make.invoke("maintainer-clean")


def do_install(self):
    self.install_dir("usr/bin")
    self.install_link("bin", "usr/bin")
    self.make.install(
        [
            "prefix=" + str(self.chroot_destdir / "usr"),
            "etcdir=" + str(self.chroot_destdir / "etc"),
        ]
    )
    self.rm(self.destdir / "bin")


def post_install(self):
    self.install_license("debian/copyright")


@subpackage("console-setup-xkb")
def _xkb(self):
    self.pkgdesc = f"{pkgdesc} (optional XKB keymap support)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "xkeyboard-config", "perl"]
    self.install_if = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "xkeyboard-config",
        "perl",
    ]
    return ["usr/bin/ckbcomp"]
