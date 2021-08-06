from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def board():
    return render_template("index.html", times=8)

@app.route('/<int:times>')
def number_select(times):
    return render_template("index.html", times=times)

# @app.route('/<int:times>')
# def number_select(times):
#     return render_template("index.html", times=times)


if __name__ == "__main__":
    app.run(debug=True)