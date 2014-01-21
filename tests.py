import os
import unittest
#from config import basedir

from app import app

class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def test_home_page_can_becontains_hello(self):
        response = self.app.get('/')
        assert 'Hello' in response.data
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()
