import os
import io
import time
import urllib
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Install Driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Navigate to Official Star Wars Databank
search_url = """https://www.starwars.com/databank/"""
driver.get(search_url)

# Filter to characters
driver.find_elements_by_xpath("""//*[@id="ref-1-6"]/div[1]/div[2]/ul/li[2]/span""")[0].click()

i = 0
exit = 0

# Create folder for character images
if not os.path.exists('sw_char'):
    os.mkdir('sw_char')

# Clicks 'Load More' until the option is no longer available.
while True:
    time.sleep(1.5)
    try:
        element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, """/html/body/div[5]/div[1]/div[2]/div[2]/article/section[7]/div[1]/div[4]/div/a/span[1]""")))

        more = driver.find_elements_by_xpath("""/html/body/div[5]/div[1]/div[2]/div[2]/article/section[7]/div[1]/div[4]/div/a/span[1]""")
        more[0].click()
    except:
        # 'Load More' not clickable
        exit = exit + 1
    i = i + 1
    # 'Load More' has failed 10 times so exit the loop
    if (exit >= 10):
        break

# Get the character image and name for each character
# Store image as '<character_name>.png' in the 'sw_char' folder
for x in range(1, 836):
    try:
        char = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/article/section[7]/div[1]/div[3]/div/ul[2]/div[" + str(x) + "]/div/div/div/div/div[2]/div[2]/div/h3/a/span")

        # Get characters name
        for element in char:
            char_name = element.text

        # Get character image
        char_img = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/article/section[7]/div[1]/div[3]/div/ul[2]/div[" + str(x) + "]/div/div/div/div/div[1]/div/a/img")
        for img in char_img:
            src = img.get_attribute('src')
            urllib.request.urlretrieve(src, "sw_char/" + char_name + ".png")
    except:
        pass
