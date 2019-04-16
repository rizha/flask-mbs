def test_get(client):
    rv = client.get('/status')
    assert b'ok' in rv.data
