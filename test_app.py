import unittest
from flask import Flask
from app import passw

class TestPassw(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_passw_all(self):
        response = self.client.post('/', data={'numbers': 'on', 'symbols': 'on', 'lgp': '10'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Generated Password:', response.data)

    def test_passw_ld(self):
        response = self.client.post('/', data={'numbers': 'on', 'lgp': '8'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Generated Password:', response.data)

    def test_passw_l(self):
        response = self.client.post('/', data={'lgp': '12'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Generated Password:', response.data)

    def test_pass_p(self):
        response = self.client.post('/', data={'symbols': 'on'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Generated Password:', response.data)

    def test_default(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Generated Password:', response.data)

if __name__ == '__main__':
    unittest.main()