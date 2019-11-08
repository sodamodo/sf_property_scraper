import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver_path = 'C:\\bin\\chromedriver'

url = "https://sfplanninggis.org/pim/?pub=true"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get(url)

inputElement = driver.find_element_by_id("addressInput")


inputElement.send_keys('0012001')
time.sleep(3)
inputElement.send_keys(Keys.ENTER)
time.sleep(3)
inputElement.send_keys(Keys.ENTER)






continue_link = driver.find_element_by_link_text('Assessor Summary')
continue_link.click()



soup=BeautifulSoup(driver.page_source, 'lxml')

mydivs = soup.findAll("div", {"class": "divTableCell"})

print(mydivs)


# searchElement = driver.find_element_by_id("Search-icon").click()
# inputElement.send_keys(Keys.ENTER)
# driver.implicitly_wait(3)

# inputElement.send_keys(Keys.ENTER)