from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_instagram(driver, username, password):
    driver.get("https://www.instagram.com/accounts/login/")

    # Wait for the login page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    # Fill in the username and password fields and submit
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Wait for the login to complete
    WebDriverWait(driver, 10).until(EC.url_changes("https://www.instagram.com/accounts/login/"))

if __name__ == "__main__":
    # List of usernames and corresponding passwords
    credentials_list = [
        {'username': 'user1', 'password': 'pass1'},
        {'username': 'trek_nerd_kutub', 'password': 'Killeriam@123'},
        # Add more username/password combinations as needed
    ]

    service = Service(executable_path="H:\khatranak\insta_scraping\Instagram-Scraping-Followers\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        for credentials in credentials_list:
            username = credentials['username']
            password = credentials['password']

            try:
                login_to_instagram(driver, username, password)
                print(f"Login successful for {username}!")

                # You can add additional actions or navigate to other pages here
                # ...

            except Exception as e:
                print(f"Login failed for {username}: {str(e)}")

    finally:
        # Close the browser window
        driver.quit()
