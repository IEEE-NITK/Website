from flask import render_template, flash, redirect
from forms import ContactForm
from config import ADMINS
from emails import send_email
from app import app


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/sig_overview')
def sig_overview():
	return render_template('sig_overview.html')

@app.route('/sight')
def sight():
	return render_template('sight.html')

@app.route('/epics')
def epics():
	return render_template('epics.html')

@app.route('/wie')
def wie():
	return render_template('wie.html')

@app.route('/gini')
def gini():
	return render_template('gini.html')

@app.route('/general_events')
def general_events():
	return render_template('gen_events.html')

@app.route('/awards_and_initiatives')
def awards_and_initiatives():
	return render_template('a_and_i.html')


@app.route('/calendar')
def calendar():
	return render_template('calendar.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if form.validate_on_submit():
		send_email(form.subject.data, form.email.data, ADMINS, form.message.data)
		flash("Thank you! We'll get back to you as soon as possible.")
		return redirect('/home')
	return render_template('contact.html', form=form)
