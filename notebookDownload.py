import os
import csv
import subprocess
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Kaggle search parameters
DATASET = os.getenv("DATASET_NAME")
DOWNLOAD_PATH = os.getenv("download_path", "./kaggle_notebooks")
SORT_ORDERS = ["hotness", "voteCount", "score"]  # Different sorting orders to maximize results
PER_PAGE = 100  # Max allowed by Kaggle API
MAX_PAGES = 20  # Fetch up to 20 pages per sorting order to get all notebooks

def is_valid_kernel_ref(ref):
    """Check if the kernel reference is valid"""
    return isinstance(ref, str) and '/' in ref and len(ref.split('/')) == 2

# Ensure the download directory exists
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

try:
    kernels_csv_path = os.path.join(DOWNLOAD_PATH, "kernels.csv")
    all_kernels = set()  # Use a set to avoid duplicates

    for sort_by in SORT_ORDERS:
        for page in range(1, MAX_PAGES + 1):
            print(f"Fetching page {page} (sorted by {sort_by})...")

            result = subprocess.run(
                ["kaggle", "kernels", "list", "--dataset", DATASET, "--csv", "--page-size", str(PER_PAGE), "--page", str(page), "--sort-by", sort_by],
                capture_output=True,
                text=False  # Binary mode to prevent encoding issues
            )

            output = result.stdout.decode("utf-8", errors="replace").strip()

            if not output or "No kernels found" in output:
                print(f"No more notebooks found for {sort_by}. Moving to next sorting method.")
                break

            with open(kernels_csv_path, "a", encoding="utf-8", errors='ignore') as f:
                f.write(output + "\n")

            rows = output.split("\n")
            if len(rows) <= 1:
                break

            reader = csv.reader(rows)
            next(reader, None)  # Skip header
            kernels = {row[0] for row in reader if row and is_valid_kernel_ref(row[0])}

            if not kernels:
                break

            all_kernels.update(kernels)

            # Kaggle API rate limiting safety
            time.sleep(2)

    # As a backup, also search by keyword to find missed notebooks
    print("Running additional search for missed notebooks...")
    for page in range(1, MAX_PAGES + 1):
        print(f"Fetching page {page} using search term '{DATASET}'...")

        result = subprocess.run(
            ["kaggle", "kernels", "list", "--search", DATASET, "--csv", "--page-size", str(PER_PAGE), "--page", str(page)],
            capture_output=True,
            text=False
        )

        output = result.stdout.decode("utf-8", errors="replace").strip()

        if not output:
            break

        rows = output.split("\n")
        if len(rows) <= 1:
            break

        reader = csv.reader(rows)
        next(reader, None)  # Skip header
        kernels = {row[0] for row in reader if row and is_valid_kernel_ref(row[0])}

        all_kernels.update(kernels)

        time.sleep(2)

    print(f"Total unique notebooks found: {len(all_kernels)}")

    if not all_kernels:
        print("No notebooks found for this dataset.")
        exit()

    # Download each notebook
    for kernel_ref in all_kernels:
        print(f"Downloading {kernel_ref}...")
        try:
            download_result = subprocess.run(
                ["kaggle", "kernels", "pull", kernel_ref, "-p", DOWNLOAD_PATH],
                capture_output=True,
                text=False
            )

            stderr_output = download_result.stderr.decode("utf-8", errors="replace")

            if download_result.returncode != 0:
                print(f"Error downloading {kernel_ref}")
                print(f"stderr: {stderr_output}")
            else:
                print(f"Successfully downloaded {kernel_ref}")

            # Prevent API rate limit issues
            time.sleep(1)

        except Exception as e:
            print(f"Error downloading {kernel_ref}: {str(e)}")
            continue

    print("Download completed!")

except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
