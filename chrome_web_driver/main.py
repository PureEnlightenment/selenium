from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

url = 'https://google.com'
ser = Service('/Users/mac/PycharmProjects/selenium/chrome_web_driver/chromedriver')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

try:
    driver.get(url=url)
    time.sleep(2)
    driver.get_screenshot_as_file('1.png')
    driver.get(url='https://stackoverflow.com')
    driver.refresh()
    time.sleep(2)
    driver.save_screenshot('stackoverflow.png')
except Exception as ax:
    print(ax)
finally:
    time.sleep(2)
    driver.close()
    driver.quit()
