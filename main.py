import sys
import importlib
from pathlib import Path


if len(sys.argv) < 2:
    print("Wrong number of arguments")
    print("Usage: python main.py [test] 01")
    sys.exit(1)

is_test = sys.argv[1] == "test"
day = sys.argv[2] if is_test else sys.argv[1]
module = importlib.import_module(f"day-{day}")


def run_part(code: int):
    if is_test:
        input = Path(f"inputs/day-01_test-{code}.txt").read_text()
    else:
        input = Path(f"inputs/day-{day}.txt").read_text()

    try:
        func = getattr(module, f"part_{code}")
    except AttributeError:
        return

    output = func(input)
    print(output)


run_part(1)
run_part(2)
