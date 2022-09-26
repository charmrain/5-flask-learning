from crypt import methods
from flask import Flask, redirect, request

app = Flask(__name__)

@app.route("/")
def first_script():
    return "Dowdow is a little child"

@app.route("/index")
def second_script():
    return "Mengmeng is a little dog"

@app.route("/video")
def youtube():
    return redirect("https://www.bilibili.com/")

# @app.route("test/post", methods = ['POST'])
# def first_post():
#     my_json = request.get_json()

app.run(host='0.0.0.0', port='7777')

# host='0.0.0.0'