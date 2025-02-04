import requests

# Ev ve yasam category
url = "https://api.hakmarexpress.com.tr/api/home/slug/ev-yasam-c"

response = requests.get(url)
data = response.json()

products = data["page"][1]["columns"][1]["contents"][1]["columns"][0]["content"]["products"]

for product in products:
    product_info = product.get("product", {})
    print(f"ID: {product_info.get('id')}")
    print(f"Name: {product_info.get('name')}")
    print(f"Price: {product_info.get('price')} TL")
    print(f"Image URL: {product_info.get('imageUrl')}")
    print("-" * 50)

