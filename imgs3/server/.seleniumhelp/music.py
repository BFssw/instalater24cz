import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.keys import Keys
import chromedriver_binary
chrome_options = Options()
chrome_options.add_argument(f"--window-size=1920,1080")
chrome_options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
driver=webdriver.Chrome(chromedriver_binary.chromedriver_filename,chrome_options=chrome_options)
driver.get('https://www.y2mate.com/download-youtube/hMW8r8-zg6o')





for i in range(2,57):
    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('//*[@id="txt-url"]'))
    driver.find_element_by_xpath('//*[@id="txt-url"]').clear()
    driver.find_element_by_xpath('//*[@id="txt-url"]').send_keys(f"https://www.youtube.com/watch?v=hMW8r8-zg6o&list=PLlpYO169CEL6ERGtXtJxfR8FF8-vIgZ0p&index={i}")
    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('//*[@id="btn-submit"]'))
    driver.find_element_by_xpath('//*[@id="btn-submit"]').click()
    time.sleep(2)
    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('//*[@id="result"]/div/div[2]/ul/li[2]/a'))
    driver.find_element_by_xpath('//*[@id="result"]/div/div[2]/ul/li[2]/a').click()
    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('//*[@id="process_mp3_a"]'))
    driver.find_element_by_xpath('//*[@id="process_mp3_a"]').click()
    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('//*[@id="process-result"]/div/a'))
    driver.find_element_by_xpath('//*[@id="process-result"]/div/a').click()
    
    
    




time.sleep(5)
try:
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/div[2]').click()
except:
    try:
        driver.find_element_by_xpath('//*[@id="player-container-outer"]').click()
    except:
        driver.find_element_by_xpath('//*[@id="text"]').click()
    