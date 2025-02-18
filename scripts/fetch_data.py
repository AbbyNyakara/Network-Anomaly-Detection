import requests
import zipfile
import io
import os

data_url = "https://academy.hackthebox.com/storage/modules/292/KDD_dataset.zip"
data_path = "../data/raw"

if not os.path.exists(data_path):
    response = requests.get(url=data_url)
    response.raise_for_status() # if there's an error:
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall(data_path)
else:
    pass