import requests
import unittest
url = r'http://127.0.0.1:8000/api/departments/'
req_head = {"Content-Type":"application/json"}
class TestDepPost(unittest.TestCase):
    def test_depPost(self):
        req_data = r'{"data":[{"dep_id":"中国001","dep_name":"北京001","master_name":"市长007","slogan":"北京欢迎您"}]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(200,res.status_code)

    def test01_depPost(self):
        req_data = r'{"data":[{"dep_id":"美国250","dep_name":"纽约250","master_name":"纽约市长250","slogan":""}]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(200,res.status_code)

    def test02_depPost(self):
        req_data = r'{"data":[{"dep_id":"","dep_name":"魔法学院","master_name":"哈利波特","slogan":""}]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400,res.status_code)

    def test03_depPost(self):
        req_data = r'{"data":[{"dep_id":"星云001","dep_name":"","master_name":"女超人","slogan":""}]}'
        res = requests.post(url, req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400, res.status_code)

    def test04_depPost(self):
        req_data = r'{"data":[{"dep_id":"星云002","dep_name":"星球大战","master_name":"","slogan":""}]}'
        res = requests.post(url, req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400, res.status_code)

    def test05_depPost(self):
        req_data = r'{"data":[{"dep_id":"中国001","dep_name":"北京001","master_name":"市长007","slogan":"北京欢迎您"}]}'
        res = requests.post(url, req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400, res.status_code)

    def test06_depPost(self):
        req_data = r'{"data":[{"dep_id":"北京001","master_name":"北京市长","slogan":"北京欢迎您"}]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400,res.status_code)

    def test07_depPost(self):
        req_data = r'{"data":[{"dep_id":"广州001","dep_name":"广州","slogan":""}]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400,res.status_code)

    def test08_depPost(self):
        req_data = r'{"data":[{"dep_id":"武汉001","dep_name":"武汉","master_name":"武汉市长","slogan":"武汉欢迎您"},{"dep_id":"武汉001"]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400,res.status_code)

    def test09_depPost(self):
        req_data = r'{"data":[{"dep_id":"合肥001","dep_name":"合肥","master_name":"合肥市长","slogan":"合肥欢迎您"},{"dep_id":"泸州001"}]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400,res.status_code)

    def test10_depPost(self):
        req_data = r'{"data":[{"dep_id":"TRUE","dep_name":"成都","master_name":"成都市长","slogan":"麻辣烫欢迎您"}]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400,res.status_code)

    def test11_depPost(self):
        req_data = r'{"data":[{"dep_id":"兰州","dep_name":"123.456","master_name":"兰州市长","slogan":"手拉面欢迎您"}]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400,res.status_code)

    def test12_depPost(self):
        req_data = r'{"data":[{"dep_id":"西安001","dep_name":"西安","master_name":"FALSE","slogan":"羊肉泡馍欢迎您"}]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400,res.status_code)

    def test13_depPost(self):
        req_data = r'{"data":[{"dep_id":"郑州001","dep_name":"郑州","master_name":"郑州市长","slogan":"345.678"}]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400,res.status_code)

    def test14_depPost(self):
        req_data = r'{"data":[{"dep_id":"石家庄001","dep_name":"石家庄","master_name":"","slogan":"赵子龙欢迎您"}]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400,res.status_code)

    def test15_depPost(self):
        req_data = r'{"data":[{"dep_id":"中国001","dep_name":"长春","master_name":"一汽大众","slogan":"为奥运加油"}]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(201,res.status_code)

    def test16_depPost(self):
        req_data = r'{"data":[{"dep_id":"#杭州01#","dep_name":"西湖01","master_name":"碧螺春","slogan":"法海欢迎您"}]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400,res.status_code)

    def test17_depPost(self):
        req_data = r'{"data":[{"dep_id":"@杭州01@","dep_name":"西湖01","master_name":"碧螺春","slogan":"法海欢迎您"}]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400,res.status_code)

    def test18_depPost(self):
        req_data = r'{"data":[{"dep_id":"%杭州02%","dep_name":"西湖01","master_name":"碧螺春","slogan":"法海欢迎您"}]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400,res.status_code)

    def test19_depPost(self):
        req_data = r'{"data":[{"dep_id":"乌鲁木齐001","dep_name":"乌鲁木齐银川甘肃黄河入海流长江澜沧江北京001","master_name":"乌鲁木齐银川甘肃黄河入海流长江澜沧江北京","slogan":"乌鲁木齐银川甘肃黄河入海流长江澜沧江北京乌鲁木齐银川甘肃黄河入海流长江澜沧江北京乌鲁木齐银川甘肃黄河入海流长江澜"}]}'
        res=requests.post(url,req_data.encode('utf-8'))
        res = requests.post(url, data=req_data.encode('utf-8'), headers=req_head)
        self.assertEqual(400,res.status_code)


if __name__ == '__main__':
    unittest.main()














