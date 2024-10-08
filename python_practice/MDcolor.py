'''
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
    顯示顏色選項並返回顏色字典 (顯示十六進位顏色碼及中文顏色名稱)
    """
    colors = {
        1: ('#FF0000', '紅色'),
        2: ('#0000FF', '藍色'),
        3: ('#008000', '綠色'),
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
    # 從剪貼簿讀取初始內容
    clipboard_content = pyperclip.paste()
    print("剪貼簿內容：")
    print(clipboard_content)

    # 輸入需要上色的文字
    word = input("請輸入要上色的文字：")

    # 顯示顏色選項並讓使用者選擇
    colors = display_color_options()
    color_choice = int(input("請輸入顏色的數字選項："))

    # 獲取對應的顏色 (使用 HTML 顏色碼與中文名稱)
    color = colors.get(color_choice, ('#000000', '黑色'))[0]  # 預設顏色為黑色

    # 輸入字體大小
    font_size = input("請輸入字體大小（預設為 3）：") or '3'

    # 生成字典
    word_color_map = {word: color}

    # 將文字上色並覆蓋回剪貼簿
    color_text_in_clipboard(word_color_map, font_size)

if __name__ == "__main__":
    main()

'''
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
        # 正確地將文字嵌入到 <font> 標籤內
        colored_word = f'<font color="{color}" size={font_size}>{word}</font>'
        # 使用正則表達式來精確匹配並替換目標文字
        clipboard_content = re.sub(f'({re.escape(word)})', colored_word, clipboard_content)

    # 將修改後的內容寫回剪貼簿
    pyperclip.copy(clipboard_content)

    print("已經將字上色並覆蓋回剪貼簿。")

def display_color_options():
    """
    顯示顏色選項並返回顏色字典 (顯示十六進位顏色碼及中文顏色名稱)
    """
    colors = {
        1: ('#FF0000', '紅色'),
        2: ('#0000FF', '藍色'),
        3: ('#008000', '綠色'),
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
    # 從剪貼簿讀取初始內容
    clipboard_content = pyperclip.paste()
    print("剪貼簿內容：")
    print(clipboard_content)

    # 輸入需要上色的文字
    # word = input("請輸入要上色的文字：")
    word = clipboard_content

    # 顯示顏色選項並讓使用者選擇
    colors = display_color_options()
    color_choice = int(input("請輸入顏色的數字選項："))

    # 獲取對應的顏色 (使用 HTML 顏色碼與中文名稱)
    color = colors.get(color_choice, ('#000000', '黑色'))[0]  # 預設顏色為黑色

    # 輸入字體大小
    font_size = input("請輸入字體大小（預設為 3）：") or '3'

    # 生成字典
    word_color_map = {word: color}

    # 將文字上色並覆蓋回剪貼簿
    color_text_in_clipboard(word_color_map, font_size)

if __name__ == "__main__":
    main()
