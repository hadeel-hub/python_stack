from flask import Flask, render_template
app= Flask(__name__)



@app.route('/')
def hello():
    return "hello"

@app.route('/users')
def users1():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template('index.html', users=users)


@app.route('/users/<name1>/<name2>')
def users2(name1, name2):
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    users.append({'first_name' :name1, 'last_name' : name2})
    return render_template('index.html', users=users)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 