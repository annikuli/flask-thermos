from flask import Flask, render_template, url_for

app = Flask(__name__)


class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def initials(self):
        return f'{self.firstname[0]}. {self.lastname[0]}.'



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Title passed from view to template', user = User('Anton', 'Nikulin'))

@app.route('/add')
def add():
    return render_template('add.html')


@app.errorhandler(404)
def error_handler(e):
    return render_template('404.html'), 404






if __name__ == '__main__':
    app.run(debug=True)
