import datasource
from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo
import view
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Window(ThemedTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Fan Data')
        #==============style================
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=('Helvetica',22))
         #============end style===============
        


def main():

    path = "D:\GitHub/0000WorkSpace\window\w1121\order.csv"
    win = Window(theme = "arc")

    win.mainloop()

if __name__ == '__main__':
    main()