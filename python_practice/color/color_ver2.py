import re
import pyperclip

def color_text_in_clipboard(word_color_map, font_size):
    """
    將剪貼簿內容中的指定文字加上顏色與字體大小，然後覆蓋回剪貼簿
    
    :param word_color_map: 包含要上色的文字及其對應顏色的字典
    :param font_size: 指定的字體大小
    """
    # 從剪貼簿讀取內容
    clipboard_content = pyperclip.paste()

    # 將需要上色的文字加上 <font> 標籤
    for word, color in word_color_map.items():
        colored_word = f'<font color="{color}" size={font_size}>{word}</font>'
        # 使用正則表達式來替換目標文字
        clipboard_content = re.sub(f'\\b{word}\\b', colored_word, clipboard_content)

    # 將修改後的內容寫回剪貼簿
    pyperclip.copy(clipboard_content)

    print("已經將字上色並覆蓋回剪貼簿。")

def display_color_options():
    """
    顯示顏色選項並返回顏色字典 (使用十六進位顏色碼)
    """
    colors = {
        1: '#FF0000',  # red
        2: '#0000FF',  # blue
        3: '#008000',  # green
        4: '#FFFF00',  # yellow
        5: '#800080',  # purple
        6: '#FFA500',  # orange
        7: '#000000',  # black
        8: '#FFFFFF',  # white
        9: '#808080',  # gray
        10: '#FFC0CB'  # pink
    }

    print("請選擇一個顏色：")
    for key, value in colors.items():
        print(f"{key}: {value}")
    
    return colors

def main():
    # 從剪貼簿讀取初始內容
    clipboard_content = pyperclip.paste()
    print("剪貼簿內容：")
    print(clipboard_content)

    # 輸入需要上色的文字
    word = input("請輸入要上色的文字：")

    # 顯示顏色選項並讓使用者選擇
    colors = display_color_options()
    color_choice = int(input("請輸入顏色的數字選項："))

    # 獲取對應的顏色 (使用 HTML 顏色碼)
    color = colors.get(color_choice, '#000000')  # 預設顏色為黑色

    # 輸入字體大小
    font_size = input("請輸入字體大小（預設為 3）：") or '3'

    # 生成字典
    word_color_map = {word: color}

    # 將文字上色並覆蓋回剪貼簿
    color_text_in_clipboard(word_color_map, font_size)

if __name__ == "__main__":
    main()