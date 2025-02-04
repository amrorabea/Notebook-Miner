# Notebook-Miner

## Project Overview
This is a simple project meant to analyze a kaggle dataset notebooks and extract it's key characteristics

## Requirements
- Python 3.8 or later

#### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file.

### Set up Kaggle API credentials
- Create a Kaggle account if you don't have one
- Go to your Kaggle account settings [Here](https://www.kaggle.com/account)
- Generate an API token
- Place the `kaggle.json` file in:
    - Linux/Max: `~/.kaggle/kaggle.json`
    - Windows: `C:\Users\USERNAME\.kaggle/kaggle.json`

## Project Explanation
### Tree
```
─── src/
    ├── helpers/
    │   ├── __init__.py
    │   ├── config.py
    │   ├── extractor.py
    │   ├── processor.py
    │   ├── regex_patterns.py
    │   ├── standardization.py
    │   └── utils.py
    ├── .env.example
    ├── .gitignore
    ├── analyzer.py
    ├── notebookDownload.py
    └── requirements.txt
├── LICENSE
├── README.md
```
1. `src/` - Main source code directory
2. `helpers/` - Package containing utility modules and helper functions
    - `__init__.py` - Makes the directory a Python package
    - `config.py` - Configuration settings and parameters
    - `extractor.py` - Functions for data extraction
    - `processor.py` - Data processing functionality
    - `regex_patterns.py` - Regular expression patterns for text processing
    - `standardization.py` - Data standardization functions
    - `utils.py` - General utility functions
3. `.env.example` - Template for environment variables
4. `.gitignore` - Specifies which files Git should ignore
5. `analyzer.py` - Main analysis script
6. `notebookDownload.py` - Script for downloading notebooks
7. `requirements.txt` - Lists project dependencies
8. `LICENSE` - Project license information
9. `README.md` - Project documentation and instructions


## Run the notebook downloader script

```bash
$ python notebookDownload.py
```

- this should create a new folder `notebooks` that will save all notebooks downloaded from Kaggle.

## Run the notebooks analyzer

```bash
$ python analyzer.py
```
- this should create a new folder `data` that will contain a csv file `extracted_data.csv` containing all data analyzed from the notebooks.