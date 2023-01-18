"""
import pyautogui
import random
import time

pyautogui.FAILSAFE = False # Failsafe mekanizmasını devre dışı bırak


while True:
    x, y = pyautogui.position() # mevcut fare pozisyonunu al
    new_x = random.randint(0, pyautogui.size()[0]) # rastgele x koordinatı oluştur
    new_y = random.randint(0, pyautogui.size()[1]) # rastgele y koordinatı oluştur
    pyautogui.moveTo(new_x, new_y, duration=1) # fare imlecini yeni konuma taşı
    time.sleep(1) # 1 saniye bekle
"""

import pyautogui
import time
import random

#Fare imlecini ekran üzerinde yakala
x, y = pyautogui.position()

while True:
    mouse_x, mouse_y = pyautogui.position() # mevcut fare pozisyonunu al
    new_x = random.randint(0, pyautogui.size()[0]) # rastgele x koordinatı oluştur
    new_y = random.randint(0, pyautogui.size()[1]) # rastgele y koordinatı oluştur
    pyautogui.moveTo(new_x, new_y, duration=1) # fare imlecini yeni konuma taşı
    time.sleep(1) # 1 saniye bekle
