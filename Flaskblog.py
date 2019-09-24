from flask import (Flask, render_template, url_for, flash, redirect,
                   get_flashed_messages)
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '9297376dbff349a9e5942888085ce4fe'

posts = [
    {
        'author' : 'Deepan Anbarasan',
        'title'  : 'Blog post 1-Test',
        'content': 'Frst post content',
        'date'   : 'September 11,2019'
        },
    {
        'author' : 'Ximena Garzon',
        'title'  : 'Mena 2-Test',
        'content': 'Second post content',
        'date'   : 'September 10,2019'
        }
    ]

about_title = 'about'


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about_page():
    return render_template('about.html', title=about_title)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == \
                'password':
            flash(f'Logged in successfully! {form.email.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Wrong username and password combination!', 'danger')

    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
