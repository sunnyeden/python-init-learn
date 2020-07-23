#### selenium使用

```python
# encoding = utf-8
from selenium import webdriver

# 实例化一个浏览器
driver = webdriver.Chrome()

# 设置窗口大小
driver.set_window_size(1920, 1080)

# 或者最大化窗口
driver.maximize_window()

# 发送请求
driver.get("https://www.tanwan.com")

# 元素定位方法
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()

# 截屏
driver.save_screenshot("./tanwan.png")

# 获取cookie
cookies = driver.get_cookies()
print(cookies)

# 获取html字符串
driver.page_source

# 查看当前请求地址
driver.current_url

# 退出当前页
driver.close()

# 退出浏览器
driver.quit()
```

#### 获取定位方法的使用

```python
# encoding = utf-8
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.tanwan.com")

ret = driver.find_elements_by_xpath('//*[@id="slideBox"]/div[2]/div/ul/li[1]/p')

# 是个element对象
print(ret)
for p in ret:
    print(p.find_element_by_xpath(".//a").get_attribute("href"), p.find_element_by_xpath(".//b").text, p.find_element_by_xpath(".//span").text)


driver.quit()
```

#### 切换到iframe

```python
driver.swith_to.frame("id|name|element")

driver.switch_to_frame("id|name|element") # 已经过时
```
