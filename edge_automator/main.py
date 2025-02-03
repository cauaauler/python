from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from faker import Faker
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
import time

# Initialize Faker for Portuguese data
fake = Faker("pt_BR")

# Specify the path to your msedgedriver executable
driver_path = r"C:\Users\cauaa\Downloads\edgedriver_win64\msedgedriver.exe"

# Create the EdgeDriver service
service = Service(driver_path)

# Configure Edge options for headless mode and reduce logging
options = Options()
options.use_chromium = True  # Important for Chromium-based Edge
# options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Initialize the Edge WebDriver with the service and options
driver = webdriver.Edge(service=service, options=options)

# Generate a random word
palavra = fake.word()

# Open Google
driver.get("https://www.bing.com/")

# Find the search bar and input the random word
x = 0
while(x < 60):
    time.sleep(10)
    barra_pesquisa = driver.find_element("id", "sb_form_q")
    barra_pesquisa.send_keys(palavra)
    time.sleep(1)
    barra_pesquisa.send_keys(Keys.ENTER)
    x += 1
    break


# Wait for results to load
time.sleep(5)

# Close the browser
# driver.quit()
