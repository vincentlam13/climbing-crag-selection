# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 17:57:30 2020

@author: vinhe
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import time

url = 'https://www.ukclimbing.com/logbook/books/dorset-1045'

driver = webdriver.Chrome('C:/users/vinhe/code/chromedriver')

driver.implicitly_wait(10)
driver.get(url)
main_title = driver.title[14:]
print(main_title)


# press privacy button
python_button = driver.find_element_by_xpath('//*[@id="consentCookiePopup"]/div/div/div/button')
python_button.click()

# selenium hands page source to Beauitful Soup
soup = BeautifulSoup(driver.page_source, 'lxml')

# find all crag URLS as they all have the same URL format of 'https://www.ukclimbing.com/logbook/crag.php?id={}'
link_list = []
for a in soup.find_all('a', href=True):
    link = a['href']
    if '/logbook/crag.php?id=' in link and '#maps' not in link:
        link_list.append(link)
        
dataframes = []
for a in link_list:
    new_url = 'https://www.ukclimbing.com' + a
    driver.get(new_url)
    time.sleep(1)
    
    cragname = driver.title[14:] # print the title after "UKC Logbook -"
    print(cragname)
    
    try:
        # test if the web page has a table, if not then skip e.g. Lulworth crag
        driver.find_element_by_class_name('datatable_column_name') 
        time.sleep(1.5)
        df = pd.read_html(driver.page_source)[1].iloc[:,2:]
        
        # some crag web pages have a slightly different table html structure, this if statement helps retrieve the useful data
        # guilty crags are: Boulder Ruckle, Hedbury, The Cuttings, Winspit
        if df.empty:
            df = pd.read_html(driver.page_source)[2].iloc[:,2:]
            df['Crag'] = cragname
            print(df)
            dataframes.append(pd.DataFrame(df))
            
        else:
            df['Crag'] = cragname
            print(df)
            dataframes.append(pd.DataFrame(df))
    
    # certain crags are closed and have no tables to scrape, e.g. Lulworth
    except NoSuchElementException:
        print('No table found')
        continue

merged = pd.concat(dataframes)
print(merged)

# export to csv
merged.to_csv(main_title + '.csv', index=False)


