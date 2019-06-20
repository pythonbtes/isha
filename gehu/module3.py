import tkinter as tk
def backclr():
    num1=var1.get()
    num2=var2.get()
    num3=var3.get()
    if num1:
        window.configure(background="red")
    elif num2:
        window.configure(background="blue")
    elif num3:
        window.configure(background="green")
    else:
        window.configure(background="white")
window=tk.Tk()
var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()
check1=tk.Checkbutton(window,text="red",bg="white",command=backclr,variable=var1,selectcolor="red")
check1.grid( row=1,column=4)
check2=tk.Checkbutton(window,text="blue",bg="white",command=backclr,variable=var2,selectcolor="blue")
check2.grid( row=2,column=4)
check3=tk.Checkbutton(window,text="green",bg="white",command=backclr,variable=var3,selectcolor="green")
check3.grid( row=3,column=4)
window.mainloop()