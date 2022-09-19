from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def survey():
    return render_template("index.html")
  
  
  
@app.route('/location', methods=['POST'])
def location():
  my_name= request.form['name']
  my_location= request.form['location']
  my_language= request.form['language']
  my_comment=request.form['comment']

  return render_template("show.html",name=my_name, my_location=my_location, my_language=my_language, comment=my_comment)




if __name__=="__main__":
    app.run(debug=True)