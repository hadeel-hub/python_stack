from flask import Flask, render_template
app= Flask(__name__)

@app.route('/play/<name1>')
def users(name1="first_name"):
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    return render_template('index.html', users=users, name1 = name1)


@app.route('/play/<name1>/<name2>')
def users(name1, name2):
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    return render_template('index.html', users=users, name1 = name1, name2 = name2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 