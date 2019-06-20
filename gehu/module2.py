from tkinter import *
from PIL import Image
from PIL import ImageTk
def loginuser():
    text1=textbox1.get()
    Label(window,text="welcome "+text1,bg="black",fg="white",font="blue 30").grid(row=3,column=0)
window=Tk()
window.title("translater");
imag=Image.open("translator-png-8.png")
imag=imag.resize((50,50),Image.ANTIALIAS)
photo1=ImageTk.PhotoImage(imag)
Label(window,image=photo1).grid(row=0,column=30)
Label(window,text="EtoH translate",bg="grey",fg="white",font="blue 30").grid(row=1,column=30)
Label(window,text="username",bg="grey",fg="white",font="blue 10").grid(row=4,column=15)
textbox1=Entry(window,width=20,bg="white")
textbox1.grid(row=4,column=20)
Label(window,text="password",bg="grey",fg="white",font="blue 10").grid(row=5,column=15)
textbox2=Entry(window,width=20,bg="white")
textbox2.grid(row=5,column=20)
Button(window,text="login",width=10,command=loginuser).grid(row=6,column=25)
window.mainloop()