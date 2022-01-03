pkgname = "perl"
pkgver = "5.34.0"
pkgrel = 0
_perl_cross_ver = "1.3.6"
build_style = "gnu_configure"
make_cmd = "gmake"
make_check_target = "test"
hostmakedepends = ["gmake", "less"]
makedepends = ["zlib-devel", "libbz2-devel"]
checkdepends = ["iana-etc", "perl-AnyEvent", "perl-Test-Pod", "procps-ng"]
depends = ["less"]
pkgdesc = "Practical Extraction and Report Language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://www.perl.org"
source = [
    f"https://www.cpan.org/src/5.0/perl-{pkgver}.tar.gz",
    f"https://github.com/arsv/perl-cross/releases/download/{_perl_cross_ver}/perl-cross-{_perl_cross_ver}.tar.gz"
]
sha256 = [
    "551efc818b968b05216024fb0b727ef2ad4c100f8cb6b43fab615fa78ae5be9a",
    "4010f41870d64e3957b4b8ce70ebba10a7c4a3e86c5551acb4099c3fcbb37ce5"
]
# prevent a massive log dump
tool_flags = {
    "CFLAGS": [
        "-Wno-compound-token-split-by-macro",
        "-DNO_POSIX_2008_LOCALE",
        "-D_GNU_SOURCE",
    ],
    "LDFLAGS": ["-Wl,-z,stack-size=2097152", "-pthread"],
}
# check is cyclic: depends on perl modules
options = ["!check"]

def pre_patch(self):
    for f in (self.cwd / f"perl-{pkgver}").iterdir():
        self.mv(f, ".")

    for f in (self.cwd / f"perl-cross-{_perl_cross_ver}").iterdir():
        if f.name == "utils":
            self.mv(f / "Makefile", "utils")
            f.rmdir()
            continue
        self.mv(f, ".")

def init_configure(self):
    from cbuild.util import make

    self.make = make.Make(self, wrksrc = ".")

    self.env["HOSTCFLAGS"] = "-D_GNU_SOURCE"

    self.tools["LD"] = self.tools["CC"]

    # to prevent perl buildsystem from invoking bmake
    self.env["MAKE"] = self.make.get_command()

def do_configure(self):
    cargs = [
        "--prefix=/usr",
        "-Dusethreads", "-Duseshrplib", "-Dusesoname", "-Dusevendorprefix",
        "-Dprefix=/usr", "-Dvendorprefix=/usr",
        "-Dprivlib=/usr/share/perl5/core_perl",
        "-Darchlib=/usr/lib/perl5/core_perl",
        "-Dsitelib=/usr/share/perl5/site_perl",
        "-Dsitearch=/usr/lib/perl5/site_perl",
        "-Dvendorlib=/usr/share/perl5/vendor_perl",
        "-Dvendorarch=/usr/lib/perl5/vendor_perl",
        "-Dscriptdir=/usr/bin", "-Dvendorscript=/usr/bin",
        "-Dinc_version_list=none", "-Dman1ext=1p", "-Dman3ext=3p",
        "-Dman1dir=/usr/share/man/man1",
        "-Dman3dir=/usr/share/man/man3",
        "-Dd_sockaddr_in6=define",
    ]

    if self.profile().cross:
        cargs.append("--target=" + self.profile().triplet)

    cfl = self.get_cflags(shell = True)
    lfl = self.get_ldflags(shell = True)

    cargs.append("-Dcccdlflags=-fPIC")
    cargs.append("-Doptimize=-Wall " + cfl)
    cargs.append("-Dccflags=" + cfl)
    cargs.append("-Dlddlflags=-shared " + lfl)
    cargs.append("-Dldflags=" + lfl)
    cargs.append("-Dperl_static_inline=static __inline__")
    cargs.append("-Dd_static_inline")

    self.do(self.chroot_cwd / "configure", *cargs)

def do_check(self):
    self.make.check(env = {
        "TEST_JOBS": str(self.make_jobs),
        "PERL_BUILD_PACKAGING": "1",
    })

def post_install(self):
    for f in (self.destdir / "usr/share").rglob("*"):
        if f.is_file() and not f.is_symlink():
            f.chmod(0o644)

    for f in (self.destdir / "usr/lib").rglob("*"):
        if f.is_file() and not f.is_symlink():
            f.chmod(0o644)

    self.install_link("perl", f"usr/bin/perl{pkgver}")

    # remove all pod files except those under
    # /usr/share/perl5/core_perl/pod/ (FS#16488)
    for f in (self.destdir / "usr/share/perl5/core_perl").glob("*.pod"):
        f.unlink()

    for d in (self.destdir / "usr/share/perl5/core_perl").iterdir():
        if not d.is_dir() or d.name == "pod":
            continue
        for f in d.rglob("*.pod"):
            f.unlink()

    for f in (self.destdir / "usr/lib").rglob("*.pod"):
        f.unlink()

    for f in self.destdir.rglob(".packlist"):
        f.unlink()

    import re
    import os

    cfpath = self.destdir / "usr/lib/perl5/core_perl/Config_heavy.pl"
    with open(cfpath) as ifile:
        with open(self.cwd / "Config_heavy.pl.new", "w") as ofile:
            for ln in ifile:
                ln = re.sub("-specs=.*hardened-ld", "", ln)
                ln = re.sub("-specs=.*hardened-cc1", "", ln)
                ofile.write(ln)

    cfpath.unlink()
    os.rename(self.cwd / "Config_heavy.pl.new", cfpath)
    cfpath.chmod(0o644)

    # convert hardlinks
    hf = self.destdir / "usr/share/man/man1/perlthanks.1p"
    hf.unlink()
    hf.symlink_to("perlbug.1p")
    hf = self.destdir / "usr/bin/perlthanks"
    hf.unlink()
    hf.symlink_to("perlbug")
