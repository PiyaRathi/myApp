from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Data(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String)


@app.route('/add',methods = ['GET'])
def add_data():
	name = request.args.get('name')
	user = Data(name=name)
	db.session.add(user)
	db.session.commit()
	return jsonify(result = 'Success')

@app.route('/get', methods=['GET'])
def get_data():
	data = Data.query.all()
	res = []
	for d in data:
		res.append({'id': d.id, 'name': d.name})
	return jsonify(data=res)
	
@app.route('/update', methods=['GET'])
def update_data():
	id = int(request.args.get('id'))
	name = request.args.get('name')
	data[id] = name
	return jsonify(data = data)
	
@app.route('/delete', methods=['GET'])
def delete_data():
	id = int(request.args.get('id'))
	name = request.args.get('name')
	del data[id] 
	return jsonify(data = data)
	
if __name__ == "__main__":
	app.run()