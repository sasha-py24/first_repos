from flask import Flask, render_template, request
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = '<KEY>'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# in terminal
# flask db init
#
# flask db migrate
# flasf db upgrade




class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(80), nullable=False)
    post = db.Column(db.Integer, ForeignKey('post.id'), nullable=False)


@app.route('/', methods =['GET'])
def index():

    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/', methods =['POST'])
def post_create():

    title = request.form['title']
    text = request.form['text']
    image = request.files['image']

    # не form а files бо картинка і дані не текст чи числа, файли окремо відправляємо

    image.save(f'app/static/images/{image.filename}')
    # пишемо шлях до картинки
    post = Post(title=title, content=text, image=f'/static/images/{image.filename}')
    db.session.add(post)
    db.session.commit()
    return {}


@app.route('/post/<int:id>', methods = ['GET'])
def show_post(id):

    post = Post.query.get(id)
    comments = Comment.query.filter_by(post = id)
    return render_template('post.html', post = post, comments=comments)


@app.route('/post/<int:id>/add-comment/', methods = ['POST'])
def post_add_comment(id):

    text = request.form['text']
    # дістаємo зі словника ключ comment
    comment = Comment(text = text, post=id)
    db.session.add(comment)
    db.session.commit()
    return {}

@app.route('/post/<int:id>/delete-comment/', methods = ['POST'])
def post_delete_comment(id):

    comment = Comment.query.get(id)
    db.session.delete(comment)
    db.session.commit()
    return {'id': id}

