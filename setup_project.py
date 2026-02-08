import os

def create_selenium_structure():
    # Define the directory structure
    folders = [
        "Selenium/tests",
        "Selenium/pages",
        "Selenium/utils",
        "Selenium/config",
    ]

    # Define the files to be created
    files = [
        "Selenium/tests/test_login.py",
        "Selenium/pages/login_page.py",
        "Selenium/utils/driver_factory.py",
        "Selenium/config/config.py",
        "Selenium/requirements.txt",
        "Selenium/README.md",
        "Selenium/.gitignore",
    ]

    # Create Folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        # Create an __init__.py to make them Python packages
        with open(os.path.join(folder, "__init__.py"), "w") as f:
            pass

    # Create Files
    for file in files:
        with open(file, "w") as f:
            if "requirements.txt" in file:
                f.write("selenium\nwebdriver-manager\npytest")
            elif "README.md" in file:
                f.write("# Selenium UI Automation Basics\nBasic POM implementation.")
    
    print("🚀 Project structure for 'selenium-ui-automation-basics' created!")

if __name__ == "__main__":
    create_selenium_structure()