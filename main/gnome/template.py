pkgname = "gnome"
pkgver = "41"
pkgrel = 0
build_style = "meta"
depends = [
    f"gnome-core>={pkgver}",
    "baobab",
    #"eog",
    "epiphany",
    "evince",
    "gedit",
    #"gnome-calculator",
    #"gnome-calendar",
    #"gnome-characters",
    #"gnome-clocks",
    #"gnome-contacts",
    #"gnome-connections",
    #"gnome-disk-utility",
    #"gnome-font-viewer",
    #"gnome-maps",
    #"gnome-music",
    #"gnome-remote-desktop",
    "gnome-screenshot",
    "gnome-shell-extensions",
    #"gnome-system-monitor",
    "gnome-terminal",
    "gnome-user-docs",
    #"gnome-user-share",
    #"gnome-weather",
    #"orca",
    #"phodav",
    "simple-scan",
    "sushi",
    #"totem",
]
pkgdesc = "GNOME desktop environment (session and apps)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://www.gnome.org"
