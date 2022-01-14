#Bret Miller Deka Popov

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#create the database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#inherits the db model
class Todo(db.Model):
    #ID for item, and unique value for each item
    id = db.Column(db.Integer, primary_key = True)
    #Title of todo item
    title = db.Column(db.String(100))
    #boolean for complete
    complete = db.Column(db.Boolean)

#@app.route('/')
#def index():
    #show all the todos and query the db 
    #todo_list = Todo.query.all()
    #print(todo_list)
    #return render_template('base.html', todo_list = todo_list)

@app.route('/')
def home():
    return {'message': 'Hello Flask!'}

#post method
@app.route("/add", methods= ["POST"])
def add():
    #adding 
    title = request.form.get("title")
    new_todo = Todo(title=title, complete = False)   
    db.session.add(new_todo)
    db.session.commit()
    #redirects user to this page after adding item     
    return redirect(url_for("index"))           

#update method
@app.route("/update/<int:todo_id>")
def update(todo_id):
    #adding 
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()  
    #redirects user to this page after updating item     
    return redirect(url_for("index"))             

#delete method
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    #adding 
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()  
    #redirects user to this page after adding item     
    return redirect(url_for("index"))             



if __name__ == '__main__':
    db.create_all()

    app.run(debug = True)
