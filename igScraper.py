
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import random



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

def get_followers_names(username, password, target_username):
    service = Service(executable_path="H:\khatranak\insta_scraping\Instagram-Scraping-Followers\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    
    try:
        # Log in to Instagram
        login_to_instagram(driver, username, password)

        # Navigate to the Instagram profile
        base_url = f'https://www.instagram.com/{target_username}/followers'
        driver.get(base_url)

        # Wait for the followers list to be present
        followers_list_locator = (By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(followers_list_locator))

        # Scroll to load more followers
        followers_list = driver.find_element(*followers_list_locator)
        for _ in range(1,10):  # You can adjust the number of scrolls as needed
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_list)
            time.sleep(2)
            # Re-locate the followers list element after each scroll
            followers_list = driver.find_element(*followers_list_locator)

           # Extract followers' names
            # Update the locator to point to the last div element inside the followers list
            random_number = str(random.randint(1, 1000))
            file_path = ('followers'+random_number+random_number+'.csv')
            new_file_path = file_path
            for i in range(1, 110):  # Adjust the range according to your needs
            # Modify the XPath with the iterator
                followers_names_locator = (By.XPATH, f'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{i}]/div/div/div/div[2]')

                # Wait for the element to be present
                WebDriverWait(driver, 20).until(EC.presence_of_element_located(followers_names_locator))

                # Extract followers' names
                followers_names = driver.find_elements(*followers_names_locator)
                names = [follower.text for follower in followers_names]
                # Print or use the names as needed
                print(names)      
                # Generate a random integer between a specified range (inclusive)
                
                # Open the file in 'a' (append) mode
                with open(new_file_path, 'a', newline='',encoding='utf-8') as csvfile:
                    # Create a CSV writer object
                    csv_writer = csv.writer(csvfile)
                    # Write additional data rows
                    csv_writer.writerow(names)


        return names

    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    # Replace 'your_username' and 'your_password' with your actual Instagram credentials
    your_username = 'username'
    your_password = 'password'
    target_username = 'msk_s1991'

    get_followers_names(your_username, your_password, target_username)
  
