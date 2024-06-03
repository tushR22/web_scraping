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
table = soup.find('table',class_= 'CetResults')
#print(table)
#print(type(table))
#tables = soup.find_all('table', class_ = "CetResults" )
#print(i)
with open("E:/Output.html" , "w" , encoding='utf-8') as file:
    file.write(str(table.prettify()))
#To search for table headers tags 
#table1 = soup.find('table' ,'th', class_= 'CetResults')
#print(table1)
#print(column_titles)
#print(headers)
#print(pretty)
#with open("E:/Output.html","r") as file:
#    html = file.read()
#path = "E:/Output.html"
#data = []
#list_header =[]
#soup2 = BeautifulSoup(open(path),'html.parser')
#header = soup2.find_all("table")[0].find('tr')

#for items in header:
#    try:
#        list_header.append(items.get_text)
#    except:
#        continue

#HTML_data = soup2.find_all("table")[0].find_all('tr')[1:]

#for element in HTML_data:
#    sub_data = []
#    for sub_element in element:
#        try:
#            sub_data.append(sub_element.get_text)
#        except:
#            continue
#        data.append(sub_data)

#dataframe = pd.DataFrame(data = data, columns = list_header)
#dataframe.to_csv("")
#soup2 = BeautifulSoup(html,'html.parser')
#table_data = soup2.find('table')
#rows = table_data.find_all('tr')
#data = []
#for row in rows:
#    columns = row.find_all('td')
#    data.append([column.text for column in columns])
#print(type(data))
#data = [re.sub(r"\n",'',row) for row in data]
#    link = columns[0].find('a')['href']

#To create a dataframe and enter data in it 

#for row in table.select('CetResults tr'):
#    sr_no = table.find_all('tr/td').get_text()
#    print(sr_no)
#    more_info = table.find('td').find("a href").get_href()
#    college_code = table.find('td', class_= "alternate").get_text()
#    college_name = table.find('td', class_= "alternate").get_text()
#    course_type = table.find('td', class_="alternate").get_text()
#    course_name = table.find('td', class_="alternate").get_text()
#    address = table.find('td', class_="alternate").get_text()
#    status = table.find('td', class_="alternate").get_text()
#    district = table.find('td', class_="alternate").get_text()
#    data.append([sr_no,more_info,college_code,college_name,course_type,course_name,address,status,district])
#for row in table1.find_all('tr'):
#    cols = row.find_all('td')
#    if len(cols) == 0:
#        cols = row.find_all('th')    
#    cols = [element.text.strip() for element in cols]
#    data.append([ele for ele in cols if ele])
#print(data)
    #course_type = table1.find('td', class_="alternate").get_text()


#dataframe = pd.DataFrame(data, columns = ['Sr No', 'More Info','College Code','College Name','Course Type','Course Name','Address','Status','District'])
#dataframe.to_csv('E:/Web Scraping/List of All Colleges.csv',index=False)


#Adding a delay so as not to overwhelm the server with many simultaneous requests
#time.sleep(10)
#print(College_List)
#print(df)

#To save the data in the CSV file format
#College_List.to_csv('E:/Web Scraping/List of All Colleges.csv', index=False)

#College_List2 = pd.read_csv('List of All Colleges.csv')

#To release the resources acquired by the driver
driver.close()