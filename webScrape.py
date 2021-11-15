import os
import selenium
from selenium import webdriver
import time
#from PIL import Image
import io
#import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import urllib

#Install Driver
driver = webdriver.Chrome(ChromeDriverManager().install())

#Specify Search URL 
search_url="""https://www.starwars.com/databank/"""

driver.get(search_url)

driver.find_elements_by_xpath("""//*[@id="ref-1-6"]/div[1]/div[2]/ul/li[2]/span""")[0].click()

i=0
exit = 0
if not os.path.exists('sw_char'):
	os.mkdir('sw_char')
while True:
	time.sleep(1.5)

	try:
		element = WebDriverWait(driver, 5).until(
			EC.element_to_be_clickable((By.XPATH, """/html/body/div[5]/div[1]/div[2]/div[2]/article/section[7]/div[1]/div[4]/div/a/span[1]""")))

		more = driver.find_elements_by_xpath("""/html/body/div[5]/div[1]/div[2]/div[2]/article/section[7]/div[1]/div[4]/div/a/span[1]""")
		more[0].click()
	except:
		exit = exit + 1

	i=i+1

	if (exit>=10):
		break
	print(i)
print("images")
for x in range(1, 836):
	try:
		char = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/article/section[7]/div[1]/div[3]/div/ul[2]/div[" + str(x) + "]/div/div/div/div/div[2]/div[2]/div/h3/a/span")
		
		for element in char:
			char_name = element.text
			print(char_name)

		char_img = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/article/section[7]/div[1]/div[3]/div/ul[2]/div[" + str(x) + "]/div/div/div/div/div[1]/div/a/img")
		for img in char_img:
			src = img.get_attribute('src')

			# download the image
			urllib.request.urlretrieve(src, "sw_char/" + char_name + ".png")
	except:
		print("f")

totalFiles=0
for base, dirs, files in os.walk("sw_char"):
    for Files in files:
        totalFiles += 1
print(totalFiles)