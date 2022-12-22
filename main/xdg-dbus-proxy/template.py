pkgname = "xdg-dbus-proxy"
pkgver = "0.1.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-man"]
hostmakedepends = ["pkgconf", "xsltproc", "docbook-xsl-nons"]
makedepends = ["libglib-devel"]
checkdepends = ["dbus"]
pkgdesc = "Filtering proxy for D-Bus connections"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/flatpak/xdg-dbus-proxy"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "1ec0eab53d1e49966d722352bcfd51ac402dce5190baedc749a8541e761670ab"

# FIXME visibility
hardening = ["!vis"]
