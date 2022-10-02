from tkinter import *
import time


tinklas = Tk()
tinklas.title("Laikrodis")
width = 600
height = 400
vaizdo_plotis = tinklas.winfo_screenwidth()
vaizdo_virsus = tinklas.winfo_screenheight()
x = (vaizdo_plotis/2)- (width/2)
y = (vaizdo_virsus/2) - (height/2)
tinklas.geometry("%dx%d+%d+%d" % (width, height, x, y))
tinklas.resizable(0, 0)
tinklas.config(bg="black")


def laikas():
    p_laikas = time.strftime('%I: %M: %S')
    clock.config(text=p_laikas)
    clock.after(200, laikas)


virsus = Frame(tinklas, width=600, bd=1, relief=SOLID)
virsus.pack(side=TOP)
vidurys = Frame(tinklas, width=600)
vidurys.pack(side=TOP, expand=1)



lbl_title = Label(virsus, text="Pirmasis projektukas:Laikrodukas", width=600, font=("arial", 20))
lbl_title.pack(fill=X)

clock = Label(vidurys, font=('ds-digital', 150 , 'bold'), fg="green", bg="black")
clock.pack()


if __name__ == '__main__':
    laikas()
    tinklas.mainloop()

