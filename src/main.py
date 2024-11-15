import json
import zipfile
from argparse import ArgumentParser, Namespace

from mapping_validator import assert_mapping
from util import get_files_by_extension, get_subdirs, unzip_at


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
    mappings_filtered = {k: v for k, v in mappings.items() if v is not None}
    proper_zips = get_files_by_extension(input_dir, ".zip")
    recalbox_dirs = get_subdirs(recalbox_dirs_path)

    if not assert_mapping(mappings, proper_zips, recalbox_dirs):
        print("\nPlease fix the errors above and try again.")
        # exit(1)

    for proper_zip, recalbox_dir in mappings_filtered.items():
        unzip_at(
            f"{input_dir}/{proper_zip}",
            "/mnt/d/repos/proper1g1r-to-recalbox/.ignore",
            # f"{recalbox_dirs_path}/{proper_zip}"
        )


if __name__ == "__main__":
    main()
