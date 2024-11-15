def _assert_dict(
    mappings: dict[str, str], check_values: set[str], check_keys: bool = True
) -> bool:
    if not check_values:
        print("❌ Empty list")
        return False

    check_dict = mappings.keys() if check_keys else mappings.values()
    label = "🔑" if check_keys else "📦"
    description = "PropeR" if check_keys else "Recalbox"

    valid = True
    for item in check_values:
        if item in check_dict:
            print(f"{label}✅ {description} '{item}' found")
        else:
            print(f"{label}❌ {description} '{item}' not found")
            valid = False

    return valid


def _has_duplicate_values(data: dict[str, str]) -> bool:
    return len(data) != len(set(data.values()))


def assert_mapping(
    mappings: dict[str, str], proper_zips: set[str], recalbox_dirs: set[str]
) -> bool:
    valid = True

    not_none = {k: v for k, v in mappings.items() if v is not None}
    if _has_duplicate_values(not_none):
        print("❌ Duplicate values\n")
        valid = False

    if not len(proper_zips) == len(mappings):
        print("❌ Length mismatch\n")
        valid = False

    if not _assert_dict(mappings, proper_zips, True):
        valid = False

    if not _assert_dict(mappings, recalbox_dirs, False):
        valid = False

    return valid
