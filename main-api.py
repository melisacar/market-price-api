import requests

# API'nin adresi
api_url = "https://api.hakmarexpress.com.tr/api/home/slug/ev-yasam-c"

# Headers ekleyerek tarayıcı gibi görünmesini sağlıyoruz
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# API'ye GET isteği gönder
response = requests.get(api_url, headers=headers)

# Başarılı yanıt aldıysak
if response.status_code == 200:
    data = response.json()  # JSON formatına çevir
    print(data)  # Tüm veriyi görmek için
else:
    print("API'ye erişilemedi!")