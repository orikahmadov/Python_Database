import sqlite3
from Book import Book
from Author import Author
try:
    conn =  sqlite3.connect("database.db")
    c=  conn.cursor()
except Exception as e:
    print(e)


def show_all(table_name):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute(f"SELECT * FROM {table_name}")
        items =  c.fetchall()
        for item in items:
            print(item)
    except Exception as e:
        print(e)
    else:
        conn.commit()
        conn.close()




def delete_table(table_name):
    try:
        con =  sqlite3.connect("database.db")
        c =  con.cursor()
        c.execute(f"DROP TABLE {table_name}")
    except Exception as e:
        print(e)
    else:
        con.commit()
        print(f"Successfully deleted {table_name}")
        con.close()





def add_one(table_name, col1, col2, col3):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute(f"INSERT INTO {table_name}  VALUES(?,?,?)",(col1, col2 , col3) )
    except Exception as e:
        print(e)
    else:
        conn.commit()
        print(f"Added new record to db")
        conn.close()

def add_many(table_name, list):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.executemany(f"INSERT INTO {table_name}  VALUES(?,?,?)",(list) )
    except Exception as e:
        print(e)
    else:
        conn.commit()
        print(f"Added new record to db")
        conn.close()


def delete_one(table_name, by_id):
    try:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute(f"DELETE FROM {table_name} WHERE author_id = (?)", str(by_id))
    except Exception as e:
        print(e)
    else:
        conn.commit()
        print(f"Deleted record with {by_id} id ")
        conn.close()


