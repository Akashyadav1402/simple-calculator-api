import unittest
import json
from app import app

class TestCalculatorAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the Calculator API!", response.data)

    def test_add(self):
        response = self.client.get('/add?a=2&b=3')
        self.assertEqual(response.status_code, 200)
        
        # ✅ Convert JSON response to a dictionary
        data = json.loads(response.data)
        self.assertEqual(data["result"], 5.0)  # Compare with float

    def test_subtract(self):
        response = self.client.get('/subtract?a=10&b=4')
        self.assertEqual(response.status_code, 200)

        # ✅ Convert JSON response to a dictionary
        data = json.loads(response.data)
        self.assertEqual(data["result"], 6.0)  # Compare with float

if __name__ == '__main__':
    unittest.main()
