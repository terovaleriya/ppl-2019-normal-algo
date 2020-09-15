import logging

from src.main import apply_scheme, parse_scheme


def test(rules: str, inp: str, output: str):
    assert apply_scheme(parse_scheme(rules), inp) == output, ("Expected string is not equal to output", inp, output)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s: %(message)s"
    )
    test("b->.a;a->b", "aaa", "aaa")
    test("*a->.;*b->.;->*", "abab", "bab")
    test("*a->.;*b->.;->*", "baba", "aba")
    test("0b->.1;1b->b0;b->.1;a0->0a;a1->1a;0a->0b;1a->1b;->a", "0", "1")
    test("01->.1;1b->b0;b->.1;a0->0a;a1->1a;0a->0b;1a->1b;->a", "1", "10")
    test("01->.1;1b->b0;b->.1;a0->0a;a1->1a;0a->0b;1a->1b;->a", "11", "100")
    # test("01->.1;1b->b0;b->.1;a0->0a;a1->1a;0a->0b;1a->1b;->a", "", "") // Infinite loop
