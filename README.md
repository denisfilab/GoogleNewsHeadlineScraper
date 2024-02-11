# Google News Headline Scraper

This Python script scrapes news headlines from Google News for a specific search term, from a specified start date to the current date. The scraped data includes the date of the news, headline, sub-headline, URL, and the news company. The data is saved to a CSV file.

## Requirements

- Python 3
- Selenium
- Pandas
- Scrapy

## Usage

1. Install the required Python packages:

    ```bash
    pip install selenium pandas scrapy
    ```

2. Download the appropriate [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for your system and place it in the same directory as the script.

3. Run the script with a search term and a start date (in MM/DD/YYYY format):

    ```bash
    python news_headline_bot.py 'Tesla' '02/09/2017'
    ```

    This will scrape news headlines for "Tesla" from February 9, 2017 to the current date.

## Notes
Please note that web scraping is against Google's Terms of Service. This script is for educational purposes only. Use it responsibly and respect Google's robots.txt file.
