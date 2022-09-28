from app import app

@app.route("/")
def first_script():
    return "Dowdow is a little child"

@app.route("/about")
def about():
    return "<h1 style='color: red'>About!!!!</h1>"