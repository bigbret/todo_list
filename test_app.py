from app import *
import pytest 

website_path = "http://127.0.0.1:5000/"


def test_index(): 
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b'Todo Task Manager' in response.data

#@pytest.mark.skip(reason="not needed at this time")
def test_add():
    with app.app_context(): 
        client = app.test_client()
        url = '/add'
        data = {'title': 'School', 'tag': 'personal'}
        response = client.post(url, data = data, follow_redirects=True)
        assert b'School' in response.data
        assert b'personal' in response.data
        todo_title = 'School'

#@pytest.mark.skip(reason="not needed at this time")
def test_update():
    with app.app_context():
        todo_id = 1
        todo = Todo.query.get(todo_id) 
        status = todo.complete
        client = app.test_client()
        url = '/update/' + str(todo_id)
        response = client.get(url, follow_redirects=True) 
        assert status != todo.complete

#@pytest.mark.skip(reason="not needed at this time")
def test_update_priority():
     with app.app_context():
        todo_id = 2
        todo = Todo.query.get(todo_id) 
        priority = todo.priority 
        client = app.test_client()
        url = '/update_priority/' + str(todo_id)
        response = client.get(url, follow_redirects=True) 
        if priority == 3: 
            assert todo.priority == 1
        else: 
            assert todo.priority == priority + 1 

#@pytest.mark.skip(reason="not needed at this time")
def test_delete(): 
    with app.app_context():
        todo_id = 4
        todo = Todo.query.get(todo_id) 
        client = app.test_client()
        url = '/delete/' + str(todo_id)
        response = client.get(url, follow_redirects=True) 
        assert Todo.query.get(todo_id) == None 


