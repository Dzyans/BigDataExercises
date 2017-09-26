import zipfile as zip
import os
def iterate_dir(path):
    dir = path
    extension = ".zip"
    for item in os.listdir(dir):
        if item.endswith(extension):
            zip.ZipFile.extract(item)