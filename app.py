from flask import Flask
from flask import request, render_template, redirect
app = Flask(__name__)


@app.route('/')
def name():
	lines = {}
	with open('log.txt', 'r') as f:
		for line in f:
			message = line.split(", ")[0]
			name = line.split(", ")[1]
			lines[name] = message

	return render_template("template.html", chat=lines.items(), location="/redirect")

@app.route('/redirect', methods=['POST'])
def text():
	message = request.form['message']
	name = request.form['name']
	f = open('log.txt', 'a')
	if message == "clear_file":
		f.truncate(0)
	else:
		f.write(message + ", " + name + '\n')
	f.close()
	return redirect(f"/")