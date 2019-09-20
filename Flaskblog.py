from flask import Flask,render_template,url_for
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '9297376dbff349a9e5942888085ce4fe'

posts = [
    {
        'author': 'Deepan Anbarasan',
        'title': 'Blog post 1-Test',
        'content': 'Frst post content',
        'date': 'September 11,2019'
        },
    {
        'author' : 'Ximena Garzon',
        'title'  : 'Mena 2-Test',
        'content': 'Second post content',
        'date'   : 'September 10,2019'
        }
         ]

about_title= 'about'

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about_page():
    return render_template('about.html', title=about_title)

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form = form)

@app.route('/login')
def register():
    form = LoginForm()
    return render_template('login.html', title='Login', form = form)

if __name__ == "__main__":
    app.run(debug=True)

