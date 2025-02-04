import requests

url = "https://api.hakmarexpress.com.tr/api/home/slug/ev-yasam-c"
response = requests.get(url)
data = response.json()

def find_components(data, path="data"):
    if isinstance(data, dict):
        if "component" in data:
            print(f"Found component: {data['component']} at {path}")
        for key, value in data.items():
            find_components(value, path + f"['{key}']")
    elif isinstance(data, list):
        for i, item in enumerate(data):
            find_components(item, path + f"[{i}]")

find_components(data)