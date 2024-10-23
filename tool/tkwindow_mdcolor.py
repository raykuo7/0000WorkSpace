from ttkthemes import ThemedTk
from tkinter import ttk
import tkinter as tk

import re
import pyperclip



def color_text_in_clipboard(word_color_map, font_size):
    clipboard_content = pyperclip.paste()

    for word, color in word_color_map.items():
        colored_word = f'<font color="{color}" size={font_size}>{word}</font>'
        clipboard_content = re.sub(f'({re.escape(word)})', colored_word, clipboard_content)

    pyperclip.copy(clipboard_content)

    print("已經將字上色並覆蓋回剪貼簿。")

def display_color_options():
    colors = {
        1: ('#FF0000', '紅色'),
        2: ('#0000FF', '藍色'),
        3: ('##4ae212df', '綠色'),
        4: ('#FFFF00', '黃色'),
        5: ('#d196e8df', '紫色'),
        6: ('#FFA500', '橙色'),
        7: ('#000000', '黑色'),
        8: ('#FFFFFF', '白色'),
        9: ('#808080', '灰色'),
        10: ('#FFC0CB', '粉紅色')
    }

    print("請選擇一個顏色：")
    for key, (hex_value, name) in colors.items():
        print(f"{key}: {name} ({hex_value})")
    
    return colors

def main_color():
    clipboard_content = pyperclip.paste()
    print("剪貼簿內容：")
    print(clipboard_content)

    word = clipboard_content

    colors = display_color_options()
    color_choice = int(input("請輸入顏色的數字選項："))

    color = colors.get(color_choice, ('#000000', '黑色'))[0]  # 預設顏色為黑色

    font_size = input("請輸入字體大小（預設為 3）：") or '3'

    word_color_map = {word: color}

    color_text_in_clipboard(word_color_map, font_size)




class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("650x600")
        self.title("MD color")

        style = ttk.Style(self)        

    # topframe============================================================ #

        topFrame = ttk.Frame(self, borderwidth=2,relief='groove')
        button1 = ttk.Button(topFrame, text="執行", command=self.copypaste)
        button1.pack()
    
        frame1 = ttk.Frame(topFrame,borderwidth=3,width=350,relief='groove')

        label1 = ttk.Label(frame1, text="剪貼簿內容：")
        label1.pack()

        self.copyboard = tk.StringVar()
        self.label2 = ttk.Label(frame1, textvariable=self.copyboard)
        self.label2.pack()
        
        frame1.pack(padx=10,pady=(10,0),ipadx=10,ipady=5,fill='y')
        topFrame.pack(padx=10,pady=(10,0),ipadx=10,ipady=10,fill='x')
        
    # mainframe=========================================================== #
        mainframe = ttk.Frame(self, borderwidth=2, relief='groove')




        mainframe.pack(padx=10, pady=10, ipadx=10, ipady=10,fill='x')
    # method============================================================== #

    def copypaste(self):
        clipboard_content = pyperclip.paste()
        self.copyboard.set(clipboard_content)
        pass
    
    

def main():
    window = Window(theme = 'arc')



    window.mainloop()

if __name__ == '__main__':
    main()