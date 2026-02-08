from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_test(driver, username_input, password_input, expected_message):
    driver.get("https://the-internet.herokuapp.com/login")

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    username.clear()
    password.clear()

    username.send_keys(username_input)
    password.send_keys(password_input)
    login_btn.click()

    wait = WebDriverWait(driver, 10)
    flash_message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    assert expected_message in flash_message.text


# Setup driver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Positive Test
    login_test(
        driver,
        "tomsmith",
        "SuperSecretPassword!",
        "You logged into a secure area!"
    )
    print("Positive login test passed ✅")

    # Negative Test
    login_test(
        driver,
        "wronguser",
        "wrongpass",
        "Your username is invalid!"
    )
    print("Negative login test passed ✅")

except Exception as e:
    print("Test failed ❌")
    print(e)

finally:
    driver.quit()
