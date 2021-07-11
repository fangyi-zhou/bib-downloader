import sys
from typing import List

from . import doi


def main(args: List[str]) -> int:
    if len(args) == 0:
        arg = input("Enter an DOI: ")
    else:
        arg = args[0]
    # TODO: Better input handling
    try:
        print(doi.process_input(arg))
        return 0
    except:
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
