pkgname = "sqlite"
pkgver = "3.36.0"
_amalg = "3360000"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-threadsafe", "--enable-dynamic-extensions", "--enable-fts5"
]
hostmakedepends = ["pkgconf"]
makedepends = ["libedit-devel", "zlib-devel"]
pkgdesc = "SQL Database Engine in a C library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://sqlite.org"
source = f"https://sqlite.org/2021/sqlite-autoconf-{_amalg}.tar.gz"
sha256 = "bd90c3eb96bee996206b83be7065c9ce19aef38c3f4fb53073ada0d0b69bbce3"
options = ["!parallel"]

_cflags = [
    "-DSQLITE_ENABLE_DBSTAT_VTAB", "-DSQLITE_ENABLE_COLUMN_METADATA",
    "-DSQLITE_ENABLE_UNLOCK_NOTIFY", "-DSQLITE_SECURE_DELETE",
    "-DSQLITE_ENABLE_JSON1", "-DSQLITE_ENABLE_FTS3",
    "-DSQLITE_ENABLE_FTS3_PARENTHESIS", "-DSQLITE_ENABLE_FTS4",
    "-DSQLITE_ENABLE_FTS3_TOKENIZER=1", "-DSQLITE_ENABLE_BATCH_ATOMIC_WRITE=1",
    "-DSQLITE_ENABLE_DESERIALIZE",

    "-DHAVE_FDATASYNC"
]

if current.profile().endian == "big":
    _cflags += ["-DSHA3_BYTEORDER=4321", "-DSQLITE_BYTEORDER=4321"]
else:
    _cflags += ["-DSHA3_BYTEORDER=1234", "-DSQLITE_BYTEORDER=1234"]

tool_flags = {"CFLAGS": _cflags}

@subpackage("sqlite-devel")
def _devel(self):
    return self.default_devel()
