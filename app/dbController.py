import sqlite3

class dbCon:
    global connect
    global cursor

    connect = sqlite3.connect("mdb.db", check_same_thread=False) # или :memory: чтобы сохранить в RAM
    cursor = connect.cursor()

    #---------------------------------------------------------------------#
    def sign_up(login, password):
        cursor.connect("INSERT INTO users (login, pass) VALUES ('"+login+"', '"+password+"')")
        connect.commit()

    #---------------------------------------------------------------------#
