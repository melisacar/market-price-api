import requests
import os
import pandas as pd
import time

# Output folder
output_folder = "hakmar_products"
os.makedirs(output_folder, exist_ok=True)

# Category URLs
category_urls = {
    "Ev ve Yasam": "https://api.hakmarexpress.com.tr/api/home/slug/ev-yasam-c?",
    "Gida ve Icecek": "https://api.hakmarexpress.com.tr/api/home/slug/gida-icecek-c?",
    "Anne ve Bebek": "https://api.hakmarexpress.com.tr/api/home/slug/anne-bebek-c?",
    "Kisisel Bakim ve Kozmetik": "https://api.hakmarexpress.com.tr/api/home/slug/kisisel-bakim-kozmetik-c?",
    "Temizlik": "https://api.hakmarexpress.com.tr/api/home/slug/temizlik-c?",
    "Elektronik ve Teknoloji": "https://api.hakmarexpress.com.tr/api/home/slug/elektronik-teknoloji-c?",
    "Giyim ve Aksesuar": "https://api.hakmarexpress.com.tr/api/home/slug/giyim-aksesuar-c?",
    "Spor ve Outdoor": "https://api.hakmarexpress.com.tr/api/home/slug/spor-outdoor-c?",
    "Yapi ve Oto": "https://api.hakmarexpress.com.tr/api/home/slug/yapi-oto-c?",
    "Oyuncak ve Kirtasiye": "https://api.hakmarexpress.com.tr/api/home/slug/oyuncak-kirtasiye-c?",
    "Pet Shop": "https://api.hakmarexpress.com.tr/api/home/slug/pet-shop-c?"
}

# Iterate over categories
for category_name, base_url in category_urls.items():
    print(f"Fetching data for: {category_name}")

    # Get first page to check total pages
    response = requests.get(f"{base_url}?page=1")
    if response.status_code != 200:
        print(f"API error in {category_name}: {response.status_code}")
        continue

    data = response.json()
    
    # Extract the correct `totalPages` information
    paging_info = data.get("paging", {})
    total_pages = paging_info.get("totalPages", 1)

    print(f"Total pages for {category_name}: {total_pages}")

    all_products = []
    unique_products = set()  # ✅ Eşsiz ürünleri takip etmek için set oluşturuldu

    # Loop through each page
    for page in range(1, total_pages + 1):
        url = f"{base_url}?page={page}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error on page {page} for {category_name}: {response.status_code}")
            break  # Stop if there's an error

        data = response.json()

        # Extract products from the correct JSON structure
        try:
            products = data["page"][1]["columns"][1]["contents"][1]["columns"][0]["content"]["products"]
            print(f"Page {page}: {len(products)} products found")
        except (KeyError, IndexError):
            print(f"Unexpected API structure on page {page} for {category_name}, skipping...")
            continue  # Skip if structure is different

        # Store products (avoid duplicates)
        for product in products:
            product_info = product.get("product", {})
            product_id = product_info.get("id")

            #if not product_id or product_id in unique_products:
            #    continue  # Eğer ID yoksa veya zaten kaydedildiyse, geç

            all_products.append([
                product_id,
                product_info.get("name"),
                product_info.get("price"),
                product_info.get("imageUrl")
            ])
            unique_products.add(product_id)  # ✅ Ürün ID ekleniyor

        print(f"Page {page}/{total_pages} completed for {category_name}")
        time.sleep(1)  # Wait to avoid calling the API too frequently

    # Save to Excel
    df = pd.DataFrame(all_products, columns=["ID", "Name", "Price (TL)", "Image URL"])
    # Unique on ids
    #df = df.drop_duplicates(subset=["ID"], keep="first")  
    filename = f"{output_folder}/{category_name.replace(' ', '_')}.xlsx"
    df.to_excel(filename, index=False, engine="openpyxl")

    print(f"Data saved for {category_name} -> {filename}")

print("All categories completed!")
