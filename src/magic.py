from src.main import parse_scheme, apply_scheme

scheme = input("Enter Bragilevsky\'s Scheme:\n")
inp = input("Enter input string:\n")

result = apply_scheme(parse_scheme(scheme), inp)
print("String after scheme application:\n" + result)
print("❤ ❤ ❤")