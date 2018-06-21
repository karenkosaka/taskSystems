#-*- coding:utf-8 -*-
from django.db import models
import sqlite3

class create_gui():
    "タスク登録画面"
    entry1 = tk.Entry(root,font=("",20),justify="center",width=25)
    entry1.pack()
    
class create_sql():
    "DBにタスクを登録"
    def __init__(self):
        db = sqlite3.connect("data.db")
        cr = db.cursor()
        #タスクの読み込み
        task = entry1.get()
        try:
            cr.execute('create table main_table(task)')
            print("１件登録しました")
        except:
            print("エラーにより登録できませんでした")
            
