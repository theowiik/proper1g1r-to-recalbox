import json
from argparse import ArgumentParser, Namespace
from pathlib import Path

from mapping_validator import assert_mapping
from util import get_files_by_extension, get_subdirs, rename_dir, unzip_at


def get_mappings() -> dict[str, str]:
    with open("mappings.json") as f:
        return json.load(f)


def get_args() -> Namespace:
    argparser = ArgumentParser()
    argparser.add_argument("input_dir", help="Input directory")
    argparser.add_argument("output_dir", help="Output directory")

    return argparser.parse_args()


def main() -> None:
    # args = get_args()
    # input_dir = args.input_dir

    input_dir = Path(
        "/mnt/e/Downloads/proper1g1r-collection/ROMs"
    )  # TODO: remove input_dir
    output_dir = Path("/mnt/d/repos/proper1g1r-to-recalbox/.ignore/roms")
    recalbox_dirs_path = Path("recalbox_rom_directory")

    mappings = get_mappings()
    mappings_filtered = {
        k: v for k, v in mappings.items() if v is not None and v == "gb"
    }
    proper_zips = get_files_by_extension(input_dir, ".zip")
    recalbox_dirs = get_subdirs(recalbox_dirs_path)

    if not assert_mapping(mappings, proper_zips, recalbox_dirs):
        print("\nPlease fix the errors above and try again.")
        # exit(1)

    for proper_zip, recalbox_dir in mappings_filtered.items():
        proper_path = Path(proper_zip)

        unzip_at(input_dir / proper_path, output_dir)
        rename_dir((output_dir / proper_path).with_suffix(""), recalbox_dir)


if __name__ == "__main__":
    main()
