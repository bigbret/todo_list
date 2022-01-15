#Bret Miller Deka Popov

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

#inherits the db model

class Todo(db.Model):
    #ID for item, and unique value for each item
    id = db.Column(db.Integer, primary_key = True)
    #Title of todo item
    title = db.Column(db.String(100))
    #boolean for complete
    complete = db.Column(db.Boolean)

    def __init__(self, title):
        self.title = title
        self.complete = False

    def __repr__(self): 
        return '<Title %s>' % self.title


@app.route('/')
def index():
    #show all the todos and query the db 
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html', todo_list = todo_list)

#post method
@app.route("/add", methods= ["POST"])
def add():
    #adding 
    title = request.form["title"]
    if not title: 
        return 'Error'
    new_todo = Todo(title)   
    db.session.add(new_todo)
    db.session.commit()
    #redirects user to this page after adding item     
    return redirect(url_for("index"))           

#update method
@app.route("/update/<int:todo_id>")
def update(todo_id):
    #adding 
    todo = Todo.query.get(todo_id)

    if not todo: 
        return redirect(url_for("index"))
    if todo.complete: 
        todo.complete = False
    else: 
        todo.complete = True
    db.session.commit()
    #redirects user to this page after updating item     
    return redirect(url_for("index"))           

#delete method
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    #adding 
    todo = Todo.query.get(todo_id)
    if not todo: 
        return redirect(url_for("index")) 
    db.session.delete(todo)
    db.session.commit()  
    #redirects user to this page after adding item   
    return redirect(url_for("index"))       

if __name__ == '__main__':
    app.run(debug = True) 
