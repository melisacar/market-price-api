import requests
import json

url = "https://api.hakmarexpress.com.tr/api/home/slug/ev-yasam-c"

response = requests.get(url)
data = response.json()

# JSON output
print(json.dumps(data, indent=4, ensure_ascii=False))
