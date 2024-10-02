import requests

# URL endpoint untuk melakukan top-up
url = "http://127.0.0.1:8000/topup/"
# Token akses yang didapatkan setelah login
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwODExMjU1NTAxIiwiZXhwIjoxNzI3ODU3OTkxfQ.SHfJ3z7NaDC-7q9snN4Sj-JUqB-YXSGUY4B24zNZGG4"  # Gantilah dengan token yang valid

# Header yang diperlukan
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

# Data yang ingin dikirim dalam permintaan top-up
data = {
    "amount": 500000
}

# Mengirim permintaan POST ke endpoint top-up
response = requests.post(url, headers=headers, json=data)

# Mencetak respons dari server
print(response.json())
