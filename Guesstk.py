import tkinter as tk
import math
import random

window = tk.Tk()
window.title('Guess Number')
window.geometry('800x600')
window.configure(background='lightgreen')

ans = int(random.randint(1, 100))

def guess_range():
    
    G = int(guess_entry.get())
    while True:
        if G == ans:
            result = "\n恭喜您猜對了！"
            break
        elif G < ans:
            result = "\n請猜大一點！"
            break
        elif G > ans:
            result = "\n請猜小一點！"
            break
    result_label.configure(text=result)


header_label = tk.Label(window, text='請猜數字(1到100)', font=('Arial', 30))
guess_label = tk.Label(window, text='輸入區', font=('Arial', 30))
guess_entry = tk.Entry(window, font=('Arial', 30))
guess_btn = tk.Button(window, text='確定送出', command=guess_range, font=('Arial', 30))
result_label = tk.Label(window, font=('Arial', 20), width=25, height=3 )


# 版面配置
header_label.grid(row=0, column=0, columnspan=2)
guess_label.grid(row=1, column=0)
guess_entry.grid(row=1, column=1)
guess_btn.grid(row=3, column=0)
result_label.grid(row=3, column=1)


window.mainloop()