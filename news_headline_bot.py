import selenium
import datetime
import random
import pandas as pd 
from selenium import webdriver
from scrapy.selector import Selector
import time
from selenium.webdriver.common.by import By



def getNews(term, input_date):
    start_time = time.time()
    df = pd.DataFrame(columns=['date', 'company', 'headline', 'sub_headline', 'url'])

    # get list of dates, format is MM/DD/YYYY
    input_date_format = '%m/%d/%Y'
    start_date = datetime.datetime.strptime(input_date, input_date_format)
    current_time = datetime.datetime.today()
    days_diff = (current_time - start_date).days

    date_list = [(current_time - datetime.timedelta(days=x)).strftime('%m/%d/%Y') for x in range(days_diff+1)]
    date_list.reverse() # start from the oldest date

    driver = webdriver.Chrome('chromedriver.exe')

    # loop through each date
    for date in date_list:
        print(f'Searching for {term} on {date}')

        # sleep time to avoid being detected
        time.sleep(random.randrange(1, 3))

        # set url for searching
        url  = f"https://www.google.com/search?q={term}&tbs=cdr:1,cd_min:{date},cd_max:{date}&tbm=nws&lr=lang_en"

        # open browser
        driver.get(url)


        # check each div
        while True:
            sel = Selector(text=driver.page_source)
            div = sel.xpath('//*[@class="SoaBEf"]')
            for content in div:
                headline = content.xpath('.//div[@class="n0jPhd ynAwRc MBeuO nDgy9d"]/text()').extract()
                sub_headline = content.xpath('.//div[@class="GI74Re nDgy9d"]/text()').extract()
                url = content.xpath('.//div/a[@class="WlydOe"]/@href').extract()
                company = content.xpath('.//div[@class="MgUUmf NUnG9d"]/span/text()').extract()
                df = df._append({'date': date, 'company': company, 'headline': headline, 'sub_headline': sub_headline, 'url': url}, ignore_index=True)
                
            # check if there is a next page
            next_button = driver.find_elements(By.XPATH, "//td[@role='heading']/a[@id='pnnext']")
            if next_button:
                next_button[0].click()
                time.sleep(random.randrange(1, 3))
            else:
                break

        # save the data to a csv file
        df.to_csv(f'{term}_news_headline.csv', mode='a', header=False, index=False)
        df = pd.DataFrame()  # clear the dataframe for the next page

    end_time = time.time()
    print("Time used:", end_time - start_time, "seconds")
    driver.quit()


getNews('Tesla', '02/09/2017')




