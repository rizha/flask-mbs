import pytest


@pytest.mark.parametrize(
    'test_input,expected',
    [
        [('user', 'password'), (201, 'user')],
        [('user', 'password'), (409, 'already exists')],
        [(None, None), (422, 'Field may not be null')]
    ]
)
def test_create(client, app, test_input, expected):
    username, password = test_input
    status_code, resp_message = expected

    rv = client.post('/users', json=dict(
        username=username,
        password=password
    ))

    assert status_code == rv.status_code
    assert resp_message.encode() in rv.data


def test_get(client):
    rv = client.get('/users')
    assert rv.status_code == 200


def test_tasks_users(client):
    from app.users.tasks import total_users
    a = total_users.delay()
    assert a.get() is not None
