import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class EbaySearchElements:
    def __init__(self,driver):
        self.driver = driver

        self.search_textbox = "//input[@type = 'text']"
        self.search_button1 = "//input[@type ='submit']"
        self.cell_phones_link = "//span[contains(text(), 'Cell Phones & Smartphones')]"
        self.see_all_link ="//span[@class='x-see-all__container'][1]"
        self.screen_size_filter = "//span[@class='x-overlay-aspect__label' and text()='Screen Size']"
        self.screen_size_option = "//div[@class='x-refine__select__svg']//div//div//span[@class='cbx x-refine__multi-select-cbx']"
        self.price_filter = "//span[normalize-space()='$35.00 to $75.00']"
        self.location_filter= "//div[@id='c2-mainPanel-location']"
        self.location_option = "(//input[@data-value='North America'])[2]"
        self.apply_button = "//button[@class='x-overlay-footer__apply-btn btn btn--primary']"
        self.search_bar ="nkw"
        self.first_result = "h3.s-item__title"


    def enter_search_textbox(self,name):
        self.driver.find_element(By.XPATH, self.search_textbox).send_keys(name)

    def click_submit_button(self):
        submit = self.driver.find_element(By.XPATH, self.search_button1)
        submit.click()

    def click_cell_phones_link(self):
        cell_phones = self.driver.find_element(By.XPATH, self.cell_phones_link)
        cell_phones.click()

    def see_all(self):
         self.driver.find_element(By.XPATH, see_all_link).click()

    def click_screen_size_filter(self):
        self.driver.find_element(By.XPATH, screen_size_filter).click()

    def click_screen_size_option(self):
        self.driver.find_element(By.XPATH, screen_size_option).click()

    def click_price_filter(self):
        self.driver.find_element(By.XPATH, price_filter).click()

    def click_location_filter(self):
        self.driver.find_element(By.XPATH, location_filter).click()

    def click_location_option(self):
        self.driver.find_element(By.XPATH, location_option).click()

    def click_apply_button(self):
        self.driver.find_element(By.XPATH, apply_button).click()

    def select_category_dropdown(self):
        category_dropdown = Select(driver.find_element(By.ID, "gh-cat"))
        category_dropdown.select_by_value("58058")


    def click_search_bar(self,a):
        search_bar = driver.find_element(By.NAME, "nkw")
        search_bar.clear()
        search_bar.send_keys(a)
        search_bar.send_keys(Keys.RETURN)

    def click_search_button2(self):
        search_button2 = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        search_button2.click()

    def get_first_result(self):
        self.driver.find_element(By.CSS_SELECTOR, first_result).click()

