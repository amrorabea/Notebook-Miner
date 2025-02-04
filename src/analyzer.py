# main.py
import os
from helpers import (
    NOTEBOOK_DIR, 
    SAVE_DIR,
    extract_code_cells, 
    process_code, 
    libraries, models, cleaning_techniques, 
    architectures, optimizers, loss_functions, 
    metrics, augmentations
)
from helpers.utils import print_counter, write_to_csv

def main():
    # Check if NOTEBOOK_DIR is set
    if not NOTEBOOK_DIR:
        print("Error: download_path is not set in the .env file.")
        return

    for notebook in os.listdir(NOTEBOOK_DIR):
        if notebook.endswith(".ipynb"):
            nb_path = os.path.join(NOTEBOOK_DIR, notebook)
            try:
                code_cells = extract_code_cells(nb_path)
                for code in code_cells:
                    process_code(code)
            except Exception as e:
                print(f"Failed to process {nb_path}: {e}")
    
    data_to_save = {
        "Libraries": libraries,
        "Models": models,
        "Data Cleaning Techniques": cleaning_techniques,
        "Architectures": architectures,
        "Optimizers": optimizers,
        "Loss Functions": loss_functions,
        "Metrics": metrics,
        "Augmentation Techniques": augmentations,
    }

    csv_filename = os.path.join(SAVE_DIR, "extracted_data.csv")
    write_to_csv(csv_filename, data_to_save)

if __name__ == "__main__":
    main()
