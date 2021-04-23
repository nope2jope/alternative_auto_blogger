from flask import Flask, render_template
import requests


application = Flask(import_name=__name__)

all_posts = requests.get('https://api.npoint.io/e0eb025823d97820e87d').json()

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

@application.route('/contact.html')
def tender_contact():
    return render_template('contact.html')


application.run(debug=True)





