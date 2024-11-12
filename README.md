## 修改于：[Joshua-auhsoj/SouthPlusQianDaoOrginal](https://github.com/Joshua-auhsoj/SouthPlusQianDaoOrginal)

- 将 API 获取改成了简单、粗暴、无脑的 WebDriver。
- 在 **Settings** 中设置好 **COOKIE**（需要 JSON 格式的 cookie）和 **serverKey**（server 酱，如果不知道可以谷歌一下）。
- 运行 Action 即可。
- cookies的格式(按这个格式创建COOKIE变量的值)：
```
[

    {
        "domain": "www.south-plus.net",
        "expiry": 填写对应的时间戳,
        "httpOnly": true,
        "name": "eb9e6_winduser",
        "path": "/",
        "sameSite": "Lax",
        "secure": false,
        "value": "填写自己账号的值"
    },
    {
        "domain": "www.south-plus.net",
        "expiry": 填写对应的时间戳,
        "httpOnly": true,
        "name": "eb9e6_cknum",
        "path": "/",
        "sameSite": "Lax",
        "secure": false,
        "value": "填写自己账号的值"
    }
]
```
![alt text](image.png)
### 本地构建要求

请确保安装了 Chrome 和对应版本的 ChromeDriver。

经过测试得出，cookies只需要eb9e6_winduser与eb9e6_cknum两个即可，其他可以删除。有效期是一年。
