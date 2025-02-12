import os
import requests
import zipfile

url = "https://upload.itcollege.ee/~aleksei/random_files_without_extension.zip"

r = requests.get(url)
with open('random_files.zip', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

with zipfile.ZipFile('random_files.zip', "r") as myzip:
        myzip.extractall()


for filename in os.listdir('random_files'):
    with open('random_files/' + filename, "rb") as f:
        signature = f.read(2)
    if signature == b'\xff\xd8':
        os.rename('random_files/' + filename, 'random_files/' + filename + '.jpg')
    else:
        os.remove('random_files/' + filename)


