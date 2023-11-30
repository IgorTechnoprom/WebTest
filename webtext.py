import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set the path to your ChromeDriver executable
chromedriver_path = 'C:\\Users\\Public\\Documents\\IgorProject\\Google_test\\Google_test\\chromedriver.exe'

# Load URL data from url.json
with open('url.json', 'r', encoding='utf-8') as json_file:
    url_data = json.load(json_file)

# URL of the webpage
url = url_data['url']

# Initialize ChromeOptions
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)

# Set up the Chrome WebDriver with the specified options
driver = webdriver.Chrome(service=ChromeService(chromedriver_path), options=chrome_options)

try:
    # Open the webpage
    driver.get(url)

    # Find elements by class name 'well-content'
    elements = driver.find_elements(By.CLASS_NAME, 'well-content')

    # Extract the inner HTML of each element and concatenate them
    combined_html = '\n'.join([element.get_attribute('outerHTML') for element in elements])

    # Save the HTML content to a file
    with open('web_text.html', 'w', encoding='utf-8') as file:
        file.write(combined_html)

    print("HTML content saved to 'web_text.html'.")

finally:
    # Close the browser window
    driver.quit()
