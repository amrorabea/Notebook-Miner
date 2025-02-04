import csv


def print_counter(name, counter, top_n=10):
    print(f"\nMost Common {name}:")
    for item, count in counter.most_common(top_n):
        print(f"{item}: {count}")


def write_to_csv(filename, data_dict):
    """Write extracted data to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Category", "Item", "Count"])
        for category, counter in data_dict.items():
            for item, count in counter.most_common():
                writer.writerow([category, item, count])
