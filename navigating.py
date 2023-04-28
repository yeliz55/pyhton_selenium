

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

searchInput = driver.find_element(By.NAME, 'q')
time.sleep(1)

searchInput.send_keys('python')
time.sleep(3)

searchInput.send_keys(Keys.ENTER)
time.sleep(5)

result = driver.find_elements(By.CSS_SELECTOR, ".f4.text-normal")
for element in result:
    print(element.text)

    time.sleep(5)

    # Alttaki satirlar butun sayfanin textini getirir
    # result =driver.page_source
    # print(result)
