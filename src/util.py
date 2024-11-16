import os
import zipfile
from pathlib import Path


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


def unzip_at(zip_absolute_path: Path, output_dir: Path) -> None:
    print(f"📦 Extracting {zip_absolute_path} to {output_dir}")

    if not zip_absolute_path.exists():
        print(f"❌ The ZIP archive {zip_absolute_path} does not exist.")

    if not zip_absolute_path.is_absolute():
        print(f"❌ {zip_absolute_path} is not an absolute path.")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with zipfile.ZipFile(zip_absolute_path.absolute(), "r") as zip_ref:
        files = zip_ref.namelist()
        total_files = len(files)

        for index, file in enumerate(files, start=1):
            zip_ref.extract(file, output_dir)
            print(f"📂 ({index}/{total_files}) Extracted: {file}")

        print(f"✅ Completed extraction of {zip_absolute_path} to {output_dir}")


def rename_dir(abs_path: Path, new_name: str) -> None:
    """
    Rename the last directory in the given absolute path.

    Parameters:
        - abs_path (Path): Absolute path of the directory to rename.
        - new_name (str): New name for the last directory.
    """
    print(f"📂➡️📂 Renaming {abs_path} to {new_name}")

    if not abs_path.exists():
        raise FileNotFoundError(f"❌ The directory {abs_path} does not exist.")

    if not abs_path.is_dir():
        raise NotADirectoryError(f"❌ {abs_path} is not a directory.")

    if not abs_path.is_absolute():
        raise ValueError(f"❌ {abs_path} is not an absolute path.")

    abs_path.rename(new_name)
    print(f"✅ Renamed {abs_path} to {new_name}")
