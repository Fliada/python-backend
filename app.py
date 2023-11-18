from flask import Flask, render_template

app = Flask(__name__, template_folder='../../resources/templates')


@app.route('/')
def index():
    return 'Index Page'


@app.route('/status')
def status():
    return "Сделано на flask"


@app.route('/hello')
def hello():
    return render_template('index.html')


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == "__main__":
    app.run()