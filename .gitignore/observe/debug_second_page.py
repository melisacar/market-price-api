import requests
import json

# Test edilecek kategori URL'si (Ev ve Yaşam)
category_name = "Ev ve Yasam"
category_url = "https://api.hakmarexpress.com.tr/api/home/slug/ev-yasam-c"

# Headers (Aynı kalıyor)
headers = {
    "authority": "api.hakmarexpress.com.tr",
    "accept": "*/*",
    "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache, no-store, must-revalidate",
    "origin": "https://www.hakmarexpress.com.tr",
    "referer": "https://www.hakmarexpress.com.tr/",
    "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "x-client-id": "929e0000-5686-0050-fb3c-08dd41200896",
    "x-client-key": "24f04afcc2e292a994837c8fb9add6c7363ba35853a6b536962b76972d9bf4bc",
    "x-page-number": "2"  # Sayfa 2 için test ediyoruz
}

# Sayfa 2'nin JSON verisini çek
response = requests.get(category_url, headers=headers)

if response.status_code == 200:
    data = response.json()

    # JSON verisini dosyaya kaydet
    with open("debug_page_2.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("✅ Sayfa 2 JSON verisi kaydedildi: debug_page_2.json")
else:
    print(f"❌ Sayfa 2 isteğinde hata: {response.status_code}")
