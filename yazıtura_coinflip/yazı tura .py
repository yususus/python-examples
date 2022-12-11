"""
yazi tura oyunu yapımı
heads or tails game
"""
import tkinter as tk
from tkinter import *
import random

pencere = tk.Tk()
pencere.geometry("300x300")

yazi_tura = ["yazı", "tura"]

secme_label = tk.Label(pencere, text="Yazı mı Tura mı?")
secme_label.pack()

secim_var = tk.StringVar(pencere)
secim_entry = tk.Entry(pencere, textvariable=secim_var,
                       font=('calibre', 10, 'normal'))
secim_entry.pack()


def secim_sonuc():
    sonuc = secim_entry.get()
    abc = random.choice(yazi_tura)

    if sonuc == abc:
         sonucunuz = "Kazandınız"
    else:
         sonucunuz = "Kaybettinnn!!!"

    
    ekran_sonuc = tk.Label(pencere, text=sonucunuz)
    ekran_sonuc.pack()
    

    
dugme = Button(pencere, text="Gönder", command=secim_sonuc)
dugme.pack()
    
   
secim_sonuc()

pencere.mainloop()