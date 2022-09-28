from flask import Flask, redirect, request, jsonify, session

app = Flask(__name__)

# when utilise the session, the secret_key is a must to setup beforehand
app.secret_key = 'xxnnqqttlllpoc'

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


@app.route("/try/login", methods=['POST'])
def login():
    """
    username johndoe
    password abc123
    :return:
    """
    get_data = request.get_json()
    username = get_data.get("username")
    password = get_data.get("password")

    if not all([username, password]):
        return jsonify(msg = "username or password is incomplete")
    
    if username == 'johndoe' and password == 'abc123':
        # if verification is passed, the status of login will be saved in the session
        session["username"] = username
        return jsonify( msg = "login successfully")
    else:
        return jsonify( msg = "wrong user or password")


    pass


@app.route("/try/logout", methods=['GET'])
def logout():
    session.clear()
    return jsonify(msg = "sucessfully logout")
    pass

@app.route("/session", methods=['GET'])
def check_session():
    """
    this function aims to check if the user is login in the session
    """
    username = session.get("username")
    if username is not None:
        return jsonify(username = username)
    else:
        return jsonify(msg = "something went wrong")


    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='7777')

# host='0.0.0.0'