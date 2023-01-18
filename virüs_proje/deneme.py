import turtle
import random

# Ekranı ve kalem özelliklerini ayarlama
screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)

# Ekranın ölçülerini ayarlama
screen_width, screen_height = screen.screensize()

# Hareket etme fonksiyonu
def move():
    pen.forward(100)
    x, y = pen.pos()
    if x > screen_width / 2 or x < -screen_width / 2:
        pen.right(900)
    
    if y > screen_height / 2 or y < -screen_height / 2:
        pen.right(180)
    screen.ontimer(move, 100)

# Hareket etme fonksiyonunu çağırma
move()

# Ekranı gösterme
screen.mainloop()
