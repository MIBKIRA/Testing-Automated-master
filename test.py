import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.thesparksfoundationsingapore.org")

    def test_page1_logo(self):
        logo = self.driver.find_element(By.ID, "home")
        self.assertTrue(logo.is_displayed())
    def test_page1_nav_bar(self):
        navbar = self.driver.find_element(By.ID, "link-effect-3")
        self.assertTrue(navbar.is_displayed())

    def test_page1_know_more_button(self):
        know_more_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/a"))
        )
        know_more_button.click()
        expected_url = "https://www.thesparksfoundationsingapore.org/about/vision-mission-and-values/"
        self.assertEqual(self.driver.current_url, expected_url, f"Expected URL: {expected_url} but got {self.driver.current_url}")


    def test_page1_learn_more_button(self):
        learn_more_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/a"))
        )
        learn_more_button.click()
        self.assertEqual(self.driver.current_url, "https://www.thesparksfoundationsingapore.org/join-us/why-join-us/")
        
    def test_page2_about(self):
        about_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[1]/a")
        about_link.click()
        about_us_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[1]/ul/li[4]/a")
        about_us_link.click()
        self.assertEqual(self.driver.current_url, "https://www.thesparksfoundationsingapore.org/about/executive-team/")
    
    def test_page3_policies(self):
        policies_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[2]/a")
        policies_link.click()
        privacy_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[2]/ul/li[1]/a")
        privacy_link.click()
        self.assertEqual(self.driver.current_url, "https://www.thesparksfoundationsingapore.org/policies-and-code/policies/")

    def test_page4_programs(self):
        programs_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[3]/a")
        programs_link.click()
        education_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[3]/ul/li[4]/a")
        education_link.click()
        self.assertEqual(self.driver.current_url, "https://www.thesparksfoundationsingapore.org/programs/workshops/")

    def test_page5_links(self):
        links_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[4]/a")
        links_link.click()
        partners_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[4]/ul/li[1]/a")
        partners_link.click()
        self.assertEqual(self.driver.current_url, "https://www.thesparksfoundationsingapore.org/links/software-and-app/")

    def test_page6_joinUs(self):
        joinUs_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[5]/a")
        joinUs_link.click()
        join_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[5]/ul/li[1]/a")
        join_link.click()
        self.assertEqual(self.driver.current_url, "https://www.thesparksfoundationsingapore.org/join-us/why-join-us/")

    def test_page5_contact(self):
        contact_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[6]/a")
        contact_link.click()
        self.assertEqual(self.driver.current_url, "https://www.thesparksfoundationsingapore.org/contact-us/")
    
    def test_facebook_icon(self):
        facebook_icon = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[1]/a")
        self.assertTrue(facebook_icon.is_displayed())
        current_window = self.driver.current_window_handle
        facebook_icon.click()
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
                self.assertEqual(self.driver.current_url, "https://www.facebook.com/thesparksfoundation.info")
                self.driver.close()
                self.driver.switch_to.window(current_window)
                
    
    def test_twitter_icon(self):
        twitter_icon = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[4]/a")
        self.assertTrue(twitter_icon.is_displayed())
        current_window = self.driver.current_window_handle
        twitter_icon.click()
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
                self.assertEqual(self.driver.current_url, "https://twitter.com/tsfsingapore")
                self.driver.close()
                self.driver.switch_to.window(current_window)

    def test_link_icon(self):
        facebook_icon = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[2]/a")
        self.assertTrue(facebook_icon.is_displayed())
        current_window = self.driver.current_window_handle
        facebook_icon.click()
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
                self.assertEqual(self.driver.current_url, "https://www.facebook.com/thesparksfoundation.info")
                self.driver.close()
                self.driver.switch_to.window(current_window)
                
    
    def test_twitter_icon(self):
        twitter_icon = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[4]/a")
        self.assertTrue(twitter_icon.is_displayed())
        current_window = self.driver.current_window_handle
        twitter_icon.click()
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
                self.assertEqual(self.driver.current_url, "https://twitter.com/tsfsingapore")
                self.driver.close()
                self.driver.switch_to.window(current_window)
    
    def test_instagram_icon(self):
        instagram_icon = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[6]/a")
        self.assertTrue(instagram_icon.is_displayed())
        current_window = self.driver.current_window_handle
        instagram_icon.click()
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
                self.assertEqual(self.driver.current_url, "https://www.instagram.com/thesparksfoundation.info/")
                self.driver.close()
                self.driver.switch_to.window(current_window)

    def test_linkedin_icon(self):
        linkedin_icon = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[2]/a")
        self.assertTrue(linkedin_icon.is_displayed())
        current_window = self.driver.current_window_handle
        linkedin_icon.click()
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
                self.assertEqual(self.driver.current_url, "https://www.linkedin.com/company/the-sparks-foundation/mycompany/")
                self.driver.close()
                self.driver.switch_to.window(current_window)

    def test_medium_icon(self):
        medium_icon = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[3]/a")
        self.assertTrue(medium_icon.is_displayed())
        current_window = self.driver.current_window_handle
        medium_icon.click()
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != current_window:
                self.driver.switch_to.window(window)
                self.assertEqual(self.driver.current_url, "https://medium.com/thesparksfoundation")
                self.driver.close()
                self.driver.switch_to.window(current_window)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='the_reports'))

