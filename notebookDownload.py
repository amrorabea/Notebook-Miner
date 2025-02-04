import os
import csv
import subprocess
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Kaggle search parameters
DATASET = "mateuszbuda/lgg-mri-segmentation"
DOWNLOAD_PATH = os.getenv("download_path", "./kaggle_notebooks")

def is_valid_kernel_ref(ref):
    """Check if the kernel reference is valid"""
    return isinstance(ref, str) and '/' in ref and len(ref.split('/')) == 2

# Ensure the download directory exists
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

try:
    kernels_csv_path = os.path.join(DOWNLOAD_PATH, "kernels.csv")
    all_kernels = []
    page = 1
    per_page = 100  # Max is 100 per page

    while True:
        print(f"Fetching page {page} of notebooks...")

        result = subprocess.run(
            ["kaggle", "kernels", "list", "--dataset", DATASET, "--csv", "--page-size", str(per_page), "--page", str(page)],
            capture_output=True,
            text=False
        )

        output = result.stdout.decode("utf-8", errors="replace").strip()

        if not output:
            print("No more data received.")
            break

        with open(kernels_csv_path, "a", encoding="utf-8", errors="ignore") as f:
            f.write(output + "\n")

        rows = output.split("\n")

        if len(rows) <= 1:  # No new kernels found
            break

        reader = csv.reader(rows)
        next(reader, None)  # Skip header
        kernels = [row[0] for row in reader if row and is_valid_kernel_ref(row[0])]

        if not kernels:
            break

        all_kernels.extend(kernels)
        page += 1

        # Kaggle API rate limiting safety
        time.sleep(2)  # Prevent hitting request limits

    if not all_kernels:
        print("No notebooks found for this dataset.")
        exit()

    print(f"Found {len(all_kernels)} notebooks to download.")

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
