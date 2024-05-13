# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import ActionChains
# from fake_useragent import UserAgent
# import time
# import undetected_chromedriver as uc

# URL = 'https://www.autoscout24.ch/de'

# options = uc.ChromeOptions()
# options.headless = False
# ua = UserAgent()
# user_agent = ua.random

# options.add_argument(f'--user-agent={user_agent}')
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-gpu")

# driver = uc.Chrome(options=options)
# actions = ActionChains(driver)
# driver.get(URL)

# time.sleep(5)

# driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
# click_captcha = driver.find_element(By.XPATH, '//*[@id="challenge-stage"]/div/label/input')
# click_captcha.click()
# driver.switch_to.default_content()

# time.sleep(10)

# driver.quit()



from seleniumbase import BaseCase
import time

class MyTestClass(BaseCase):

    def test_autoscout_captcha(self):
        self.open('https://www.autoscout24.ch/de')
        self.wait_for_tag('iframe')
        self.switch_to_frame('iframe')
        self.click('//*[@id="challenge-stage"]/div/label/input')
        self.switch_to_default_content()
        time.sleep(10)
