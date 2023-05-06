from peewee import *

def GetTable(pageId):
    connection = None
    try:
        connection = SqliteDatabase('products.db')
        print("Connection to SQLite DB successful")
    except:
        print("Connection error")

    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM products LIMIT {(pageId - 1) * 50},50")
    results = cursor.fetchall()
    connection.close()
    return results

def GetProductsByName(userRequest):
    connection = None
    try:
        connection = SqliteDatabase('products.db')
        print("Connection to SQLite DB successful")
    except:
        print("Connection error")

    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM 'products' WHERE NAME LIKE '{userRequest}%'")
    results = cursor.fetchall()
    connection.close()
    return results

