from datetime import datetime
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 1. Aktuális idő kiírása
now = datetime.now()
print("Aktuális idő:", now.strftime("%Y-%m-%d %H:%M:%S"))

# 2. Böngésző user-agent lekérdezése
ua = UserAgent()
user_agent = ua.random
print("Böngésző User-Agent:", user_agent)

# 3. Weboldal lekérése és title kiírása
url = "https://example.com"  # Itt átírhatod másik weboldalra is
headers = {'User-Agent': user_agent}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
title = soup.title.string if soup.title else "Nincs <title> elem"

print(f"A weboldal címe: {title}")
