import zipfile
import os
from tqdm import tqdm

path_to_zips_folder = "/path/to/zips/downloaded"
destination_folder = "/path/to/extract/zips"

for file in tqdm(os.listdir(path_to_zips_folder)):
    filename = path_to_zips_folder + "/" + file;
    if filename.__contains__(".zip"):
        try:
            with zipfile.ZipFile(filename, 'r') as zip_ref:
                folder_name = file.split("-320")[0]
                zip_ref.extractall(destination_folder + "/" + folder_name)
        except Exception as e:
            print(f"Exception while unzipping {filename}", e)
print("Done and Dusted!!")
print("Before deleting the zips make sure all the folders are extracted, once")