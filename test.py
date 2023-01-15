from test_obj import status

test = status()


def test_conn_status():
    assert status.conn_status(connection=1) == 'Server now has connection'
    assert status.conn_status(connection=2) == 'No connection'
