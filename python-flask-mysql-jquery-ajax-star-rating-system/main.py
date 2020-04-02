import dao
#import pymysql
from app import app
from db_config import mysql
from flask import flash, render_template, request, redirect, url_for, jsonify
		
@app.route('/rate', methods=['POST'])
def rate_blog():
	blog_id = request.json['blog_id']
	rate = request.json['rate']
	# validate the received values
	if blog_id and rate:
		curr_rate = dao.rate_blog(blog_id, rate)
		
		result = dao.get_blog_rating(blog_id)
		vote_rows = int(result['total_rows'])
		rating = result['total_rating']
		vote_rate = int(round(rating/(vote_rows if vote_rows > 0 else 1), 0))
		vote_dec_rate = int(round(vote_rate, 0))
		
		curr_rating = int(round(curr_rate, 0))
		
		return jsonify({'vote_rows' : vote_rows, 'vote_rate' : vote_rate, 'vote_dec_rate' : vote_dec_rate, 'vote_curr_rate' : curr_rating})
	else:
		resp = jsonify({'message' : 'Bad Request - invalid credendtials'})
		resp.status_code = 400
		return resp
		
@app.route('/')
def home():
	#the hard-coded blog id value 1 should come from UI
	blog_id = 1;
	
	result = dao.get_blog_rating(blog_id)
	
	vote_rows = int(result['total_rows'])
	rating = result['total_rating']
	vote_rate = int(round(rating/(vote_rows if vote_rows > 0 else 1), 0))
	vote_dec_rate = int(round(vote_rate, 0))
	
	vote_ip_rate = dao.get_blog_rating_from_ip(blog_id)
	
	return render_template('star-rate-vote.html', overall_rows=vote_rows, overall_rate=vote_rate, overall_dec_rate=vote_dec_rate, ip_rate=vote_ip_rate)
		
if __name__ == "__main__":
    app.run()