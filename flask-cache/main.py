import pymysql
from app import app
from db import mysql
from app import cache
from flask import render_template
	
@app.route('/')
@cache.cached()
#@cache.cached(timeout=50)
def users():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user")
        rows = cursor.fetchall()
        print(rows)
        return render_template('index.html', rows=rows)
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    app.run()