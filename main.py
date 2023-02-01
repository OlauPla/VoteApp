from flask import Flask, url_for, redirect, request, render_template
from replit import db

#db["users"] = ["1234","0000","1233"]
#db["x"] = []
#db["y"] = []

print(db["users"])


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		password = request.form['password']
		print(password)
		return redirect(url_for('vote', password=password))
		
	else:
		return render_template('index.html')

@app.route('/vote/<password>', methods=['GET', 'POST'])
def vote(password):
	if request.method == 'POST':
		#Add option chosen to the user
		pass

	else:
		users = db["users"]
		if password in users:
			if password != "0000":
				users.remove(password)
			db["users"] = users 
			return render_template('vote.html', password = password)

		else:
			return redirect(url_for('index'))


@app.route('/results')
def results():
	return render_template('results.html')


app.run(debug=True,host="0.0.0.0")
