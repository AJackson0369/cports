pkgname = "gnome-control-center"
pkgver = "43.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "gettext-tiny",
    "glib-devel", "polkit", "python"
]
makedepends = [
    "libhandy-devel", "accountsservice-devel", "colord-devel",
    "colord-gtk-devel", "libglib-devel", "gnome-desktop-devel",
    "gnome-settings-daemon-devel", "gnome-online-accounts-devel",
    "gsettings-desktop-schemas-devel", "libxml2-devel", "polkit-devel",
    "libpulse-devel", "upower-devel", "libgudev-devel", "libx11-devel",
    "libxi-devel", "libepoxy-devel", "gtk4-devel", "cups-devel",
    "ibus-devel", "networkmanager-devel", "modemmanager-devel",
    "gnome-bluetooth-devel", "libwacom-devel", "gcr-devel", "libnma-devel",
    "libsecret-devel", "udisks-devel", "gsound-devel", "libgtop-devel",
    "heimdal-devel", "libpwquality-devel", "libsmbclient-devel", "gnutls-devel",
]
depends = [
    "udisks", "cups-pk-helper", "gsettings-desktop-schemas",
    "sound-theme-freedesktop",
]
pkgdesc = "GNOME control center"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-control-center"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "988c933592cbdc4e7f0dba9a93262e617b739e25927aa16e177960c754e31c48"
# needs graphical environment
options = ["!check"]

def pre_build(self):
    # racey, included from elsewhere but not dependencies
    self.make.invoke("panels/network/cc-network-resources.h")

@subpackage("gnome-control-center-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()
