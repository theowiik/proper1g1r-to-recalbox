import csv
import os
import pprint
from argparse import ArgumentParser, Namespace

emoji_cross = "❌"


def get_mappings() -> dict[str, str]:
    with open("data.csv") as f:
        reader = csv.reader(f)
        return {row[0]: row[1] for row in reader}


def get_files_by_extension(directory: str, extension: str) -> set[str]:
    proper_directories = []

    for filename in sorted(os.listdir(directory)):
        if filename.lower().endswith(extension.lower()):
            proper_directories.append(filename)

    return set(proper_directories)


def get_subdirs(directory: str) -> set[str]:
    subdirs = []

    for filename in sorted(os.listdir(directory)):
        if os.path.isdir(os.path.join(directory, filename)):
            subdirs.append(filename)

    return set(subdirs)


def get_args() -> Namespace:
    argparser = ArgumentParser()
    argparser.add_argument("input_dir", help="Input directory")

    return argparser.parse_args()


def assert_is_subset(superset: set[str], subset: set[str]) -> bool:
    """Checks if all elements in the 'subset' set are also in the 'superset' set."""
    if not isinstance(superset, set):
        raise TypeError("The 'superset' argument must be a set.")

    if not isinstance(subset, set):
        raise TypeError("The 'subset' argument must be a set.")

    return subset.issubset(superset)

def assert_valid_keys(mappings: dict[str, str], check_values: set[str]) -> bool:
    """
    Validates that all elements in the 'check_values' set are present as keys in the 'mappings' dictionary.

    Args:
        mappings (dict[str, str]): A dictionary where keys are strings, and values are also strings.
        check_values (set[str]): A set of strings to be checked against the keys in 'mappings'.

    Returns:
        bool: Returns True if all 'check_values' are found as keys in the 'mappings' dictionary, and False otherwise.  If 'check_values' is empty, returns False.

    Prints an error message if 'check_values' is empty.
    """
    if len(check_values) == 0:
        print(f"{emoji_cross} Empty list")
        return False

    valid = True

    for key in check_values:
        if key not in mappings:
            print(f"{emoji_cross} '{key}' is not mapped")
            valid = False

    return valid


def assert_valid_mappings(mappings: dict[str, str], check_values: set[str]) -> bool:
    """
    Validates that all elements in the 'check_values' set are present as values in the 'mappings' dictionary.

    Args:
        mappings (dict[str, str]): A dictionary where keys are strings, and values are also strings.
        check_values (set[str]): A set of strings to be checked against the values in 'mappings'.

    Returns:
        bool: Returns True if all 'check_values' are found as values in the 'mappings' dictionary, and False otherwise. If 'check_values' is empty, returns False.

    Prints an error message if 'check_values' is empty.
    """
    if len(check_values) == 0:
        print(f"{emoji_cross} Empty list")
        return False

    valid = True

    for value in check_values:
        if value not in mappings.values():
            print(f"{emoji_cross} '{value}' is not mapped")
            valid = False

    return valid


def main() -> None:
    # args = get_args()
    # input_dir = args.input_dir
    input_dir = "/mnt/e/Downloads/proper1g1r-collection/ROMs"  # TODO: remove
    recalbox_dirs_path = "recalbox_rom_directory"

    mappings = get_mappings()
    proper_zips = get_files_by_extension(input_dir, ".zip")
    recalbox_dirs = get_subdirs(recalbox_dirs_path)

    # if not assert_is_subset(proper_zips, set(mappings.keys())):
    #     print(f"{emoji_cross} Not all proper zips are mapped")
    #     exit(1)

    # if not assert_is_subset(recalbox_dirs, set(mappings.values())):
    #     print(f"{emoji_cross} Not all recalbox directories are mapped")
    #     exit(1)

    # pprint.pprint(proper_dirs)
    # pprint.pprint(recalbox_dirs)

    if not assert_valid_keys(mappings, proper_zips):
        exit(1)

    if not assert_valid_mappings(mappings, recalbox_dirs):
        exit(1)


if __name__ == "__main__":
    main()
