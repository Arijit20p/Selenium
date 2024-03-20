from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome (options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

digit = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# print(digit.text)



artcle_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# print(artcle_count.text)
# artcle_count.click()

# link = driver.find_element(By.LINK_TEXT,value='white-cheeked honeyeater')
# link.click()

link = driver.find_element(By.LINK_TEXT,value="Grant's Canal")
link.click()

#Typing in the search<input name = search>
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python",Keys.ENTER)

# driver.quit()