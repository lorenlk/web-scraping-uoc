# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv 

#Creation of the empty data list and input of startdate and enddate to scrap
data = []
print('Enter the startdate you want to search (dd/mm/yyy):')
startdatein = input()
print('Enter the enddate you want to search (dd/mm/yyy):')
enddatein = input()

# Creating options to open a headless Chrome instance
chrome_options = Options()  
chrome_options.add_argument("--headless")    

# Web driver of Selenium Chrome to run the instance
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.ign.es/web/ign/portal/sis-catalogo-terremotos")

#Let's search for the Startdate and EndDate in the HTML to fill it 
startdate = driver.find_element_by_id('_IGNSISCatalogoTerremotos_WAR_IGNSISCatalogoTerremotosportlet_startDate')
startdate.clear()
startdate.send_keys(startdatein)

enddate = driver.find_element_by_id('_IGNSISCatalogoTerremotos_WAR_IGNSISCatalogoTerremotosportlet_endDate')
enddate.clear()
enddate.send_keys(enddatein)

#Search of the button to submit the form
python_button = driver.find_element_by_id('enviar') 
python_button.click() 

#Let's create the first soup and extract the header of the table
soup=BeautifulSoup(driver.page_source, 'lxml')
table=soup.find(text="Evento").find_parent("table")

for row in table.findAll("tr"):
    cells = row.findAll('th')
    cells = [ele.text.strip() for ele in cells]
    data.append(cells) 

#Let's create another soup for every page we visit and extract the data of the table
while(True):
    try:
        button2 = driver.find_element_by_link_text('Siguiente')
        next_soup=BeautifulSoup(driver.page_source, 'lxml')
        next_table=next_soup.find(text="Evento").find_parent("table")
        print("Extracting data...")
        for row in next_table.findAll("tr"):
            cells = row.findAll('td')
            cells = [ele.text.strip() for ele in cells]
            data.append(cells)
        button2.click()
    except:
        print("No more pages to scrap")
        break

#Empty values of list are discarded
data = list(filter(None, data))

#Let's create the csv and append all the data
with open('dataset.csv', 'a', newline='',  encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(data)

csvFile.close()

driver.quit()

