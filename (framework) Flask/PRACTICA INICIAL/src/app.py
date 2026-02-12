from flask import Flask, render_template

app = Flask(__name__)

@app.route("/user")
def show_post():
    return render_template("user/index.html")

@app.route("/admin")
def halo():
    return render_template("admin/index.html")

if __name__ == '__main__':
    app.run(debug=True)