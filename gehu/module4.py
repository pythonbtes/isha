from tkinter import *
window=Tk()
window.configure(background="#F1948A")
for i in range(1,5):
    Label(window,text="hello"+str(i),bg="grey",fg="white",font="blue 30").grid(row=i,column=30)
window.mainloop() 