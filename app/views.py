from app import app

@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"

@app.route('/bravone')
def bravone():
	return "bravone!"
