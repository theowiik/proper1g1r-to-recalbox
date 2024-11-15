import os
import zipfile


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


def unzip_at(zip_path: str, output_dir: str) -> None:
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        files = zip_ref.namelist()
        total_files = len(files)

        if total_files == 0:
            print("❌ The ZIP archive is empty.")
            return

        for index, file in enumerate(files, start=1):
            zip_ref.extract(file, output_dir)
            print(f"📂 Extracted: {file} ({index}/{total_files})")

        print(f"✅ Completed extraction of {zip_path} to {output_dir}")
