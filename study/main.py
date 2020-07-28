# coding=utf-8
from selenium import webdriver

# 配置请求代理参数
PROXY = "http://42.51.13.69:16817"
# 复制一份配置文件
desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()
# 改变配置文件的复制版本.
desired_capabilities['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "noProxy": None,
    "proxyType": "MANUAL",
    "class": "org.openqa.selenium.Proxy",
    "autodetect": False
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("window-size=1024,768")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=desired_capabilities)

driver.get('https://pv.sohu.com/cityjson')
# driver.find_element_by_id('kw').send_keys('ip')
# driver.find_element_by_id('su').click()
