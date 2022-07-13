from tkinter import *
import tkinter as tk
import tkinter.font as tkFont # 导入了一个字体
import datetime
import time

class Screensaver():
    def __init__(self):
        self.win = Tk() # 基于tkiner中的Tk()方法实例个对象
        self.ft = tkFont.Font(family='Fixdsys', size=30, weight=tkFont.BOLD) # 修改字体的方法
        self.width = self.win.winfo_screenwidth() # 获取屏幕大小
        self.height= self.win.winfo_screenheight()

        self.win.overrideredirect(0) # 全屏设置
        self.win.attributes('-alpha',1) # 以参数alpha的方式设置透明度


        # 绑定事件
        self.canvas=Canvas(self.win,width=self.width,height=self.height,bg='#FFFFFF')
        self.Text=tk.Label(self.win,text= "%s%d"%(datetime.datetime.now().strftime('%H:%M:%S:'),datetime.datetime.now().microsecond // 100000),fg = '#FFF000').pack()
        self.canvas.pack()

        self.win.mainloop()
        #time.sleep(5)
        #self.win.destroy()
    def run_screensaver(self): # 循环体 ，不断更新屏幕内容
        if self.i == 1:
            for emumt in self.list_:
                emumt.move_text()
                if emumt.x1<= -30:
                    emumt
                    self.i = -1
                    self.delect()
                    self.list_ =[]
                    self.birth_list()
                    for my_text in self.str_text:
                        xt = Text_screen(self.canvas,self.ft,self.width,self.height,my_text)
                        self.list_.append(txt)
                        break
                else:
                    self.i *= -1
        self.canvas.after(1,self.run_screensaver) # 第一个参数是间隔事件吧？第二个是调用函数
        

Screensaver() # 实例化