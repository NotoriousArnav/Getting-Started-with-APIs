import requests

URL = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

data = requests.get(URL)
data_json = data.json()
print(data_json)

hdurl = data_json['hdurl']
hdpicture = requests.get(hdurl)

with open(f"{data_json['date']}_NASA-APOD.jpg", 'wb') as f:
    f.write(hdpicture.content)
