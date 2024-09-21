import tkinter as tk
from random import randint
from PIL import Image, ImageTk
import random
import resizeimage

window = tk.Tk()
window.geometry("800x1000")
window.title("Dice Roll")
window.config(background="#90be6d")
window.resizable(False,False)
dic = ["dice1.png","dice2.png","dice3.png","dice4.png","dice5.png","dice6.png",]
image = ImageTk.PhotoImage(Image.open(random.choice(dic)))
label1 = tk.Label(window,image=image)
label1.image=image
label1.place(x=145,y=100)
def dice_roll():
    image = ImageTk.PhotoImage(Image.open(random.choice(dic)))
   
    label1.configure(image=image)
    label1.image=image

button = tk.Button(window,text="Click Here to Dice Roll ",command=dice_roll,background="White",font="Arial")
button.place(x=340,y=640)
label3 =tk.Label(window,text="Empower Edge Solution",font="Arial",background="#90be6d",foreground="White")
label3.place(x=622,y=670)
window.mainloop()