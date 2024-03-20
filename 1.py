from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome (options=chrome_options)
driver.get("https://ew.com/music/best-rock-songs/")

english_songs = driver.find_elements(By.CLASS_NAME, value='mntl-sc-block-heading__text')
# english = [item.text for item in english_songs]
english = []
for item in english_songs:
    english.append(item.text)
    
print(english)


driver.quit()