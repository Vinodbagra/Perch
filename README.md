# Perch

first create a app.py file in a folder

After writing this code i run the following command
python -m venv env

then the command to activate the virtual environment .\env\Scripts\activate

After that installation of modules
pip install flask
pip install flask_sqlalchemy
pip install flask-migrate
flask db init
flask db migrate -m "message"
flask db upgrade

then setting the env variable
set FLASK_APP=app.py
set FLASK_ENV=development

then just run the application by command flask run




API testing urls and its response

(a) Create a new blog post with a title, body, and tags
Method in Postman = POST
url = http://127.0.0.1:5000/posts
Json in body = {
  "title": "My third Blog Post",
  "body": "This is the body of my third blog post.",
  "tags": "tag5,tag6"
}

Response = {
    "body": "This is the body of my third blog post.",
    "created_at": "2023-04-23 08:27:21",
    "id": 3,
    "tags": [
        "tag5",
        "tag6"
    ],
    "title": "My third Blog Post"
}

(b) Retrieve a list of all blog posts, sorted by date
Method in Postman = GET
URL = http://127.0.0.1:5000/posts
Response = [
    {
        "body": "This is the body of my third blog post.",
        "created_at": "2023-04-23 08:27:21",
        "id": 3,
        "tags": [
            "tag5",
            "tag6"
        ],
        "title": "My third Blog Post"
    },
    {
        "body": "This is the body of my second blog post.",
        "created_at": "2023-04-23 08:26:52",
        "id": 2,
        "tags": [
            "tag3",
            "tag4"
        ],
        "title": "My second Blog Post"
    },
    {
        "body": "This is the body of my first blog post.",
        "created_at": "2023-04-23 08:24:50",
        "id": 1,
        "tags": [
            "tag1",
            "tag2"
        ],
        "title": "My first Blog Post"
    }
]

(c) Retrieve a single blog post by ID
Method in Postman = GET
URL = http://127.0.0.1:5000/posts/1
Response = {
    "body": "This is the body of my first blog post.",
    "created_at": "2023-04-23 08:24:50",
    "id": 1,
    "tags": [
        "tag1",
        "tag2"
    ],
    "title": "My first Blog Post"
}

(d) Update an existing blog post
Method in Postman = PUT
URL = http://127.0.0.1:5000/posts/3
Json = {
  "title": "My fourth Blog Post",
  "body": "This is the body of my fourth blog post.",
  "tags": "tag7,tag8"
}

Response = {
    "body": "This is the body of my fourth blog post.",
    "created_at": "2023-04-23 08:27:21",
    "id": 3,
    "tags": [
        "tag7",
        "tag8"
    ],
    "title": "My fourth Blog Post"
}

(e) Delete an existing blog post
Method in Postman = DELETE
URL = http://127.0.0.1:5000/posts/3


