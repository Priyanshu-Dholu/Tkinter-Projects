import tkinter
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer")
# root.geometry('500x500')
root.iconbitmap('D:\MEGA\Priyanshu\Programming\Python\Tkinter\Image Viewer\Window-Icon.ico')

img_1 = ImageTk.PhotoImage(Image.open("D:\MEGA\Priyanshu\Programming\Python\Tkinter\Image Viewer\Art1.png"))
img_2 = ImageTk.PhotoImage(Image.open("D:\MEGA\Priyanshu\Programming\Python\Tkinter\Image Viewer\Art2.png"))
img_3 = ImageTk.PhotoImage(Image.open("D:\MEGA\Priyanshu\Programming\Python\Tkinter\Image Viewer\Art3.png"))



image_list = [img_1, img_2,img_3]

label_1 = Label(image=img_1)
label_1.grid(row=0,column=0,columnspan=3)



button_back = Button(root,text='<')
button_exit = Button(root,text='Exit',command=root.quit)
button_forward = Button(root,text='>')

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)



root.mainloop()