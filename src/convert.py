import json
from argparse import ArgumentParser, Namespace

from mapping_validator import assert_mapping
from util import get_files_by_extension, get_subdirs


def get_mappings() -> dict[str, str]:
    with open("mappings.json") as f:
        return json.load(f)


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
    proper_zips = get_files_by_extension(input_dir, ".zip")
    recalbox_dirs = get_subdirs(recalbox_dirs_path)

    if not assert_mapping(mappings, proper_zips, recalbox_dirs):
        print("\nPlease fix the errors above and try again.")
        exit(1)


if __name__ == "__main__":
    main()
