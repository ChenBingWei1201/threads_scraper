import os
import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ThreadsScraper:
    def __init__(self, username, password, driver_path):
        """
        Initialize the scraper with user credentials, driver path, and user agent.
        """
        self.username = username
        self.password = password
        self.driver_path = driver_path
        self.user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0)"
        self.login_url = "https://www.threads.net/login"
        self.search_url = "https://www.threads.net/search"
        self.class_name = "x1lliihq x1plvlek xryxfnj x1n2onr6 x1ji0vk5 x18bv5gf x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xjohtrz xo1l8bm xp07o12 x1yc453h xat24cr xdj266r"
        self.driver = None

    def get_driver(self):
        """
        Initialize and return the WebDriver instance.
        """
        options = Options()
        options.headless = True
        options.add_argument(f"user-agent={self.user_agent}")
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)

    def login_to_threads(self):
        """
        Log into Threads using provided credentials.
        """
        self.driver.get(self.login_url)
        try:
            # Wait for username field and enter credentials
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
            )
            username_field.send_keys(self.username)

            # Find and fill password field
            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
            )
            password_field.send_keys(self.password)

            # Click login button
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[text()='Log in']"))
            )
            submit_button.click()

            time.sleep(5)  # Wait for the login process to complete
            return True
        except Exception as e:
            print(f"Login failed: {e}")
            return False

    def scrape(self, keywords, scroll_times=5):
        """
        Scrape posts for the given keywords and return results.
        """
        all_data = []
        for keyword in keywords:
            print(f"Scraping keyword: {keyword}")
            search_url = f"{self.search_url}?q={keyword}&serp_type=default"
            self.driver.get(search_url)

            try:
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, f"//span[@class='{self.class_name}']"))
                )

                for _ in range(scroll_times): # Scroll and load content
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(random.uniform(2, 5))

                elements = self.driver.find_elements(By.XPATH, f"//span[@class='{self.class_name}']")
                posts = [elem.text.strip() for elem in elements]
                all_data.append({"keyword": keyword, "posts": posts})
            except Exception as e:
                print(f"Error scraping keyword '{keyword}': {e}")
        return all_data

    def save_to_csv(self, data, filename, csv_index=False):
        """
        Save scraped data to a CSV file.
        """
        rows = [{"keyword": row["keyword"], "post": post} for row in data for post in row["posts"]]
        df = pd.DataFrame(rows)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        df.to_csv(filename, index=csv_index)

    def close(self):
        """
        Close the WebDriver.
        """
        if self.driver:
            self.driver.quit()
