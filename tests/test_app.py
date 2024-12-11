import unittest

import pytest
from app import app  # Import your Flask app here


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_route(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['message'] == "Welcome to the Email Generator!"


def test_generate_email(client):
    """Test the email generation route."""
    response = client.post('/generate')
    assert response.status_code == 200
    assert "email" in response.json
    assert response.json['email'] == "Generated email content."

