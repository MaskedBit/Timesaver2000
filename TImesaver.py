import tkinter as tk

root = tk.Tk()
root.title("Timesaver 2000")

def closer( event ):
    root.destroy()

root.bind( "<Escape>", closer )

ctrl = tk.Toplevel()
ctrl.title("Control window")

root.mainloop()
