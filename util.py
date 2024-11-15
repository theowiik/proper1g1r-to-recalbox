import os


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


def has_duplicate_values(values: dict[str, str]) -> bool:
    return len(values) != len(set(values.values()))
