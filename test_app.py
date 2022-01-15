from app import *

website_path = "http://127.0.0.1:5000/"


def test_index(): 
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_add():
    client = app.test_client()
    url = '/add'
    data = {'title': 'Grocery Shop'}
    response = client.post(url, data = data)
    assert response.status_code == 302  
    response = client.get("/")
    assert b'Grocery Shop' in response.data

'''
def test_update():
    client = app.test_client()
    url = '/update/<int:todo_id>'
    data = {'todo_id' : '1'}
    response = client.post(url, data = data)
    assert response.status_code == 302  
    response = client.get("/") 
    assert 
     #resp = client.get('/update/3', follow_redirects=True)

    

#def test_delete(client):
    #resp = client.post('/delete/1', follow_redirects=True)'''