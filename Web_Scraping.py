#Import the required libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')

driver = webdriver.Chrome('E:\Web Scraping\chromedriver-win64\chromedriver-win64\chromedriver.exe')

#Send an HTTP GET request to the website 
response = driver.get('https://cetcell.mahacet.org/search-institute')
print("Response received is :" ,response)

#Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.page_source, 'html.parser')
print("Parsed content is: " ,soup)

#pretty = soup.prettify
#print(pretty)

institutes = []
#for row in soup.select('table tbody tr td a'):
#    college_code = row.find("td", class_='alternate').get_text()
#    print(college_code)
    #print(college_code)
    #college_code = row.find('td', class_= 'alternate').find('span').get_text()[1:-1]
    #college_name = row.find('td', class_= 'alternate').find('')
    #course_type = 
    #course_name = 
    #address = 
    #status = 
    #district = 
#institutes.append(college_code)
#print(institutes)
#, college_name, course_type, course_name, address, status, district])

#df = pd.DataFrame(institutes, columns = ['College Code','College Name','Course Code','Course Name','Address','Status','District'])

#time.sleep(1)

#df.to_csv('All Institues.csv', index=False)

