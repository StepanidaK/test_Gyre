import unittest
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

class Test_Gyre (unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.set_window_size (1024, 768)


    def test_registered_user(self):
        link = "https://master.gyre.pages.dev"
        self.driver.get(link)

        #registration_btn = self.driver.find_element(By.CSS_SELECTOR, ".page-header__sign-up-btn")

        registration_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".page-header__sign-up-btn")))
        registration_btn.click()

        registration_by_Twitch = self.driver.find_element(By.XPATH, "//a[@class='sign-up-modal__sign-up-with-twitch-button']")
        registration_by_Twitch.click()

        self.assertEqual(self.driver.title, "Войти - Twitch")

        input_name = self.driver.find_element(By.XPATH, '//input[@id="login-username"]')
        input_name.send_keys('test_nida')

        input_password = self.driver.find_element(By.XPATH, '//input[@aria-label="Введите свой пароль"]')
        input_password.send_keys('test_my_twitch_2022')

        input_enter = self.driver.find_element(By.XPATH, '//div[@data-a-target="tw-core-button-label-text"]')
        input_enter.click()

        time.sleep(10)

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


