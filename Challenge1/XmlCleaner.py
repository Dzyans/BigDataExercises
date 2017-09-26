import zipfile as zip
import os
def iterate_dir(path):
    dir = os.path.abspath("")
    extension = ".zip"
    for item in os.listdir(dir):
        if item.endswith(extension):
            zip_file = zip.ZipFile(item, 'r')
            print(os.path.join(dir, item))
            zip_file.extractall(dir+"/out")
            zip_file.close()


iterate_dir("jek")