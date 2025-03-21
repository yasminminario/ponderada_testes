import unittest
import requests

class TestServer(unittest.TestCase):

    def test_get_html(self):
        # Testa se a página inicial está sendo servida corretamente
        response = requests.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)
        
    
    def test_get_css(self):
        # Testa se o CSS está sendo servido corretamente
        response = requests.get('http://localhost:8000/style.css')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'text/css')

if __name__ == '__main__':
    unittest.main()
