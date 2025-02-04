# Hakmar Product Scraper

This project is a Python-based web scraper that retrieves product information from the Hakmar Express API for multiple categories. The script fetches all available pages for each category and saves the collected data into Excel files.

## Features

- Fetches product data from multiple categories.
- Automatically detects the total number of pages for each category.
- Extracts product ID, name, price, and image URL.
- Saves the scraped data into Excel files.
- Implements error handling to manage API changes or failures.

## Requirements

Make sure you have the following Python packages installed:

```bash
pip install requests pandas openpyxl
```

## Usage

1.Clone the repository or copy the script.

2.Run the script using Python:

```bash
python3 main.py
```

The data will be saved in the hakmar_products folder as separate Excel files for each category.

## How It Works

1. The script starts by defining a dictionary of category URLs.
2. It requests the first page of each category to determine the total number of pages.
3. It iterates through all pages, extracting product details.
4. The extracted data is saved into an Excel file.

## Notes

- The script includes a delay between requests to prevent excessive API calls.
- If the API response structure changes, modifications may be required to match the new structure.