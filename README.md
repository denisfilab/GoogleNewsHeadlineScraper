# Google News Headline Scraper

This Python script scrapes news headlines from Google News for a specific search term, from a specified start date to an end date. The scraped data includes the date of the news, headline, sub-headline, URL, company, and the date when the data was scraped. The data is saved to a CSV file.

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

3. Run the script with a search term, a start date, and an end date (in MM/DD/YYYY format):

    ```bash
    python news_headline_bot.py 'Tesla' '02/09/2017' '02/09/2022'
    ```

    This will scrape news headlines for "Tesla" from February 9, 2017 to February 9, 2022.

## Notes

- The script sleeps for a random interval between 1 and 3 seconds after each page to avoid being detected as a bot.
- The script appends the data from each page to the same CSV file.
- The script prints the time used after it stops.
- Please note that web scraping is against Google's Terms of Service. This script is for educational purposes only. Use it responsibly and respect Google's robots.txt file.
