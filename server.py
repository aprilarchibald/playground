
from flask import Flask, render_template
app=Flask(__name__)

def index():
    return render_template("index.html")

@app.route('/play/<int:num>')
def play(num):
    return render_template("index_html", num=num, color ="blue")

@app.route('/play/<int:num>/<color>')
def play2(num, color):
    return render_template("index_html", num = num, color =color)


if __name__=="__main__":
    app.run(debug=True)
