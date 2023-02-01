'''
Description: 爬虫程序的GUI界面
Language: UTF-8
Author: hummer
Date: 2023-01-19 19:32:50
'''
from tkinter import *
from threading import Thread
from search import NovSearch
import time


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.createSearch()
        self.createContent()
        self.title = ""
        

    def createSearch(self):
        # 创建搜索区域
        self.sea_frame = Frame(self.master)
        self.sea_frame.pack(side=TOP, pady=30)
        # 创建提示信息
        self.sea_lab = Label(self.sea_frame, text="Please input your novel name:", font=("黑体", 14, "bold"))
        self.sea_lab.pack(side=TOP)
        # 创建搜索框
        self.title = StringVar()
        self.sea_entry = Entry(self.sea_frame, textvariable=self.title, width=20, font=("黑体", 14, "bold"))
        self.sea_entry.pack(side=LEFT, anchor=CENTER, pady=10)
        # 创建搜索按钮
        self.sea_btn = Button(self.sea_frame, text="search", command=lambda:self.searchClick(self.title), font=("黑体", 12, "bold"))
        self.sea_btn.pack(side=LEFT, padx=15)

    def createContent(self):
        # 创建显示区域
        self.sea_res = Frame(self.master)
        self.sea_res.pack(side=TOP, pady=30)
        # 创建提示标签
        self.res_lab = Label(self.sea_res, text="The search results are as follows: ", font=("黑体", 14, "bold"))
        self.res_lab.pack(side=TOP)
        # 创建显示文本框
        self.res_text = Text(self.sea_res, font=("黑体", 12))
        self.res_text.pack(side=TOP, pady=10)
        
        
    def searchClick(self, title):
        nov_search = NovSearch(title)
        nov_search.start()
        # nov_search.join()
        

def main():
    win = Tk()
    win.geometry("800x600+550+200")
    app = Application(win)
    win.mainloop() 
        
        
if __name__ == '__main__':
    main()