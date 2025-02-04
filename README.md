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