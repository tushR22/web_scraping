#Import the required libraries
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

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
#xpath - '//button[text()="Info Toko"]'
#css selector - #submitbtnresults
#button = driver.find_element(By.CLASS_NAME,'submitbtn')
#driver.execute_script("arguments[0].click();", button)
#button.submit()

#To parse the content received from the server
soup = BeautifulSoup(driver.page_source, 'html.parser')
#pretty = soup.prettify()
#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.presence_of_element_located((By.ID, 'dynamic-element')))

#To find the table class, here it is CetResults
table = soup.find_element(By.CSS_SELECTOR,'#SearchResultsShow > table > tbody > tr:nth-child(2)')
print(table)

#tables = soup.find_all('table', class_ = "CetResults" )
#print(i)

#To search for table headers tags 
#table1 = soup.find('table' ,'th', class_= 'CetResults')
#print(table1)
#print(column_titles)
#print(headers)
#print(pretty)

#To create a dataframe and enter data in it 
#data =[]
#rows = 1+len(driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div/div/div/div/div/div[2]/table/tbody/tr[2]"))
#cols = len(driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div/div/div/div/div/div[2]/table/tbody/tr[2]/td"))

#for r in range(rows):
#    for s in range(cols):
#        value = driver.find_element(By.XPATH,"/html/body/div[1]/div/section/div/div/div/div/div/div[2]/table/tbody/tr["+str(r)+"]/td["+str(s)+"]").text
#        print(value, end='')
#    print()
#for row in table.select('table CetResults tr'):
#    sr_no = row.find('tr/td[1]', class_name = "alternate").get_text()
#    more_info = row.find('td').find("a href").get_href()
#    college_code = row.find('td', class_= "alternate").get_text()
##    college_name = row.find('td', class_= "alternate").get_text()
 #   course_type = row.find('td', class_="alternate").get_text()
 #   course_name = row.find('td', class_="alternate").get_text()
 #   address = row.find('td', class_="alternate").get_text()
 #   status = row.find('td', class_="alternate").get_text()
 #   district = row.find('td', class_="alternate").get_text()
 #   data.append([sr_no,more_info,college_code,college_name,course_type,course_name,address,status,district])
#for row in table1.find_all('tr'):
#    cols = row.find_all('td')
#    if len(cols) == 0:
#        cols = row.find_all('th')    
#    cols = [element.text.strip() for element in cols]
#    data.append([ele for ele in cols if ele])
#print(data)
    #course_type = table1.find('td', class_="alternate").get_text()

#College_List = pd.DataFrame(data, columns = ['Sr No', 'More Info','College Code','College Name','Course Type','Course Name','Address','Status','District'])
#Adding a delay so as not to overwhelm the server with many simultaneous requests
#time.sleep(10)
#print(College_List)
#print(df)

#To save the data in the CSV file format
#College_List.to_csv('E:/Web Scraping/List of All Colleges.csv', index=False)

#College_List2 = pd.read_csv('List of All Colleges.csv')

#To release the resources acquired by the driver
driver.close()