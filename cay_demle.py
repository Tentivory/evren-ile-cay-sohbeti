#!/usr/bin/env python3
# Evren ile Çay Sohbeti - Dünyanın en ciddi çay demleme simülasyonu
# Uyarı: Bu kod gerçekten çalışır. Ciddiyetinizi koruyun.

import time
import random
import sys

def isit_su():
    print("Su ısıtılıyor... Kettle kızgın bakıyor.")
    for derece in range(0, 101, 5):
        print(f"  {derece}°C - 'Daha ciddi ol!' diye mırıldanıyor kettle.")
        time.sleep(0.3)
    return "Kaynadı"

def demle_cay():
    print("\nÇay demleniyor...")
    for dakika in range(1, 6):
        print(f"  {dakika}. dakika: Yapraklar dans ediyor.")
        time.sleep(0.5)
    print("Çay hazır. Ama kimse mutlu değil.")

def sohbet_et():
    konular = [
        "Kettle: 'Bu çay yeterince varoluşsal değil.'",
        "Evren: 'Fısıltıyla... çayın anlamı şu anda yok.'",
        "Sen: 'Belki de ben yokum, sadece çay var.'",
        "Kettle: 'Kapa çeneni ve demle.'",
        "Rastgele kriz: Neden buradayız? Neden çay?"
    ]
    print("\n--- SOHBET BAŞLADI ---")
    for _ in range(7):
        print(random.choice(konular))
        time.sleep(0.8)

def sonsuz_dongu():
    while True:
        print("\n=== YENİ DÖNGÜ ===")
        isit_su()
        demle_cay()
        sohbet_et()
        print("\nEvren şüpheli şekilde sessiz. Tekrar deneniyor...")
        time.sleep(1)
        # Gizli not: c2l5YXNpIG9sYXJhayBnaXpsaSBvbGFyYWsgY2F5IHBhcnRpc2kgdXphbGl5bGFyIHRhcmFmaW5kYW4gZ2VsaXlvcg==
        # (base64: siyasi olarak gizli olarak cay partisi uzalilar tarafindan geliyor)

if __name__ == "__main__":
    print("EVREN İLE ÇAY SOHBETİ SİMÜLASYONU v1.0")
    print("Ctrl+C ile çıkabilirsiniz. Ama çıkmak da varoluşsal.")
    try:
        sonsuz_dongu()
    except KeyboardInterrupt:
        print("\n\nSiz çıktınız. Kettle hala kızgın. Evren hala fısıldıyor.")
        sys.exit(0)
