from flask import Flask, jsonify, request
import json
from model.post import Post

posts = []

app = Flask(__name__)

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Post):
            return {'body': obj.body, 'author': obj.author}
        else:
            return super().default(obj)
app.json_encoder = ComplexEncoder

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})

@app.route('/post', methods=['POST'])
def create_post():
    """{"body": "Hello World", "author": "@kitamiian"}
    """
    post_json = request.get_json()
    body = post_json.get('body')
    author = post_json.get('author')
    new_post = Post(body, author)
    return jsonify(new_post.to_json())

@app.route('/post', methods=['GET'])
def get_posts():
    return jsonify({'posts': posts})

@app.route('/post', methods=['PUT'])
def update_post():
    """{"body": "Hello World", "author": "@kita
    """
    post_json = request.get_json()
    return jsonify(post_json)

@app.route('/post', methods=['DELETE'])
def delete_post():
    return jsonify({'response': 'post deleted'})


if __name__ == '__main__':
    app.run(debug=True)
