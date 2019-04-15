

def test_create(client):
    rv = client.post('/users', json=dict(
        username='user',
        password='password'
    ))

    assert rv.status_code is 201