# -*- coding：utf-8-*-

import requests

url = "http://openapi.tuling123.com/openapi/api/v2"
data = {
    "reqType": 0,
    "perception": {
        "inputText": {
            "text": "附近的酒店"
        },
        "inputImage": {
            "url": "imageUrl"
        },
        "selfInfo": {
            "location": {
                "city": "北京",
                "province": "北京",
                "street": "信息路"
            }
        }
    },
    "userInfo": {
        "apiKey": "ec961279f453459b9248f0aeb6600bbe",
        "userId": "206379"
    }
}
res = requests.post(url=url, json=data)    # JSON格式的请求，将数据赋给json参数
print(res.text)