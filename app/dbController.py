import sqlite3

global connect
global cursor

connect = sqlite3.connect("mdb.db", check_same_thread=False) # или :memory: чтобы сохранить в RAM
cursor = connect.cursor()
