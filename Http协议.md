#### http协议

* 浏览器访问服务器协议的一种规范

* 基于tcp

#### 请求头

```http
GET / HTTP/1.1
Host: 127.0.0.1:8080
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
```

#### 响应头

```http
Accept-Ranges: bytes
Cache-Control: max-age=864000
Connection: keep-alive
Content-Encoding: gzip
Content-Length: 1133
Content-Type: application/javascript;charset=utf-8
Date: Tue, 28 Jul 2020 02:02:54 GMT
Expires: Fri, 07 Aug 2020 02:02:53 GMT
Last-Modified: Tue, 16 Jun 2020 06:16:33 GMT
Server: NWS_TCloud_S1
X-Cache-Lookup: Hit From Disktank3 Gz
X-Cache-Lookup: Hit From Inner Cluster
X-Daa-Tunnel: hop_count=1
X-NWS-LOG-UUID: 55c3e7c3-891f-4eee-972c-f1560e23609b
```

#### web服务器实现待深入

#### 网络通信


##### tcp-ip协议族

* 互联网协议包含了上百种协议标准，但是最重要的两个协议是TCP和IP协议，所以简称TCP/IP协议族

* 应用层、传输层、网际层[网络层]、网络接口层[链路层]

##### OSI标准

* 包括应用层、表示层、会话层、传输层、网络层、数据链路层、物理层

##### 获取mac地址、物理地址 [中间人攻击原理]

```
arp -a
```

##### 浏览器访问服务器的过程

* DNS解析域名

* tcp的3次握手,建立连接

* 发送请求

* 分析请求，返回数据

* 显示页面