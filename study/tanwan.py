# encoding=utf-8
import requests, json, time, re
from retrying import retry

class Xinxin():
    def __init__(self):
        self.captcha_url = "https://webapi.693975.com/web/index.php?r=login/captcha"
        self.login_url = "https://webapi.693975.com/web/index.php?r=login/login"
        self.logout_url = "https://webapi.693975.com/web/index.php?r=user/out"
        self.user_url = "https://webapi.693975.com/web/index.php?r=user/state"

    def down_captcha(self):
        response = self.request(self.captcha_url)
        cookies = re.search(r"PHPSESSID=(\w+);", response.headers['Set-Cookie']).group(1)
        print("验证码的PHPSESSID=", cookies)
        with open("./captcha.png", 'wb') as f:
            f.write(response.content)

    def login(self, username, password, code):
        login_data = {
            "username": username,
            "password": password,
            "code": code
        }
        response = self.request(self.login_url, login_data)
        cookies = re.search(r"PHPSESSID=(\w+);", response.headers['Set-Cookie']).group(1)
        print("登陆的PHPSESSID=", cookies)
        print(json.loads(response.text))

    def get_user_info(self):
        response = json.loads(self.request(self.user_url).text)
        # print(response.headers)
        print(response)

    def logout(self):
        response = json.loads(self.request(self.logout_url).text)
        print(response)

    @retry(stop_max_attempt_number=3)
    def request(self, url, params = ''):
        session = requests.session()
        response = session.get(url, params=params, timeout=10)
        # print(response.request.headers)
        assert response.status_code == 200
        return response

    def run(self):
        print('*' * 50)
        print('--------webapi 验证码登陆用户信息退出----------\n')
        self.down_captcha()
        username = input("请输入登陆账号\n") or "18819268053"
        password = input("请输入登陆密码\n") or "123456"
        captcha = input("请输入验证码\n")
        self.login(username, password, captcha)
        time.sleep(2)
        self.get_user_info()
        time.sleep(2)
        self.logout()

if __name__ == "__main__":
    xx = Xinxin()
    xx.run()
