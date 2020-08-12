from flask import Flask
app = Flask(__name__)

@app.route('/')
def demo_one():
	return 'byee'

@app.route('/app')
def demo_two():
	return 'hello World'
	
if __name__ == "__main__":
	app.run()

#Hello.py