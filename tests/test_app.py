import unittest
from app import app  # Import the app instance

class TestEmailGenerator(unittest.TestCase):

    def setUp(self):
        """Set up the app for testing."""
        self.client = app.test_client()  # Get a test client instance
        self.client.testing = True  # Enable testing mode

    def test_home_status_code(self):
        """Test the home route."""
        response = self.client.get('/')  # Send a GET request to the home route
        self.assertEqual(response.status_code, 200)  # Check that the status code is 200

    def test_generate_email_route(self):
        """Test the /generate-email POST route."""
        data = {
            "to": "test@example.com",
            "message": "Hello, how are you?",
            "tone": "formal"
        }
        response = self.client.post('/generate-email', json=data)  # Send a POST request to the /generate-email route

        self.assertEqual(response.status_code, 200)  # Check that the status code is 200
        response_json = response.get_json()  # Get the response JSON
        self.assertIn("email", response_json)  # Check that the 'email' key is in the response JSON

if __name__ == "__main__":
    unittest.main()
