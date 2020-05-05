import pymysql
from db import mysql

def products():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		
		sql = "SELECT * FROM product"
		
		cursor.execute(sql)
		
		rows = cursor.fetchall()
		
		return rows
		
	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()

def delete_products(ids):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		
		sql = "DELETE FROM product WHERE id IN (" + ",".join(ids) + ")"
		
		cursor.execute(sql)
		
		conn.commit()
		
		return True
		
	except Exception as e:
		print(e)
		
		return False

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()