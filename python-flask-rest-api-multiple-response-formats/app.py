import rest
import json
from simplexml import dumps
from flask import Flask, make_response
from flask_restful import Api

app = Flask(__name__)

api = Api(app)
#api = Api(app, default_mediatype='application/json')

@api.representation('application/json')
def output_json(data, code, headers=None):
	resp = make_response(json.dumps({'response' : data}), code)
	resp.headers.extend(headers or {})
	return resp

@api.representation('application/xml')
def output_xml(data, code, headers=None):
	resp = make_response(dumps({'response' : data}), code)
	resp.headers.extend(headers or {})
	return resp

#api.representations['application/json'] = output_json
#api.representations['application/xml'] = output_xml

api.add_resource(rest.Greet, '/')
api.add_resource(rest.GreetName, '/<string:name>')

if __name__ == "__main__":
	app.run()