import os, json
from flask import Flask, Response, request, g
from flask_restful import abort, Api, Resource
from peewee import IntegrityError
from playhouse.shortcuts import model_to_dict
from database import get_db, Attendee

class AttendeesResource(Resource):
    def get(self):
	attendees = Attendee.select()
	r = json.dumps({'items':[model_to_dict(a) for a in attendees]})
	return Response(r, mimetype = 'application/json')

class WebhookListener(Resource):
    def post(self):
        payload = request.json
        form_response = payload['form_response']
	form_id = form_response['form_id']
	answers = form_response['answers']
	r_name = self.get_answer(answers, '21524209', 'text')
	r_website = self.get_answer(answers, '21524210', 'url')
	r_source = self.get_answer(answers, '21524211', 'choice')['label']
	r_email = self.get_answer(answers, '21524212', 'email')
	r_party = self.get_answer(answers, '21524213', 'choice')['label']
	r_other = self.get_answer(answers, '21524214', 'text')	

	try:
    	    with g.db.transaction():
	        Attendee.create(name = r_name, website = r_website, source = r_source, email = r_email, party = r_party, other = r_other)
    	except IntegrityError:
	    abort(500, message = 'Attendee email already exists')
    
        return {'message': 'Attendee added', 
        }

    def get_answer(self, answers, field_id, field_type):
        for i in answers:
            if i['field']['id'] == field_id:
	        return i[field_type]

app = Flask(__name__)
api = Api(app)
api.add_resource(AttendeesResource, '/attendees')
api.add_resource(WebhookListener, '/typeform-webhook')

@app.before_request
def before_request():
    g.db = get_db()
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

if __name__ == '__main__':
    app.run(debug=True, host=os.getenv('IP_ADDRESS', 'localhost'))
