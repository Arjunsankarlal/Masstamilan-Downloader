from selenium import webdriver
from selenium.webdriver.common.by import By
import time

music_director_name = "a.r.rahman"
download_directory = "path/to/your/desination"

site_name = f"https://masstamilan.dev/music/{music_director_name}"
pages = 200  # To accommodate all the films of the director

chromeOptions = webdriver.ChromeOptions()

prefs = {"download.default_directory": download_directory}
chromeOptions.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chromeOptions)
download_count = 1
print(f'Start Time: {time.time()}')
for page in range(1, pages):
    site_page = site_name + f"?page={page}"
    driver.get(site_page)
    elements = driver.find_elements(By.CLASS_NAME, 'a-i')
    for i in elements:
        movie_link = i.find_element(By.TAG_NAME, 'a').get_attribute('href')
        driver.get(movie_link)
        print(f"Page no is {i} and downloading {download_count} movie link is {movie_link}")
        download_links = driver.find_element(By.CLASS_NAME, "dlink.anim")
        driver.get(download_links.get_attribute("href"))
        time.sleep(15)
        driver.back()
        download_count += 1
print(f'End Time: {time.time()}')
