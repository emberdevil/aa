#encoding = utf-8
"""
GUI（Graphics User Interface）图形用户界面

"""

from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("我的第一个GUI程序")  # 定义窗口标题
root.geometry("500x300+100+200")  # 定义窗口大小

btn01 = Button(root)
btn01["text"] = "点我就送花"

btn01.pack()

def songhua(e):  # e就是事件对象
    messagebox.showinfo("Message", "送你一朵玫瑰花，亲亲我吧")
    print("送你99多玫瑰花")

btn01.bind("<Button-1>", songhua)

root.mainloop()  # 调用组件的mainloop()方法，进入事件循环
