import tkinter as tk
import math
import random

window = tk.Tk()
window.title('Guess Number')
window.geometry('800x600')
window.configure(background='lightgreen')

ans = []
ans = random.sample(range(0, 10), 4)
print(ans)

def guess_num():

	G = guess_entry.get()
	Gus = list(G)
	
	if len(Gus) != 4:
		result = '錯誤!!請輸入四位數字!!'
	else:
		countA = 0
		for i in range(4):
			Gus[i]  = int(Gus[i])
			if ans[i] == Gus[i]:
				countA += 1
		
		countB = 0
		for i in range(4):
			for j in range(4):
				if Gus[i] != ans[i]:
					if Gus[i] == ans[j]:
						countB += 1
		if countA != 4:
			result = countA, 'A', countB, 'B'
		else:
			result = '恭喜答對了!!'
	result_label.configure(text=result)

header_label = tk.Label(window, text='請猜四位數字', font=('Arial', 30))
guess_label = tk.Label(window, text='輸入區', font=('Arial', 30))
guess_entry = tk.Entry(window, font=('Arial', 30))
guess_btn = tk.Button(window, text='確定送出', command=guess_num, font=('Arial', 30))
result_label = tk.Label(window, font=('Arial', 30), width=25, height=3 )

# 版面配置
header_label.grid(row=0, column=0, columnspan=2)
guess_label.grid(row=1, column=0)
guess_entry.grid(row=1, column=1)
guess_btn.grid(row=3, column=0)
result_label.grid(row=3, column=1)


window.mainloop()