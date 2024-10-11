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
        5: ('#800080', '紫色'),
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

def main():
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

if __name__ == "__main__":
    main()
