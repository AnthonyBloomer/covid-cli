import sys

from .parser import Parser
from .utils import create_table

parser = Parser()
args = parser.parse_args()


def main():
    create_table(args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
