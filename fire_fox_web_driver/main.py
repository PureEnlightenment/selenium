from selenium import webdriver
import time

url_asura_scan = 'https://asurascans.com'
url_github = 'https://github.com'
driver = webdriver.Firefox(executable_path='/Users/mac/PycharmProjects/selenium/fire_fox_web_driver/geckodriver')

try:
    driver.get(url=url_asura_scan)
    time.sleep(2)
    driver.get_screenshot_as_file('asura_scan_main.png')
    driver.get(url=url_github)
    driver.refresh()
    time.sleep(2)
    driver.save_screenshot('github.png')
except Exception as ax:
    print(ax)
finally:
    time.sleep(2)
    driver.close()
    driver.quit()
