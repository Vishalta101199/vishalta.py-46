from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# --- Configuration ---
url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"

# --- Start the browser ---
driver = webdriver.Chrome()  
driver.get(url)

# --- Cookies before login ---
cookies_before = driver.get_cookies()
print("Cookies before login:", cookies_before)

# --- Login ---
driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "login-button").click()
sleep(2)  # Allow time for login and potential cookie setting

# --- Cookies after login ---
cookies_after = driver.get_cookies()
print("Cookies after login:", cookies_after)

# --- Verify cookie generation ---
if len(cookies_after) > len(cookies_before):
    print("New cookies were generated during login.")
else:
    print("No new cookies detected after login.")

# --- Logout ---
driver.find_element(By.ID, "react-burger-menu-btn").click()
sleep(1) 
driver.find_element(By.ID, "logout_sidebar_link").click()
sleep(2)

# --- Close the browser ---
driver.quit()