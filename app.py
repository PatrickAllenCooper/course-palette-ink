"""Choose readable chart ink using a designer-provided palette."""
from pathlib import Path
import argparse
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "vendor"))
import webcolors
from candidate import ink


def normalize(color):
    if color.startswith("#"):
        return webcolors.normalize_hex(color)
    return webcolors.name_to_hex(color)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("background")
    parser.add_argument("preferred")
    parser.add_argument("allowed", nargs="+")
    args = parser.parse_args()
    choice = ink(normalize(args.background), normalize(args.preferred),
                 [normalize(c) for c in args.allowed])
    print(choice or "manual review")
