from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import chromedriver_binary
chrome_options = Options()
chrome_options.add_argument('--proxy-server=34.85.50.202:3128')
chrome_options.add_argument(f"--window-size=1920,1080")
chrome_options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
driver=webdriver.Chrome(chromedriver_binary.chromedriver_filename,chrome_options=chrome_options)
driver.get('https://www.youtube.com/')