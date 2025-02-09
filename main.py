from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time


class WorldBrain:
    def __init__(self, driver_path=None):
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=BlockCredentialedSubresources")
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
        self.wait = WebDriverWait(self.driver, 10)

    def add_cookies(self, cookies):
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def open_blog(self, url):
        self.driver.get(url)
        cookies = [
            {
                "name": "_help_center_session",
                "value": "b2cycEtPY1Zxd3JDSTVkRy9BVGFOMzVkT2I1YnIyUXpkZ0Z2S2UzbWpRSnphNVdLRjZlcFc0cENpQ1c0d0hvU3Axb3FIVzRvL2phb3RPNXpFYjNBNzMzdWFXSjlhaSs5T0lWcTBFU3l3ODdOa3UzTXZ6aDdyMllURWMydHNjYXpqbGk1YjVaa3dXVHRVYjJqRHpERkZva05Ta0tYQW9BWmNaTE1DSXM1TGs0ZUplQTZUTFVNSzJzWnQ3MTVXdGdhMmdReHhKSVpFMUErMXZwSWYxR3VrUT09LS1FZmZUT0pMd05xcG9lWGtPMC9PTjlRPT0%3D--8f43ff7bc464dfd0ccb89cf0792e0ff0b615895e",
                "path": "/",
                "secure": True,
                "httpOnly": True,
            },
        ]
        self.add_cookies(cookies)
        self.driver.refresh()
        print("Browser is running. Press Enter to continue...")
        input()

    def click_all_vote_buttons(self):
        try:
            self.wait.until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "like-btn"))
            )
            vote_buttons = self.driver.find_elements(By.CLASS_NAME, "like-btn")
            print(f"Founded {len(vote_buttons)} comments.")
            breakpoint()
            for index, button in enumerate(vote_buttons):
                try:
                    self.driver.execute_script(
                        "arguments[0].scrollIntoView(true);", button
                    )
                    time.sleep(0.5)
                    button.click()
                    print(f"Clicked into comment {index + 1}.")
                except Exception as e:
                    print(f"Error when click {index + 1}: {e}")
        except TimeoutException:
            print("This blog hasn't comment.")

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    blog_url = "https://support.worldquantbrain.com/hc/en-us/community/posts/29234887416727--L%C3%BD-gi%E1%BA%A3i-v%E1%BB%81-c%C3%A1c-ti%C3%AAu-ch%C3%AD-c%E1%BB%A7a-Genius"
    world_brain = WorldBrain()
    try:
        world_brain.open_blog(blog_url)
        while True:
            print("Options:")
            print("1. Vote all comment")
            print("2. Exit")
            choice = input("Enter your choose (1/2): ").strip()

            if choice == "1":
                world_brain.click_all_vote_buttons()
            elif choice == "2":
                print("Exit...")
                break
            else:
                print("Select is bad. Please choose again.")
    finally:
        world_brain.close()
