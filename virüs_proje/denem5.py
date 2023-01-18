import random
import tkinter as tk
import pyautogui
from threading import Thread
import time

TRANS_COLOR = '#abcdef'


root = tk.Tk()
root.attributes("-topmost", True)
root.overrideredirect(1)
root.attributes('-transparentcolor', TRANS_COLOR)
root.geometry("+1920+1080")


image1 = tk.PhotoImage(file='ordek1.png')
image2 = tk.PhotoImage(file='ordek2.png')
image3 = tk.PhotoImage(file='ordek3.png')
image4 = tk.PhotoImage(file='ordek4.png')


label = tk.Label(root, image=image2, bg=TRANS_COLOR)
label.pack()

def mousu_cal():
    mouse_x, mouse_y = pyautogui.position()
    x, y = root.winfo_x(), root.winfo_y()
    if x==mouse_x and x!=0:
        def move_mouse():
            for i in range(20):
                pyautogui.moveTo(i, i, duration=1)

        def update_geometry():
            root.geometry("+{}+{}".format(mouse_x, mouse_y))


        thread1 = Thread(target=move_mouse)
        thread2 = Thread(target=update_geometry)
        thread2.start()
        thread1.start()
    root.after(50,mousu_cal)

def follow_mouse():
# Mouse'un x ve y koordinatlarını al
    mouse_x, mouse_y = pyautogui.position()
    x, y = root.winfo_x(), root.winfo_y()

# Güvercinin penceresini mouse'un konumuna doğru hareket ettir
    root.geometry("+{}+{}".format(x + (mouse_x - x) // 20, y + (mouse_y - y) // 20))

# Bir saniye bekle
    mesaj="ördek yeri: {},{} \n mouse yeri:{},{} ".format(x,y,mouse_x,mouse_y)
    print(mesaj)
    root.after(100, follow_mouse)


counter = 0
random_x=0
random_y=0
def move_window():
    x, y = root.winfo_x(), root.winfo_y()
    """random_x = random.randint(0, root.winfo_screenwidth()-root.winfo_width())
    random_y = random.randint(0, root.winfo_screenheight()-root.winfo_height())"""
    root.geometry("+{}+{}".format(x + (random_x - x) // 20, y + (random_y - y) // 20))
    """root.after(2000,rasgele_koordinat)"""
    root.after(200, move_window)
    print(random_x)
    """root.after(10000, rasgele_koordinat)"""

def rasgele_koordinat():
    global random_x
    global random_y
    random_x = random.randint(0, root.winfo_screenwidth() - root.winfo_width())
    random_y = random.randint(0, root.winfo_screenheight() - root.winfo_height())
    root.after(5000, rasgele_koordinat)



def update_image():
    global counter
    # Mouse'un x koordinatını al
    x, y = root.winfo_x(), root.winfo_y()
    # Ekranın yarısından sola mı yoksa sağa mı hareket ediyor güvercin
    if random_x < x:
        resim_listesi = [image1, image2]
    else:
        resim_listesi = [image3, image4]

    # label'ın resmini değiştirme
    label.config(image=resim_listesi[counter])
    counter += 1
    if counter >= len(resim_listesi):
        counter = 0
    root.after(200, update_image)

fonksiyon_sayici=0


root.after(200, update_image)

root.after(200,follow_mouse)

root.after(50,mousu_cal)





root.mainloop()

