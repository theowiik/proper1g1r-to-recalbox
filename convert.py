import json
from argparse import ArgumentParser, Namespace

from util import get_files_by_extension, get_subdirs, has_duplicate_values


def get_mappings() -> dict[str, str]:
    with open("mappings.json") as f:
        return json.load(f)


def get_args() -> Namespace:
    argparser = ArgumentParser()
    argparser.add_argument("input_dir", help="Input directory")

    return argparser.parse_args()


def assert_valid_mapping(
    mappings: dict[str, str], check_values: set[str], check_keys: bool = True
) -> bool:
    if len(check_values) == 0:
        print("❌ Empty list")
        return False

    valid = True
    check_dict = mappings.keys() if check_keys else mappings.values()

    for item in check_values:
        if item not in check_dict:
            msg = (
                f"🔑 PropeR '{item}' is not a key"
                if check_keys
                else f"📦 Recalbox '{item}' is not a value"
            )
            print(msg)
            valid = False

    return valid


def valid_pair(proper: str, recalbox: str) -> bool:
    # TODO: check if both exists
    return True


def main() -> None:
    # args = get_args()
    # input_dir = args.input_dir
    input_dir = "/mnt/e/Downloads/proper1g1r-collection/ROMs"  # TODO: remove
    recalbox_dirs_path = "recalbox_rom_directory"

    mappings = get_mappings()
    proper_zips = get_files_by_extension(input_dir, ".zip")
    recalbox_dirs = get_subdirs(recalbox_dirs_path)

    valid = True

    if has_duplicate_values(mappings):
        print("❌ Duplicate values")
        valid = False

    if not len(proper_zips) == len(mappings):
        print("❌ Length mismatch")
        valid = False

    if not assert_valid_mapping(mappings, proper_zips, True):
        valid = False

    if not assert_valid_mapping(mappings, recalbox_dirs, False):
        valid = False

    if not valid:
        print("\nPlease fix the errors above and try again.")
        exit(1)


if __name__ == "__main__":
    main()
