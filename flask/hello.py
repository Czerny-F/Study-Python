from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello', methods=['GET', 'POST'])
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'
    print('Request posted to hello')


@app.route('/user/<username>')
def show_user_profile(username):
    print(type(username))
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    print(type(post_id))
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    print(type(subpath))
    # show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about', methods=['GET'])
def about():
    print(request)
    print(type(request))
    print(request.__class__.mro())
    print(request.method)
    # print(vars(request))
    return 'The about page'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('projects'))
    print(url_for('projects', next='/'))
    print(url_for('show_user_profile', username='John Doe'))
    print(url_for('static', filename='style.css'))
