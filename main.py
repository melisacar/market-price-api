import requests
import os
import pandas as pd
import time

# Create the output folder
output_folder = "hakmar_products"
os.makedirs(output_folder, exist_ok=True)

# Category URLs
category_urls = {
        "Ev ve Yasam": "https://api.hakmarexpress.com.tr/api/home/slug/ev-yasam-c",
    "Gida ve Icecek": "https://api.hakmarexpress.com.tr/api/home/slug/gida-icecek-c",
    "Anne ve Bebek": "https://api.hakmarexpress.com.tr/api/home/slug/anne-bebek-c",
    "Kisisel Bakim ve Kozmetik": "https://api.hakmarexpress.com.tr/api/home/slug/kisisel-bakim-kozmetik-c",
    "Temizlik": "https://api.hakmarexpress.com.tr/api/home/slug/temizlik-c",
    "Elektronik ve Teknoloji": "https://api.hakmarexpress.com.tr/api/home/slug/elektronik-teknoloji-c",
    "Giyim ve Aksesuar": "https://api.hakmarexpress.com.tr/api/home/slug/giyim-aksesuar-c",
    "Spor ve Outdoor": "https://api.hakmarexpress.com.tr/api/home/slug/spor-outdoor-c",
    "Yapi ve Oto": "https://api.hakmarexpress.com.tr/api/home/slug/yapi-oto-c",
    "Oyuncak ve Kirtasiye": "https://api.hakmarexpress.com.tr/api/home/slug/oyuncak-kirtasiye-c",
    "Pet Shop": "https://api.hakmarexpress.com.tr/api/home/slug/pet-shop-c"
}

# Headers for API requests
headers = {
    "authority": "api.hakmarexpress.com.tr",
    "accept": "*/*",
    "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache, no-store, must-revalidate",
    "origin": "https://www.hakmarexpress.com.tr",
    "referer": "https://www.hakmarexpress.com.tr/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "x-client-id": "929e0000-5686-0050-fb3c-08dd41200896",
    "x-client-key": "24f04afcc2e292a994837c8fb9add6c7363ba35853a6b536962b76972d9bf4bc"
}

# Loop through categories
for category_name, base_url in category_urls.items():
    print(f"Fetching data for: {category_name}")

    # First page request to determine total pages
    headers["x-page-number"] = "1"
    response = requests.get(base_url, headers=headers)
    
    if response.status_code != 200:
        print(f"API error in {category_name}: {response.status_code}")
        continue

    data = response.json()
    
    # Retrieve total page count
    total_pages = data.get("paging", {}).get("totalPages", 1)

    print(f"Total pages for {category_name}: {total_pages}")

    all_products = []
    unique_products = set()

    # Loop over the pages
    for page in range(1, total_pages + 1):
        headers["x-page-number"] = str(page)
        response = requests.get(base_url, headers=headers)

        if response.status_code != 200:
            print(f"Error on page {page} for {category_name}: {response.status_code}")
            break  # Exit if theres error

        data = response.json()

        # Determine the correct JSON structure based on page number
        try:
            if page == 1:
                products = data["page"][1]["columns"][1]["contents"][1]["columns"][0]["content"]["products"] # First page structure
            else:
                products = data["page"][0]["products"]  # Structure for page 2 and beyond
            print(f"Page {page}: {len(products)} products found")
        except KeyError:
            print(f"Unexpected API structure on page {page} for {category_name}, skipping...")
            continue  # Skip the page if the structure is unexpected

        # Store product details while avoiding duplicates
        for product in products:
            product_info = product.get("product", {})
            product_id = product_info.get("id")

            if not product_id or product_id in unique_products:
                continue

            all_products.append([
                product_id,
                product_info.get("name"),
                product_info.get("price"),
                product_info.get("imageUrl")
            ])
            unique_products.add(product_id)

        print(f"Page {page}/{total_pages} completed for {category_name}")
        time.sleep(1)  # Pause to prevent API overload

    # Save data to an Excel file
    df = pd.DataFrame(all_products, columns=["ID", "Name", "Price (TL)", "Image URL"])
    filename = f"{output_folder}/{category_name.replace(' ', '_')}.xlsx"
    df.to_excel(filename, index=False, engine="openpyxl")

    print(f"Data saved for {category_name} -> {filename}")

print("All categories completed! ✅")
