import os
from datetime import datetime
from flask import Flask
from flask import request
from flask import current_app
from flask import make_response
from flask import render_template
from flask import redirect, session, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from flask.ext.mail import Mail
from wtforms.validators import Required



class NameForm(Form):
	name = StringField('What is your name?',validators=[Required()])
	submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)





@app.route('/', methods=['GET', 'POST']) 
def index():     
	# name = None     
	# form = NameForm()     
	# if form.validate_on_submit():         
	# 	name = form.name.data         
	# 	form.name.data = ''     
	# return render_template('index.html', form=form, name=name)
	# form = NameForm()     
	# if form.validate_on_submit():         
	# 	session['name'] = form.name.data         
	# 	return redirect(url_for('index'))     
	# return render_template('index.html', form=form, name=session.get('name'))
	form = NameForm()
	if form.validate_on_submit():         
		old_name = session.get('name')         
		if old_name is not None and old_name != form.name.data:
		    flash('Looks like you have changed your name!')         
		    session['name'] = form.name.data         
		    return redirect(url_for('index'))     
	return render_template('index.html',form = form, name = session.get('name'))

@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name)

@app.errorhandler(404) 
def page_not_found(e):     
	return render_template('404.html'), 404  

@app.errorhandler(500) 
def internal_server_error(e):     
	return render_template('500.html'), 500



if __name__ == '__main__':
	app.run(debug=True)