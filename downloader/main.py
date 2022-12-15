from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from time import perf_counter, sleep

music_director_name = "a.r.rahman"
download_directory = "path/to/your/desination"

site_name = f"https://masstamilan.dev/music/{music_director_name}"
pages = 50  # To accommodate all the films of the director

chromeOptions = webdriver.ChromeOptions()

prefs = {"download.default_directory": download_directory}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chromeOptions)
download_count = 1
print(f'Start Time: {datetime.now()}')
st = perf_counter()
for page in range(1, pages):
    try:
        site_page = site_name + f"?page={page}"
        driver.get(site_page)
        elements = driver.find_elements(By.CLASS_NAME, 'a-i')
        movie_link = ""
        for i in elements:
            movie_link = i.find_element(By.TAG_NAME, 'a').get_attribute('href')
            driver.get(movie_link)
            print(f"Page no is {page} and downloading {download_count} movie link is {movie_link}")
            download_links = driver.find_element(By.CLASS_NAME, "dlink.anim")
            driver.get(download_links.get_attribute("href"))
            sleep(15)
            driver.back()
            download_count += 1
    except Exception as e:
        print(
            f"Exception while downloading for page no {page} and downloading {download_count} movie link is {movie_link}", e)
print(f'End Time: {datetime.now()}')
print(f"Total time taken is {perf_counter() - st} secs")
print("Now it is time to unzip things!")
