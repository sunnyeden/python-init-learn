# encoding = utf-8
import requests, time

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

# 设置请求参数
params = {
    "who": "felix",
    "time": time.time()
}

# 设置代理
proxies = {
    "http": "http://12.34.56.79:9527",
    "https": "https://12.34.56.79:9527"
}

response = requests.get("https://www.tanwan.com", headers=headers, params=params, proxies=proxies)

# 响应头
print(response.headers)

# 请求头
print(response.request.headers)

# 请求的url
print(response.request.url)

# 请求状态
assert response.status_code == 200

# 请求内容
print(response.text)