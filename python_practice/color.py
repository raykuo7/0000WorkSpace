import re
import pyperclip

def color_text_in_clipboard(word_color_map):
    """
    將剪貼簿內容中的指定文字加上顏色，然後覆蓋回剪貼簿
    
    :param word_color_map: 包含要上色的文字及其對應顏色的字典
                          例如：{'Python': 'red', 'Markdown': 'blue'}
    """
    # 從剪貼簿讀取內容
    clipboard_content = pyperclip.paste()

    # 將需要上色的文字加上 HTML 標籤
    for word, color in word_color_map.items():
        colored_word = f'<span style="color:{color};">{word}</span>'
        # 使用正則表達式來替換目標文字
        clipboard_content = re.sub(f'\\b{word}\\b', colored_word, clipboard_content)

    # 將修改後的內容寫回剪貼簿
    pyperclip.copy(clipboard_content)

    print("已經將字上色並覆蓋回剪貼簿。")

def display_color_options():
    """
    顯示顏色選項並返回顏色字典
    """
    colors = {
        1: 'red',
        2: 'blue',
        3: 'green',
        4: 'yellow',
        5: 'purple',
        6: 'orange',
        7: 'black',
        8: 'white',
        9: 'gray',
        10: 'pink'
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

    # 獲取對應的顏色
    color = colors.get(color_choice, 'black')  # 預設顏色為黑色，如果輸入無效
    
    # 生成字典
    word_color_map = {word: color}

    # 將文字上色並覆蓋回剪貼簿
    color_text_in_clipboard(word_color_map)

if __name__ == "__main__":
    main()