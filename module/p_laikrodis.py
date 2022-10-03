from tkinter import *
from datetime import datetime


cor1 = "#3d3d3d"  # juoda
cor2 = "#fafcff"  # balta
cor3 = "#21c25c"  # zalia


la = Tk()
la.title("Laikrodis")
la.geometry('')
la.resizable(width=TRUE, height=TRUE)
la.configure(background=cor1)


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


l1 = Label(la, text="10:05:05", font=('ds-digital', 120 , 'bold'), bg=cor1, fg=cor3)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(la,  font=('ds-digital', 60 , 'bold'), bg=cor1, fg=cor3)
l2.grid(row=1, column=0, sticky=NW, padx=5)

laikrodis()

la.mainloop()