from flask import Flask, request, render_template, redirect, url_for,flash, session, g
import sqlite3
from functools import wraps

DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
#secret ket used for managing user session
SECRET_KEY = "\xcd\x8e\x15\xd6\xec\x8deY\x11\xddm\xf22x\xefm\xfd\xa4\xd0\xf1\x19M9&"

app=Flask(__name__)

app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash("You need to log in first.")
			return redirect(url_for('login'))
	return wrap

@app.route("/", methods=['GET', 'POST'])
def login():
	error = None
	status_code = 200	
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			status_code = 401
			error = "Invalid credentials. Please Try again."
		else:
			session['logged_in'] = True
			flash("you were logged in.")
			return redirect(url_for('main'))	
	return render_template("login.html", error=error), status_code

@app.route('/main')
@login_required
def main():
	g.db = connect_db()
	cur = g.db.execute("SELECT * FROM posts")
	posts = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template("main.html" , posts=posts)

@app.route('/add', methods=['POST'])
@login_required
def add():
	title=request.form['title']
	post=request.form['post']
	if not title or not post:
		flash("All fields are required. Please try again.")
		return redirect(url_for('main'))
	else:
		g.db=connect_db()
		g.db.execute("INSERT INTO posts(title, post) VALUES(?,?)", [title, post])
		g.db.commit()
		g.db.close()		
		flash("New entry was successfully posted!")
		return redirect(url_for('main'))

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash("You were logged out. Thank you!")
	return redirect(url_for('login'))

if __name__=="__main__":
	app.run(debug=True)
