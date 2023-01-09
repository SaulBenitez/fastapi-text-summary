from app import main


def test_ping(test_app):
    # Given
    # test_app
    # This means the test configuration

    # When
    # This is the tested behavior
    response = test_app.get("/ping")

    # Then
    # This is the expected behavior
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong!", "testing": True}