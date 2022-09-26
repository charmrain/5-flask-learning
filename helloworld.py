from flask import Flask, redirect, request, jsonify

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

@app.route("/test/post", methods = ['POST'])
def first_post():
    my_json = request.get_json()
    print(my_json)

    get_name = my_json.get("name")
    get_age = my_json.get("age")

    return "the name is {}, the age is {}".format(get_name, str(get_age))


@app.route("/test/post2", methods = ['POST'])
def json_post():
    my_json = request.get_json()
    print(my_json)

    get_name = my_json.get("name")
    get_age = my_json.get("age")
    if not all([get_name, get_age]):
        return jsonify(msg = "lacks of parameter")

    return jsonify(name=get_name, age=get_age)

app.run(host='0.0.0.0', port='7777')

# host='0.0.0.0'