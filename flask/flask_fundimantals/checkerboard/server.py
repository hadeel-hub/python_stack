from cgitb import html
from re import X
from tabnanny import check
from turtle import color

from flask import Flask,render_template
app= Flask(__name__)

@app.route("/play/<int:x>/<int:y>")
def checkerboard(x,y):
    number_of_rows=x
    number_of_columns=y
    print(number_of_rows)
    return render_template("index.html",number_of_rows = x,number_of_columns = y)

if __name__=="__main__":
    app.run(debug=True)
