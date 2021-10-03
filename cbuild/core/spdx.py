import json

_opprec = {
    "OR": 1,
    "AND": 2,
}

class SPDXParser:
    def __init__(self, spath):
        self.ldict = {}
        self.edict = {}

        def _license_parse(v):
            if "licenseId" in v:
                self.ldict[v["licenseId"]] = v

        def _exception_parse(v):
            if "licenseExceptionId" in v:
                self.edict[v["licenseExceptionId"]] = v

        with open(spath / "licenses.json") as f:
            json.load(f, object_hook = _license_parse)

        with open(spath / "exceptions.json") as f:
            json.load(f, object_hook = _exception_parse)

    def lex(self):
        while True:
            # skip whitespace before matching any token
            nsp = 0
            while self.stream[nsp:nsp + 1].isspace():
                nsp = nsp + 1
            if nsp:
                self.stream = self.stream[nsp:]
                continue
            # early exit
            if len(self.stream) == 0:
                return None
            # see if we match a known token
            if self.stream[0:1] == "(" or self.stream[0:1] == ")":
                tok = self.stream[0]
                self.stream = self.stream[1:]
                return tok
            elif self.stream[0:4] == "WITH":
                self.stream = self.stream[4:]
                return "WITH"
            elif self.stream[0:3] == "AND":
                self.stream = self.stream[3:]
                return "AND"
            elif self.stream[0:2] == "OR":
                self.stream = self.stream[2:]
                return "OR"
            # otherwise see if we match a license id, maybe with a +
            idlen = 0
            stlen = len(self.stream)
            while stlen > idlen:
                c = self.stream[idlen]
                if (c != "-") and (c != ".") and not c.isalnum():
                    break
                idlen = idlen + 1
            # didn't get any valid character
            if idlen == 0:
                raise RuntimeError("unknown token: " + self.stream[0])
            tok = self.stream[0:idlen]
            # this must be a license id and it's not one
            if not tok in self.ldict and not tok in self.edict:
                raise RuntimeError("unknown token: " + tok)
            # may be directly followed by a +
            if self.stream[idlen:idlen + 1] == "+":
                tok = tok + "+"
                idlen = idlen + 1
            # return the token
            self.stream = self.stream[idlen:]
            return tok

    def parse_simple(self):
        if not self.token:
            raise RuntimeError("token expected")
        tok = self.token
        # parenthesized expression
        if tok == "(":
            self.token = self.lex()
            self.parse_expr()
            if self.token != ")":
                raise RuntimeError("')' expected to close '('")
            self.token = self.lex()
            return
        # license id maybe with exception
        if tok.endswith("+"):
            tok = tok[0:len(tok) - 1]
        if not tok in self.ldict:
            raise RuntimeError("license id expected, got: " + tok)
        # check for exception
        self.token = self.lex()
        if self.token == "WITH":
            self.token = self.lex()
            if not self.token:
                raise RuntimeError("token expected")
            if not self.token in self.edict:
                raise RuntimeError("exception id expected, got: " + tok)
            self.token = self.lex()

    def parse_expr(self, mprec = 1):
        # parse lhs
        self.parse_simple()
        # parse the rest
        while True:
            # no operator follows
            if not self.token:
                break
            # we're expecting an operator to be here
            # if it's not one, let the parent call handle it
            if not self.token in _opprec:
                break
            # deal with precedence
            oprec = _opprec[self.token]
            if oprec < mprec:
                break
            # expecting an rhs
            self.token = self.lex()
            if not self.token:
                raise RuntimeError("token expected")
            # for right associative this would be just oprec
            # we don't have any right associative operators here
            nprec = oprec + 1
            # parse rhs, repeat
            self.parse_expr(nprec)

    def parse(self, str):
        self.stream = str
        self.token = self.lex()
        self.parse_expr()
        if self.token:
            raise RuntimeError("invalid token: " + self.token)

_parser = None

def init():
    from cbuild.core import paths
    global _parser
    _parser = SPDXParser(paths.distdir() / "cbuild/spdx")

def validate(str):
    _parser.parse(str)
