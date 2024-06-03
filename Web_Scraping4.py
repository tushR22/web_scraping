#Import the required libraries
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import re

#Configuring the webdriver as per requirement
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

#Send a GET HTTP request to the domain
driver.get('https://cetcell.mahacet.org/search-institute')
driver.maximize_window()
driver.implicitly_wait(50)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight,)") #Scroll down to the end
#driver.find_elements
time.sleep(20) #Wait so that the webpage is loaded fully

#To click on the search button using the XPath
button = driver.find_element(By.XPATH,'//*[@id="submitbtnresults"]').send_keys(Keys.ENTER) 
time.sleep(20)

#To parse the content received from the server
soup = BeautifulSoup(driver.page_source, 'html.parser')

#Creating an empty list to store the result into
data = []
list_header =[]
header = soup.find_all("table")[0].find('tr')

for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue

HTML_data = soup.find_all("table")[0].find_all('tr')[1:]

for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
        data.append(sub_data)

dataframe = pd.DataFrame(data = data, columns = list_header)

#To convert the data into data frame 
dataframe = pd.DataFrame(data, columns = ['Sr No', 'More Info','College Code','College Name','Course Type','Course Name','Address','Status','District'])

#To convert the dataframe into csv format
dataframe.to_csv('E:/Web Scraping/List of All Colleges.csv',index=False)


#To close the driver and release the resources
driver.close()
