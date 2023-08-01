from selenium import webdriver
from selenium.webdriver.common.by import By
url = "https://www.amazon.com/"

# Create a headless browser using Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(options=options)

# Fetch the HTML content of the URL
driver.get(url)

# Get page title
page_title = driver.title
print(f"Page Title: {page_title}")

# Get number of links on the page
links =driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.get_attribute("href"))
# links = driver.find_elements_by_tag_name('a')
num_links = len(links)
print(f"Number of Links: {num_links}")

# # Get number of images on the page
# images = driver.find_elements(By.TAG_NAME, "img")
# num_images = len(images)
# print(f"Number of Images: {num_images}")

# # # Get number of forms on the page
# forms = driver.find_elements(By.TAG_NAME, "form")
# num_forms = len(forms)
# print(f"Number of Forms: {num_forms}")

# Close the browser
driver.quit()
