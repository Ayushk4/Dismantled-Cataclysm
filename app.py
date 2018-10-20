from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homePage():
    return render_template("home.html")

@app.errorhandler(404)
def pageNotFound(e):
    return ("Page Does Not Exist")

if __name__ == "__main__":
    app.run(debug=True)