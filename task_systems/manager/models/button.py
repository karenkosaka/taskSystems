#-*- coding:utf-8 -*-
from django.db import models
import sqlite3
import tkinter as tk
import sys

class create ():
    def create_sql(self):
        #rootフレーム作成
        root = tk.Tk()
        root.title(u"add_task")
        root.geometry("400x500")
        
        #エントリー
        EditBox = tk.Entry()#root,font=("",20),justify="center",width=50)
        EditBox.pack()
        
        #DBに登録
        db = sqlite3.connect("data.db")
        cr = db.cursor()
        #タスクの読み込み
        task = EditBox.get()
        try:
            cr.execute('create table main_table(task)')
            print("１件登録しました")
        except:
            print("エラーにより登録できませんでした")

root =tk.Tk()
root.mainloop()
            
