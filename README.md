# Masstamilan-Downloader

This is a selenium based project to download songs from masstamilan site.

### Steps to follow

#### Download zips
1. Clone the git repository and cd inside the folder in your terminal
2. Run the command `pip install -r requirements.txt`
3. Download the selenium webdriver of your browser and place it in `/usr/local/bin`. You can download it by searching it in google.
4. Open the project in your favourite python supported IDE
5. Go to `https://masstamilan.dev/` and find the music director songs you want to download and click on the name from the music director wise song list option.
6. On clicking, you can find the format they have stored the name in the url 
7. Now copy that music director name from url and place it in `main.py`
8. Specify the download location
9. Now you can run the application and download the songs movie wise. 

#### Extract zips
1. Once all the files are downloaded, open `extract_zips.py` and modify `path_to_zips_folder` and `destination_folder`
2. Then run it, all the zips would be extracted and placed in the destination in proper folder structure


#### Note:
This is a fun project tried with python with the goal of learning selenium with a real life application.
I do not recommend you to download songs this way. You can always opt in subscription services like Spotify, Amazon Music, YouTube Music.

Also this might not work when you are trying, due to HTML changes in masstamilan site (in this case you might have to make some changes in `main.py`),
or the site might have been removed due to copyright infringement.

Made with ❤️ from Madurai by Arjun

**வாழ்க தமிழ்! வளர்க தமிழ்!**



#### References
1. https://selenium-python.readthedocs.io/
2. https://masstamilan.dev/
3. https://sites.google.com/chromium.org/driver/
