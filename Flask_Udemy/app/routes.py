from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	title = 'Mi Microblog'
	user = {'username' : 'nroy'}
	posts = [
		{
			'author': {'username' : 'Mariola'},
			'body': 'que lugar absolutamente bello'
		},
		{
			'author': {'username': 'Carlos'},
			'body': 'Volvere aqui de nuevo - Hermosa Espana'
		}
	]
	return render_template('index.html', user=user['username'], title=title, posts=posts)
