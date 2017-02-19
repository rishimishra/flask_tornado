from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello"

@app.route("/<name>")
def hello_name(name):
	return "Hello %s" % name

@app.route("/<name>/<int:age>")
def hello_name_age(name, age):
	return "Hello %s you are now %d" % (name, age)

# if __name__ == '__main__':
# 	app.run()