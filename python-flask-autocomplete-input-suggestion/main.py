import os, json
from app import app
from flask import Flask, jsonify, request, redirect, render_template
	
@app.route('/')
def upload_form():
	return render_template('autocomplete.html')

@app.route('/search', methods=['POST'])
def search():
	term = request.form['q']
	print ('term: ', term)
	
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "data", "results.json")
	json_data = json.loads(open(json_url).read())
	#print (json_data)
	#print (json_data[0])
	
	filtered_dict = [v for v in json_data if term in v]	
	#print(filtered_dict)
	
	resp = jsonify(filtered_dict)
	resp.status_code = 200
	return resp

if __name__ == "__main__":
    app.run()