import requests

# Token pengguna (bukan token bot)
USER_TOKEN = "YOUR_USER_TOKEN"  # Ganti dengan token pengguna Anda

# URL endpoint Discord untuk mendapatkan daftar server (guilds)
GUILDS_URL = "https://discord.com/api/v9/users/@me/guilds"

# Headers untuk request API
headers = {
    "Authorization": USER_TOKEN,
    "Content-Type": "application/json"
}

# Mendapatkan daftar server yang telah diikuti oleh user
response = requests.get(GUILDS_URL, headers=headers)

# Mengecek apakah request berhasil
if response.status_code == 200:
    guilds = response.json()
    print(f"Anda telah bergabung dengan {len(guilds)} server.")
else:
    print(f"Gagal mengambil daftar server: {response.status_code}, {response.text}")
