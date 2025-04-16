import json
import tkinter as tk
from tkinter import ttk
from main import nbamessage

def show_content(flag):
    nba = nbamessage(flag)
    nba.get_message()

    # 显示联赛名称和赛季
    ttk.Label(frame, text=f" {nba.title}", font=("Helvetica", 16, "bold")).grid(row=1, column=0, sticky=tk.W)
    ttk.Label(frame, text=f"赛季: {nba.duration}", font=("Helvetica", 14)).grid(row=2, column=0, sticky=tk.W)

    # 创建一个框架来容纳内容
    content_frame = ttk.Frame(frame, padding="10")
    content_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

    # 创建一个画布和滚动条
    canvas = tk.Canvas(content_frame)
    scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

    # 清除当前内容
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    if flag == 1:
        # 显示赛程信息
        for match in nba.matchs:
            date = match['date']
            week = match['week']
            for game in match['list']:
                time_start = game['time_start']
                status_text = game['status_text']
                team1 = game['team1']
                team2 = game['team2']
                team1_score = game['team1_score']
                team2_score = game['team2_score']

                # 创建一个方块来显示比赛信息
                game_frame = ttk.Frame(scrollable_frame, padding="10", relief="solid", borderwidth=1)
                game_frame.grid(sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

                # 显示日期和星期
                ttk.Label(game_frame, text=f"日期: {date}, 星期: {week}", font=("Helvetica", 12, "bold")).grid(row=0, column=0, columnspan=2, sticky=tk.W)

                # 显示比赛信息
                ttk.Label(game_frame, text=f"开始时间: {time_start}", font=("Helvetica", 10)).grid(row=1, column=0, sticky=tk.W)
                ttk.Label(game_frame, text=f"状态: {status_text}", font=("Helvetica", 10)).grid(row=1, column=1, sticky=tk.W)
                ttk.Label(game_frame, text=f"{team1} {team1_score}", font=("Helvetica", 12, "bold")).grid(row=2, column=0, sticky=tk.W)
                ttk.Label(game_frame, text=f"vs {team2_score} {team2} ", font=("Helvetica", 12, "bold")).grid(row=2, column=1, sticky=tk.W)

    elif flag == 2:
        # 显示排名信息
        for ranking in nba.rankings:
            name = ranking['name']
            ranking_list = ranking['list']

            # 显示排名名称
            ttk.Label(scrollable_frame, text=name, font=("Helvetica", 14, "bold")).grid(sticky=tk.W)

            # 创建一个表格来显示排名信息
            tree = ttk.Treeview(scrollable_frame, columns=("排名", "球队", "胜场", "负场", "胜率"), show="headings")
            tree.grid(sticky=(tk.W, tk.E, tk.N, tk.S))

            # 设置列标题
            tree.heading("排名", text="排名")
            tree.heading("球队", text="球队")
            tree.heading("胜场", text="胜场")
            tree.heading("负场", text="负场")
            tree.heading("胜率", text="胜率")

            # 设置列宽度
            tree.column("排名", width=50, anchor="center")
            tree.column("球队", width=150, anchor="center")
            tree.column("胜场", width=50, anchor="center")
            tree.column("负场", width=50, anchor="center")
            tree.column("胜率", width=50, anchor="center")

            # 插入数据
            for team in ranking_list:
                rank_id = team['rank_id']
                team_name = team['team']
                wins = team['wins']
                losses = team['losses']
                wins_rate = team['wins_rate']

                tree.insert("", tk.END, values=(rank_id, team_name, wins, losses, wins_rate))

root = tk.Tk()
root.title("NBA赛事信息")
root.geometry("450x400")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Button(frame, text="显示赛程信息", command=lambda: show_content(1), width=26).grid(row=0, column=0, sticky=tk.W, pady=5)
ttk.Button(frame, text="显示排名信息", command=lambda: show_content(2), width=26).grid(row=0, column=1, sticky=tk.W, pady=5)

root.mainloop()