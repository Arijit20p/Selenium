from selenium import webdriver
from selenium.webdriver.common.by import By
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome ()

driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, value="q")  
print(search_bar) #object
print(search_bar.tag_name) 
print(search_bar.get_attribute('placeholder'))
print(search_bar.size)

button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

date_list = driver.find_elements(By.CSS_SELECTOR,value='.event-widget time')
dates = [item.text for item in date_list]
# print(dates)

name_list = driver.find_elements(By.CSS_SELECTOR,value='.event-widget li a')
names = [item.text for item in name_list]
# print(names)
event = {}

for n in range(len(dates)):
    event[n] = {
        "time": dates[n],
        "name": names[n]
    }
print(event)

# driver.close()
driver.quit()