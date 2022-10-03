from tkinter import *
from datetime import datetime


cor1 = "#3d3d3d"  # juoda
cor2 = "#fafcff"  # balta
cor3 = "#21c25c"  # zalia


root = Tk()
root.title("Laikrodis")
root.geometry('')
root.resizable(width=TRUE, height=TRUE)
root.configure(background=cor1)


def laikrodis():
    time = datetime.now()

    valanda = time.strftime("%H:%M:%S")
    savaites_diena = time.strftime("%A")
    diena = time.day
    menesiai= time.strftime("%b")
    metai = time.strftime("%Y")
    l1.config(text=valanda)
    l1.after(200, laikrodis)
    l2.config(text=savaites_diena + "" + str(diena) + "/" + str(menesiai) + "/" + (metai))


l1 = Label(root, text="10:05:05", font=('ds-digital', 120 , 'bold'), bg=cor1, fg=cor3)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(root,  font=('ds-digital', 60 , 'bold'), bg=cor1, fg=cor3)
l2.grid(row=1, column=0, sticky=NW, padx=5)

laikrodis()

root.mainloop()