from flask import Flask,render_template
app = Flask(__name__)

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

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about_page():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)

