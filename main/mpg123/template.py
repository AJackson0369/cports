pkgname = "mpg123"
pkgver = "1.30.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-optimization=0", "--with-default-audio=pulse",
    "--enable-ipv6=yes", "--enable-network=yes",
    "--disable-lfs-alias",
]
hostmakedepends = ["pkgconf"]
makedepends = [
    "pipewire-jack-devel", "libpulse-devel", "sdl-devel", "linux-headers"
]
depends = [f"mpg123-output-dummy={pkgver}-r{pkgrel}"]
pkgdesc = "MPEG 1.0/2.0/2.5 audio player"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://www.mpg123.org"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "c7ea863756bb79daed7cba2942ad3b267a410f26d2dfbd9aaf84451ff28a05d7"

def _genlib(libn, descn, iif):
    @subpackage(f"mpg123-output-{libn}")
    def _out(self):
        self.pkgdesc = f"{pkgdesc} ({descn} output plugin)"
        if iif:
            self.install_if = [f"{pkgname}-libs={pkgver}-r{pkgrel}", iif]

        return [f"usr/lib/mpg123/output_{libn}.so"]

for libn, descn, iif in [
    ("oss", "OSS", None),
    ("jack", "JACK", "jack"),
    ("pulse", "PulseAudio", "libpulse"),
    ("sdl", "SDL", "sdl"),
    ("dummy", "dummy", None),
]:
    _genlib(libn, descn, iif)

@subpackage("mpg123-libs")
def _libs(self):
    self.depends = [f"mpg123-output-dummy={pkgver}-r{pkgrel}"]

    return self.default_libs()

@subpackage("mpg123-devel")
def _devel(self):
    return self.default_devel()
