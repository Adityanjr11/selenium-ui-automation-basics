from utils.driver_factory import create_driver
from pages.login_page import LoginPage
from utils.logger import setup_logger

logger = setup_logger()
driver = create_driver()

try:
    logger.info("Browser launched successfully")

    login_page = LoginPage(driver)
    logger.info("Navigating to login page")
    login_page.load()

    # Positive Test
    logger.info("Running positive login test")
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login_page.get_flash_message()
    logger.info("Positive test passed")

    # Negative Test
    logger.info("Running negative login test")
    login_page.login("wronguser", "wrongpass")
    assert "Your username is invalid!" in login_page.get_flash_message()
    logger.info("Negative test passed")

    # Empty Credentials Test
    logger.info("Running empty credentials test")
    login_page.login("", "")
    assert "Your username is invalid!" in login_page.get_flash_message()
    logger.info("Empty credentials test passed")

except Exception as e:
    logger.error(f"Test failed: {e}")

finally:
    logger.info("Closing browser")
    driver.quit()
