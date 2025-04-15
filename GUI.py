import json
import tkinter as tk
from tkinter import ttk
from main import nbamessage

flag = 1

def setflag(v):
    global flag
    flag = v

def show_content():
    print()


root = tk.Tk()
root.title("NBA赛事信息")
root.geometry("600x500")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# ttk.Label(frame, text="选择功能：", font=("黑体", 16), width=10).grid(row=0, column=0)
ttk.Button(frame, text="显示赛程信息", command=lambda: setflag(1), width=26).grid(row=0, column=0, sticky=tk.W, pady=5)
ttk.Button(frame, text="显示排名信息", command=lambda: setflag(2), width=26).grid(row=0, column=1, sticky=tk.W, pady=5)
ttk.Button(frame, text="确认", command=show_content(), width=26).grid(row=0, column=2, pady=5)
nba = nbamessage(flag)
nba.get_message()
# 显示联赛名称和赛季
ttk.Label(frame, text=f" {nba.title}", font=("Helvetica", 16, "bold")).grid(row=1, column=0, sticky=tk.W)
ttk.Label(frame, text=f"赛季: {nba.duration}", font=("Helvetica", 14)).grid(row=2, column=0, sticky=tk.W)

# 创建一个框架来容纳内容
content_frame = ttk.Frame(frame, padding="10")
content_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))



root.mainloop()
