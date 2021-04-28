from flask import Flask, render_template, request
import requests
from email_funct import notify_user
import os


application = Flask(import_name=__name__)

all_posts = requests.get('https://api.npoint.io/e0eb025823d97820e87d').json()

USER_EMAIL = os.environ['ENV_USER_EMAIL']
USER_PASSWORD = os.environ['ENV_USER_PW']


@application.route('/')
def say_hi():
    return render_template('index.html', posts=all_posts)


@application.route('/post<int:num>')
def fetch_post(num):
    selected_post = None
    for post in all_posts:
        if post['id'] == num:
            selected_post = post

    return render_template('post.html', post=selected_post, num_choice=num)

@application.route('/about')
def tender_about():
    return render_template('about.html')

@application.route('/contact', methods=['GET', 'POST'])
def tender_contact():
    if request.method == 'POST':
        credentials = request.form.items()
        # reformat this body message so that fields are more elegantly represented
        body_msg = ""
        for item in credentials:
            body_msg += item[1] + '\n'
        # notification is being sent from and to same user for testing
        notify_user(email=USER_EMAIL, pw=USER_PASSWORD, user_from=USER_EMAIL, user_to=USER_EMAIL, body_text=body_msg)
        # return to confirmation page
        return ("<h1>WOO</h1>")
    elif request.method == 'GET':
        return render_template('contact.html')


application.run(debug=True)





