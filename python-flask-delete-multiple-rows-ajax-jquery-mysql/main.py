import dao
import pymysql
from app import app
from flask import jsonify, request, render_template
		
@app.route('/delete_products', methods=['POST'])
def delete_products():	
	ids = request.json['ids']
	
	# validate the received values
	if ids:
		if ',' in ids:		
			ids = ids.split(',')
		
		resp = dao.delete_products(ids)
		
		if resp:
			resp = jsonify('<span style=\'color:green;\'>Products deleted successfully</span>')
			resp.status_code = 200
			return resp
		else:
			resp = jsonify('<span style=\'color:red;\'>Something went wrong during products deletion</span>')
			resp.status_code = 500
			return resp
	else:
		resp = jsonify('<span style=\'color:red;\'>Make sure you pass the required parameter</span>')
		resp.status_code = 400
		return resp
		
@app.route('/')
def home():
	products = dao.products()
	return render_template('app.html', products = products)
		
if __name__ == "__main__":
    app.run()