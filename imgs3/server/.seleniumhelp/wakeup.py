import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.keys import Keys
import chromedriver_binary
chrome_options = Options()
# chrome_options.add_argument('--proxy-server=176.212.112.45:3128')
chrome_options.add_argument(f"--window-size=1400,800")
# chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_extension('crx.crx')
chrome_options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
driver=webdriver.Chrome(chromedriver_binary.chromedriver_filename,chrome_options=chrome_options)
driver.get('https://youtu.be/Z0h4vCRWu1E?t=45')
# driver.save_screenshot('maibmob.png')


time.sleep(1800)
try:
	driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/div[2]').click()
except:
	try:
		driver.find_element_by_xpath('//*[@id="player-container-outer"]').click()
	except:
		driver.find_element_by_xpath('//*[@id="text"]').click()
	
driver.find_element_by_xpath('//*[@id="movie_player"]/div[1]/video').send_keys(Keys.SPACE)
# elem.send_keys()

# import smtplib, ssl

# port = 465  # For SSL


# # Create a secure SSL context
# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.yandex.ru", port, context=context) as server:
#     server.login("info@nadiozimova.ru", 'Nadi2020')
#     server.sendmail('info@nadiozimova.ru', 'ozerow.vlad2018@yandex.ru', 'From: НАДЕЖДА ОЗИМОВА\r\nTo:\r\n\r\nРезультаты теста')
#     server.quit()
#     print(dir(server))