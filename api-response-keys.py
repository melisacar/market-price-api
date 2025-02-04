import requests

url = "https://api.hakmarexpress.com.tr/api/home/slug/ev-yasam-c"
response = requests.get(url)
data = response.json()

# JSON keys
print(data.keys())
