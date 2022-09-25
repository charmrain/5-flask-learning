from flask import Flask

app = Flask(__name__)

@app.route("/")
def first_script():
    return "Dowdow is a little child"

@app.route("/index")
def second_script():
    return "Mengmeng is a little dog"

app.run()

# host='0.0.0.0'