from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from werkzeug.urls import url_encode
from wtforms.validators import InputRequired, Email, Length
from flask_wtf.recaptcha import RecaptchaField
import os

last_submissions = {}

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'oliver.james.dev@gmail.com'
app.config['MAIL_PASSWORD'] = 'zgnjotsncjijnftp'
app.config['MAIL_DEFAULT_SENDER'] = 'oliver.james.dev@gmail.com'

mail = Mail(app)

app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lf3YmMrAAAAANW9oXmHUo9MCwc4D1dB_Vk7nXKl'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Lf3YmMrAAAAAKRKkGCh8quyA8Ym6srb4qSyua_K'

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=50)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    subject = StringField('Subject', validators=[Length(max=100)])
    message = TextAreaField('Message', validators=[InputRequired(), Length(min=10, max=1000)])
    recaptcha = RecaptchaField()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message(
            subject=f"New Contact: {form.subject.data}",
            recipients=['chabdulwahhab@yahoo.com'],
body = f"""
You have received a new message from the contact form on your portfolio website.

🧑 Name: {form.name.data}
📧 Email: {form.email.data}
📝 Subject: {form.subject.data}

💬 Message:
{form.message.data}

📅 Please reply promptly to maintain a good impression.
"""
        )
        mail.send(msg)
        flash('Message sent successfully! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)

@app.route('/projects')
def all_projects():
    return render_template('all_projects.html')

@app.route('/projects/project-one')
def project_one():
    return render_template('project.html')

@app.route('/projects/project-two')
def project_two():
    return render_template('project2.html')

@app.route('/projects/project-three')
def project_three():
    return render_template('project3.html')

@app.route('/projects/project-four')
def project_four():
    return render_template('project4.html')

@app.route('/projects/project-five')
def project_five():
    return render_template('project5.html')

@app.route('/projects/project-six')
def project_six():
    return render_template('project6.html')

@app.route('/projects/project-seven')
def project_seven():
    return render_template('project7.html')

@app.route('/projects/project-eight')
def project_eight():
    return render_template('project8.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True)
