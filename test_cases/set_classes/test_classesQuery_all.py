import requests
import unittest
class TestDepQueryALL(unittest.TestCase):
    def test_depQuery_all(self):
        url = r'http://127.0.0.1:8000/api/departments/ghi/classes/'
        res = requests.get(url)
        self.assertEqual(200, res.status_code)
        print(res.text)


        
        
        
        
        
        
        