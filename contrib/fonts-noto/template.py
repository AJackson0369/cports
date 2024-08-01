pkgname = "fonts-noto"
pkgver = "24.8.1"
pkgrel = 0
pkgdesc = "Google Noto fonts"
maintainer = "GeopJr <evan@geopjr.dev>"
license = "OFL-1.1"
url = "https://github.com/notofonts/notofonts.github.io"
source = f"{url}/archive/refs/tags/noto-monthly-release-{pkgver}.zip"
sha256 = "6eff68e142d68ea2258180f441f2c6045bb08955f42d6f7270a229dfc9d88044"


def do_install(self):
    for f in self.files_path.glob("*.conf"):
        self.install_file(f, "usr/share/fontconfig/conf.avail")

    self.install_file(
        "fonts/Noto*/hinted/ttf/*.ttf", "usr/share/fonts/noto", glob=True
    )

    self.install_file(
        "fonts/Noto*/unhinted/otf/*.otf", "usr/share/fonts/noto", glob=True
    )


def post_install(self):
    self.install_license("fonts/LICENSE")


def _gensub(subn, subd, subc):
    @subpackage(f"fonts-noto-{subn}")
    def _sub(self):
        self.subdesc = subd
        self.depends = [self.parent, f"!{pkgname}-{subc}"]
        if subn == "otf":
            self.install_if = [self.parent]

        return [
            f"usr/share/fonts/noto/Noto*-Bold.{subn}",
            f"usr/share/fonts/noto/Noto*-Regular.{subn}",
        ]

    @subpackage(f"fonts-noto-extra-{subn}")
    def _sub_extra(self):
        self.subdesc = f"{subd} additional variants"
        self.depends = [
            self.with_pkgver(f"{pkgname}-extra"),
            f"!{pkgname}-extra-{subc}",
            f"!{pkgname}-{subc}",
        ]
        if subn == "otf":
            self.install_if = [self.with_pkgver(f"{pkgname}-extra")]

        return [f"usr/share/fonts/noto/*.{subn}"]


for _subn, _subd, _subc in [
    ("otf", "OpenType", "ttf"),
    ("ttf", "TrueType", "otf"),
]:
    _gensub(_subn, _subd, _subc)


@subpackage("fonts-noto-extra")
def _extra(self):
    self.subdesc = "additional variants"
    self.depends = [self.parent]
    self.options = ["empty"]

    return []
