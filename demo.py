import requests
data = {'username':'sarah',
        'password':'11111'}

url = 'http://127.0.0.1:8000/login/'
def send_post(url,data):
    res = requests.post(url=url,data=data).json()
    return res
print(send_post(url,data))

