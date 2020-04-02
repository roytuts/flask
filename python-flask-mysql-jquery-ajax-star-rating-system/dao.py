import pymysql
from flask import request
from db_config import mysql

def get_blog_rating(blog_id):
	conn = None
	cursor = None
	
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		
		sql = "SELECT COUNT(DISTINCT(vote_id)) total_rows, IFNULL(SUM(blog_vote),0) total_rating FROM blog_vote WHERE blog_id=%s LIMIT 1"
		sql_where = (blog_id,)
		
		cursor.execute(sql, sql_where)
		
		row = cursor.fetchone()
		
		return row
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

def get_blog_rating_from_ip(blog_id):
	conn = None
	cursor = None
	
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		
		ip = request.remote_addr
	
		sql = "SELECT vote_id as vote_id FROM blog_vote WHERE ip_address=%s AND blog_id=%s LIMIT 1"
		sql_where = (ip, blog_id,)
		
		cursor.execute(sql, sql_where)
			
		row = cursor.fetchone()
	
		if row:
			vote_id = row['vote_id']
			
			sql = "SELECT IFNULL(SUM(blog_vote),0) total_rating FROM blog_vote WHERE blog_id=%s LIMIT 1"
			sql_where = (blog_id,)
			
			cursor.execute(sql, sql_where)
			
			row = cursor.fetchone()

			rating = row['total_rating']
			rating = rating
			
			return int(round(rating, 0))
		else:
			return 0
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

def rate_blog(blog_id, rate):
	conn = None
	cursor = None
	
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		
		ip = request.remote_addr
	
		sql = "SELECT vote_id FROM blog_vote WHERE ip_address=%s AND blog_id=%s LIMIT 1"
		sql_where = (ip, blog_id,)
		
		cursor.execute(sql, sql_where)
			
		row = cursor.fetchone()
		
		if row:
			vote_id = row['vote_id']			
		
			sql = "SELECT IFNULL(SUM(blog_vote),0) total_rating FROM blog_vote WHERE vote_id=%s AND blog_id=%s LIMIT 1"
			sql_where = (vote_id, blog_id,)
			
			cursor.execute(sql, sql_where)
			
			row = cursor.fetchone()
			
			rating = row['total_rating']
			rating = rating
			
			return int(round(rating, 0))
		else:
			sql = "INSERT INTO blog_vote(blog_vote, blog_id, ip_address) VALUES(%s, %s, %s)"
			sql_where = (rate, blog_id, ip,)
			
			cursor.execute(sql, sql_where)
			
			conn.commit()
				
			sql = "SELECT IFNULL(SUM(blog_vote),0) total_rating FROM blog_vote WHERE blog_id=%s LIMIT 1"
			sql_where = (blog_id,)
			
			cursor.execute(sql, sql_where)
			
			row = cursor.fetchone()
	
			rating = row['total_rating']
			rating = rating
			
			return int(round(rating, 0))
	
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()