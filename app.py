from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)



# Define a BlogPost model for the database
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "tags": self.tags.split(",") if self.tags else [],
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }

# API endpoint to create a new blog post
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    post = BlogPost(title=data['title'], body=data['body'], tags=data.get('tags'))
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201

# API endpoint to retrieve all blog posts
@app.route('/posts', methods=['GET'])
def get_posts():
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return jsonify([post.to_dict() for post in posts]), 200

# API endpoint to retrieve a single blog post by ID
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = BlogPost.query.get(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    return jsonify(post.to_dict()), 200

# API endpoint to update an existing blog post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = BlogPost.query.get(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    data = request.get_json()
    post.title = data.get('title', post.title)
    post.body = data.get('body', post.body)
    post.tags = data.get('tags', post.tags)
    db.session.commit()
    return jsonify(post.to_dict()), 200

# API endpoint to delete an existing blog post
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = BlogPost.query.get(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    db.session.delete(post)
    db.session.commit()
    return "", 204

if __name__ == '__main__':
    app.run(debug=True)
