import requests

# Token pengguna (bukan token bot)
USER_TOKEN = "YOUR_USER_TOKEN"

# URL endpoint Discord untuk mendapatkan daftar server (guilds)
GUILDS_URL = "https://discord.com/api/v9/users/@me/guilds"

# Headers yang dibutuhkan
headers = {
    "Authorization": USER_TOKEN,
    "Content-Type": "application/json"
}

# Daftar server yang masuk blacklist (ID server yang tidak akan ditinggalkan)
blacklist_guild_ids = ["ID_SERVER_1", "ID_SERVER_2"]  # Masukkan ID server yang tidak ingin keluar

# Mendapatkan daftar server yang telah diikuti
response = requests.get(GUILDS_URL, headers=headers)
if response.status_code != 200:
    print(f"Failed to retrieve guilds: {response.status_code}")
    exit()

# Mengambil data server
guilds = response.json()

print(f"Bot terhubung ke {len(guilds)} server.")

# Looping untuk keluar dari server yang tidak ada di blacklist
for guild in guilds:
    guild_id = guild['id']
    guild_name = guild['name']

    # Jika server tidak ada dalam blacklist, maka bot akan keluar
    if guild_id not in blacklist_guild_ids:
        print(f"Meninggalkan server: {guild_name} (ID: {guild_id})")

        # URL endpoint untuk meninggalkan server
        leave_url = f"https://discord.com/api/v9/users/@me/guilds/{guild_id}"
        
        # Mengirim request DELETE untuk keluar dari server
        leave_response = requests.delete(leave_url, headers=headers)

        if leave_response.status_code == 204:
            print(f"Berhasil keluar dari server: {guild_name}")
        else:
            print(f"Gagal keluar dari server: {guild_name}, Error: {leave_response.status_code}")
    else:
        print(f"Server '{guild_name}' ada di blacklist, tidak akan ditinggalkan.")

print("Selesai memproses server.")
