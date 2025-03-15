from selenium import webdriver

# Make sure the chromedriver.exe is in the same folder as this script
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.ca")