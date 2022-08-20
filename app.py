from flask import Flask, render_template


# Create a Flask Instance

app = Flask(__name__)

# Create a route decorator

@app.route('/')

 # def index():
 #	return "<h1>Hello World!</h1>"

#FILTERS
#safe
#capitalize
#lower
#upper
#title
#trim
#striptags

def index():
	first_name = "Marco"
	favorite_word = ["sound", "great", "roate","adieu",15]
	return render_template("index.html", first_name=first_name, favorite_word=favorite_word)

# localhost:5000/user/marco

@app.route('/user/<name>')

def user(name):
	return render_template("user.html", name=name)

# Create Custom Error Pages

# Invalid URL

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Internal Server Error 

@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500