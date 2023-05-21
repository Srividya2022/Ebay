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
import time
import unittest
from srividya.PageObjects.ebaysearch_elements import EbaySearchElements

class AccessPrdCategory(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        # Navigate to eBay.com
        cls.driver.get("https://www.ebay.com")
        print("Application launched successfully")
        cls.driver.maximize_window()

#       Scenario 1: Access a Product via category after applying multiple filters
    def access_prd_category(self):
        driver = self.driver
        prd_category = EbaySearchElements(driver)
        # Find the search box and enter "electronics"
        a  ="electronics"
        prd_category.enter_search_textbox("electronics")
        prd_category.click_submit_button()
        # Wait for the page to load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//span[normalize-space()='Cell Phones, Smart Watches & Accessories'])[1]")))
        prd_category.cell_phones_link()
        # Click on "See All" under "Shop by brand"
        prd_category.see_all_link()
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class ='x-overlay-sub-panel__aspect-options-list']")))
        prd_category.click_screen_size_filter()
        time.sleep(2)
        prd_category.click_screen_size_filter()
        prd_category.screen_size_option()
        prd_category.click_price_filter()
        prd_category.click_location_filter()
        prd_category.click_location_option()
        prd_category.click_apply_button()

        # Verify that filter tags are applied
        filter_tags = driver.find_elements(By.CSS_SELECTOR, ".x-refine__value")
        assert len(filter_tags) == 3, "Expected 3 filter tags, but found {}.".format(len(filter_tags))
        assert "4.0 - 4.4 in" in [tag.text for tag in filter_tags], "Screen size filter tag not found."
        assert "$35.00 to $75.00" in [tag.text for tag in filter_tags], "Price filter tag not found."
        assert "North America" in [tag.text for tag in filter_tags], "Item location filter tag not found."

#Scenario 2: Access a Product via Search
        driver = self.driver
        prd_search = EbaySearchElements(driver)
        prd_search.select_category_dropdown()
        prd_search.click_search_bar("MacBook")
        prd_search.click_search_button2()
        prd_search.select_category_dropdown()
        # Wait for the page to load completely
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "srp-river-results")))
        prd_search.get_first_result()
        prd_search.first_result_name = prd_search.first_result.text
        # Verify that the first result name matches with the search string
        assert "MacBook" in prd_search.first_result_name

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

