import csv
import os
import pprint
from argparse import ArgumentParser, Namespace


def get_mappings() -> dict[str, str]:
    with open("data.csv") as f:
        reader = csv.reader(f)
        return {row[0]: row[1] for row in reader}


def get_proper_zips(directory: str) -> list[str]:
    proper_directories = []

    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".zip"):
            proper_directories.append(filename)

    return proper_directories


def get_subdirs(directory: str) -> list[str]:
    subdirs = []

    for filename in sorted(os.listdir(directory)):
        if os.path.isdir(os.path.join(directory, filename)):
            subdirs.append(filename)

    return subdirs


def get_args() -> Namespace:
    argparser = ArgumentParser()
    argparser.add_argument("input_dir", help="Input directory")

    return argparser.parse_args()


def main() -> None:
    # args = get_args()
    # input_dir = args.input_dir
    input_dir = "/mnt/e/Downloads/proper1g1r-collection/ROMs"  # TODO: remove
    recalbox_dirs_path = "recalbox_rom_directory"

    mappings = get_mappings()
    proper_dirs = get_proper_zips(input_dir)
    recalbox_dirs = get_subdirs(recalbox_dirs_path)

    # pprint.pprint(proper_dirs)
    pprint.pprint(recalbox_dirs)


if __name__ == "__main__":
    main()
