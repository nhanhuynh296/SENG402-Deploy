import pytest
from application import app


@pytest.fixture(scope='module')
def test_client():
    flask_app = app
    flask_app.testing = True
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


def test_home_page1():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = app
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
