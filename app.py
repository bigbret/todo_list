'''
Bret Miller Deka Popov
CS321 - Project 1 
Building a flask application for a todo List Website
'''

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

#inherits the db model and is over arching class
class Todo(db.Model):
    '''
    Takes in db.Model as argument
    db.Model is a instance of an SQLAlchemy application 
    '''
    #ID for item, and unique value for each item
    id = db.Column(db.Integer, primary_key = True)
    #Title of todo item
    title = db.Column(db.String(100))
    #boolean for complete
    complete = db.Column(db.Boolean)
    #flag for priority of todo
    priority = db.Column(db.Integer)
    #tag for different things
    tag = db.Column(db.String(100))
    

    def __init__(self, title, priority, tag):
        self.title = title
        self.complete = False
        self.priority = priority
        self.tag = tag
        

    def __repr__(self): 
        return '<Title %s>' % self.title


@app.route('/')
def index():
    '''
    This loads the main home screen of the website
    '''
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html', todo_list = todo_list, datetime = str(datetime.now()))


@app.route("/add", methods= ["POST"])
def add():
    '''
    This will add items to the index screen 
    so that they are there on next reload 
    '''
    title = request.form["title"]
    tag = request.form['tag']
    if not title: 
        return 'Error'
    new_todo = Todo(title, 1, tag)   
    db.session.add(new_todo)
    db.session.commit()
    #reloads the page for the user in a way, bringing them back to the home screen
    return redirect(url_for("index"))           


@app.route("/update/<int:todo_id>")
def update(todo_id):
    '''
    This updates the status of the todo items 
    so that you can leave them on the screen and know finished vs unfinished
    '''
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

@app.route("/update_priority/<int:todo_id>")
def update_priority(todo_id):
    todo = Todo.query.get(todo_id)
    
    if not todo:
        return redirect(url_for("index"))
    if todo.priority == 3:
        todo.priority = 1
    else:
        todo.priority = todo.priority + 1
    db.session.commit()
    return redirect(url_for("index"))
                  


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
    #db.create_all()
    #db.session.commit()
    app.run(debug = True) 
