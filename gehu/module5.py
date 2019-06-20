from tkinter import *
window=Tk()
frame=Frame(window)
frame.pack() 
string="python"
lngth=len(string)
for j in range (1,lngth+1):
    textbox1=Entry(frame,width=10,bg="black")
    textbox1.pack(side=LEFT)
window.mainloop()