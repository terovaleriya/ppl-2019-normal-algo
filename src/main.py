import logging
from typing import Tuple, List

Rule = Tuple[str, str, bool]
Scheme = List[Rule]


def apply_scheme(rules: Scheme, inp: str) -> str:
    line = inp
    while True:
        for rule in rules:
            p0, p1, terminate = rule
            if len(p0) == 0:
                nline = p1 + line
            else:
                nline = line.replace(p0, p1)
            if line != nline:
                if terminate is True:
                    logging.debug("Terminating with `" + nline + "`")
                    return nline
                else:
                    logging.debug("Iteration with `" + nline + "`")
                    line = nline
                    break
        if line == inp:
            logging.error("Scheme is not applicable")
            assert False


def parse_rule(inp: str) -> Rule:
    parts = inp.split("->")
    p0 = parts[0]
    p1 = parts[1]
    terminal = p1.startswith(".")
    if terminal:
        p1 = p1[1:]
    rule = p0, p1, terminal
    return rule


def parse_scheme(inp: str) -> Scheme:
    return list(map(parse_rule, inp.split(";")))

