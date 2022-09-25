from itertools import count
from re import T
from flask import Flask, render_template, session,redirect
app = Flask(__name__)
app.secret_key="keep it secret"

@app.route("/")
def counter():
    if "count" not in session:
      session['count']=0
    else:
      session['count']+=1
    
    return render_template("index.html")

@app.route("/show")
def counter2():
    session.clear() 
    return redirect("/")

if __name__=="__main__":
    app.run(depug=True)
    