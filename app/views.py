from flask import render_template, flash, redirect
from forms import ContactForm
from app import app


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	return render_template('home.html')

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

@app.route('/calendar')
def calendar():
	return render_template('calendar.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if form.validate_on_submit():
		flash("Thank you! We'll get back to you as soon as possible.")
		return redirect('/home')
	return render_template('contact.html', form=form)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404