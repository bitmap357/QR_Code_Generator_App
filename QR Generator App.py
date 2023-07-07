from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

root = Tk()


def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200, 450, window=image_label)


canvas = Canvas(root, width=400, height=600)
canvas.pack()

root.mainloop()
