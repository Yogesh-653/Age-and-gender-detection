import requests
import pandas as pd
import shutil

path = "D:/Face/image/image"

dataset = pd.read_csv('D:/Face/FER/Face_Recognition.csv')

urls = [url for url in dataset['content'] if str(url) != 'nan']
i=1
for url in urls:
    img = requests.get(url,stream=True)
    img.raw.decode_content=True
    f = open(path+str(i)+".jpg",'wb')
    i=i+1
    shutil.copyfileobj(img.raw,f)