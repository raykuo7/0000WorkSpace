from tkinter import ttk
from ttkthemes import ThemedTk
import re
import pyperclip


class Window(ThemedTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('MD檔上色')
        self.geometry('800x600')

        topFrame = ttk.Frame(self,borderwidth=3,relief='groove')
        topFrame.pack()

def main():
    window = Window(theme = "breeze")
    window.mainloop()

if __name__ == '__main__':
    main()