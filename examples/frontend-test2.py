#!/usr/bin/python
'''
This code is to specifically show tkinter (a windowing interface toolbox)
I'm using it to potentially draw up to 3 lines in different colors, to the same scale on a graph

This is just to show, at a rudimentary level, python programs don't have to be "just text"
'''
import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt


top = tk.Tk("Liner")

tk.Label(top, text="Slope", fg='green').grid(row=0)
tk.Label(top, text="Intercept", fg='green').grid(row=1)
tk.Label(top, text="X range", fg='green').grid(row=2)

ent1 = tk.Entry(top)
ent1.grid(row=0, column=1 )

ent2 = tk.Entry(top)
ent2.grid(row=1, column=1)

ent3 = tk.Entry(top)
ent3.grid(row=2, column=1)
ent4 = tk.Entry(top)
ent4.grid(row=2, column=2)

tk.Label(top, text="Slope", fg='blue').grid(row=3)
tk.Label(top, text="Intercept", fg='blue').grid(row=4)

ent21 = tk.Entry(top)
ent21.grid(row=3, column=1 )

ent22 = tk.Entry(top)
ent22.grid(row=4, column=1)

tk.Label(top, text="Slope", fg='red').grid(row=5)
tk.Label(top, text="Intercept", fg='red').grid(row=6)

ent31 = tk.Entry(top)
ent31.grid(row=5, column=1 )

ent32 = tk.Entry(top)
ent32.grid(row=6, column=1)

def button1click():
    print( "Click!: slope=", ent1.get(), "Intercept: ", ent2.get())
#    p1 = [ent2.get(), 0]
#    p2 = [(20*ent1.get() + ent2.get()), 20]
    inter = float(ent2.get())
    slope = float(ent1.get())
    Xmin = int(ent3.get())
    Xmax = int(ent4.get())
    Xs = [Xmin, Xmax]
    Ys = [Xmin*slope + inter, (Xmax * slope + inter)]
    if slope > 0:
        Ymin = Xmin * slope + inter - 2
        Ymax = Xmax * slope + inter + 5
    else:
        Ymax = Xmin * slope + inter + 5
        Ymin = Xmax * slope + inter -2

    plt.plot(Xs,Ys, linewidth=2, marker = 'o', color='green')

    if len(ent22.get()) > 0:
        inter = float(ent22.get())
        slope = float(ent21.get())
        Xs = [Xmin, Xmax]
        Ys = [Xmin*slope + inter, (Xmax * slope + inter)]
        if slope > 0:
            Ymin = Xmin * slope + inter - 2
            Ymax = Xmax * slope + inter + 5
        else:
            Ymax = Xmin * slope + inter + 5
            Ymin = Xmax * slope + inter -2

        plt.plot(Xs,Ys, linewidth=2, marker = 'o', color='blue')

    if len(ent32.get()) > 0:
        inter = float(ent32.get())
        slope = float(ent31.get())
        Xs = [Xmin, Xmax]
        Ys = [Xmin*slope + inter, (Xmax * slope + inter)]
        if slope > 0:
            Ymin = Xmin * slope + inter - 2
            Ymax = Xmax * slope + inter + 5
        else:
            Ymax = Xmin * slope + inter + 5
            Ymin = Xmax * slope + inter -2

        plt.plot(Xs,Ys, linewidth=2, marker = 'o', color='red')

    plt.axis([Xmin-1,Ymax+1,Ymin,Ymax])
    plt.grid(True)
    plt.title( "Slope="+ent1.get()+" Intercept: "+ent2.get())
    plt.show()


button = tk.Button(top, text="Process", command=button1click  )
# button.pack()
button.grid(row=7, column=1)

photo = tk.PhotoImage(file="InitialGlyph.gif")
# later: after drawing: photo = ImageTk.PhotoImage(image)

biglbl = tk.Label(top, image=photo)
biglbl.image = photo
biglbl.grid(row=0, column=3, rowspan=6)


top.mainloop()