import csv


def get_mappings() -> dict[str, str]:
    with open("data.csv") as f:
        reader = csv.reader(f)
        return {row[0]: row[1] for row in reader}


def main() -> None:
    print("Hello, world!")

    mappings = get_mappings()

    print(mappings)


if __name__ == "__main__":
    main()
