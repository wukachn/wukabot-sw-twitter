import os
import time
import wget
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

FILTER_CHAR_XPATH = """//*[@id="ref-1-20"]/div[1]/div[3]/ul/li[2]/a"""
SHOW_MORE_XPATH = """//*[@id="ref-1-20"]/div[1]/div[5]/div/a/span[1]"""

# Install Driver
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# Navigate to Official Star Wars Databank
search_url = "https://www.starwars.com/databank/"
driver.get(search_url)

# Filter to characters
driver.find_elements(By.XPATH, FILTER_CHAR_XPATH)[0].click()

# Create folder for character images
if not os.path.exists('sw_char'):
    os.mkdir('sw_char')

# Clicks 'Load More' until the option is no longer available.
exit = 0
while True:
    time.sleep(1.5)
    try:
        element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, SHOW_MORE_XPATH)))

        more = driver.find_element("xpath", SHOW_MORE_XPATH)
        more.click()
    except:
        # 'Load More' not clickable
        exit = exit + 1
    # 'Load More' has failed 10 times so exit the loop
    if (exit >= 10):
        break

# Get the character image and name for each character
# Store image as '<character_name>.png' in the 'sw_char' folder
for x in range(1, 1022):
    try:
        char = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/article/section[21]/div[1]/div[4]/div/ul[2]/li[" + str(x) + "]/div/div/div/div/div[2]/div[5]/div/h3/a/span")
        char_name = char.text

        # Get character image
        char_img = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/article/section[21]/div[1]/div[4]/div/ul[2]/li[" + str(x) + "]/div/div/div/div/div[1]/div/a/img")
        src = char_img.get_attribute('src')
        path = "sw_char/" + char_name + ".png"
        wget.download(src, out=path)
    except:
        pass
