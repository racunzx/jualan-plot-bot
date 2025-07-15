import matplotlib.pyplot as plt
import numpy as np
import datetime
import os
import requests

# Data jualan JUN 2025
sales_data = [
    ("1.6.2025", 910),
    ("4.6.2025", 279),
    ("5.6.2025", 397),
    ("6.6.2025", 363),
    ("10.6.2025", 751),
    ("11.6.2025", 575),
    ("12.6.2025", 777),
    ("13.6.2025", 943),
    ("14.6.2025", 993),
    ("15.6.2025", 1096),
    ("17.6.2025", 613),
    ("18.6.2025", 461),
    ("19.6.2025", 455),
    ("20.6.2025", 654),
    ("21.6.2025", 316),
    ("22.6.2025", 665),
    ("23.6.2025", 344),
    ("24.6.2025", 373),
    ("25.6.2025", 451),
    ("26.6.2025", 835),
    ("27.6.2025", 229),
    ("28.6.2025", 897),
    ("29.6.2025", 483),
    ("30.6.2025", 336),
]

# Proses data
label_x = []
sale = []

for date_str, s in sales_data:
    date_obj = datetime.datetime.strptime(date_str, "%d.%m.%Y")
    day_name = date_obj.strftime("%A")
    label = f"{day_name} ({date_str})"
    label_x.append(label)
    sale.append(s)

jumlah_sale = sum(sale)
purata_sale = jumlah_sale / len(sale)

# Plot graf jualan
fig, ax = plt.subplots(figsize=(14, 7))
x_indexes = np.arange(len(label_x))
color_sale = '#28B463'

ax.bar(x_indexes, sale, color=color_sale, label='Jualan Harian')
ax.axhline(purata_sale, color='blue', linestyle='--', linewidth=2, label=f'Purata: RM {purata_sale:.2f}')
ax.text(len(sale)-1, purata_sale + 10, f"Purata RM {purata_sale:.2f}", color='blue', ha='right')

ax.set_xlabel("Hari dan Tarikh")
ax.set_ylabel("Jualan (RM)")
ax.set_title("Jualan Harian JUN 2025")
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_xticks(x_indexes)
ax.set_xticklabels(label_x, rotation=45, ha="right")

for i, txt in enumerate(sale):
    ax.text(i, txt + 10, str(txt), ha='center', fontsize=8)

fig.text(0.1, 0.01, f"Total Jualan: RM {jumlah_sale:.2f}", fontsize=12, color='red')
ax.legend()
plt.tight_layout()

# Simpan gambar
filename = "graf_jualan_jun.png"
plt.savefig(filename)
plt.close()

# Hantar ke Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_photo(photo_path, caption="Graf Jualan JUN 2025"):
    if not BOT_TOKEN or not CHAT_ID:
        print("ERROR: BOT_TOKEN atau CHAT_ID tidak diset di environment variables.")
        return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(photo_path, "rb") as photo_file:
        files = {"photo": photo_file}
        data = {"chat_id": CHAT_ID, "caption": caption}
        resp = requests.post(url, files=files, data=data)
        print("Telegram response:", resp.json())

send_telegram_photo(filename)
