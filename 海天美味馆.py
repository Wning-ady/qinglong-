"""
new Env("微信小程序-海天美味馆")
cron 0 8 * * *
环境变量名称 wx_htmw_auth = Authorization#uuid
"""
import traceback
from datetime import datetime

import ApiRequest
from notify import send

title = '微信小程序-海天美味馆'
tokenName = 'wx_htmw_auth'


class htmwg(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'cmallapi.haday.cn',
            'Connection': 'keep-alive',
            # 'Content-Length': '41',
            'Content-Type': 'application/json',
            'xweb_xhr': '1',
            'uuid': data.split('#')[1],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a1b) XWEB/9129',
            'envVersion': 'release',
            'Authorization': data.split('#')[0],
            'Referer': 'https://servicewechat.com/wx7a890ea13f50d7b6/595/page-frame.html',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        data = {
            'activity_code': '202404',
            'fill_date': '',
        }
        response = self.sec.post('https://cmallapi.haday.cn/buyer-api/sign/activity/sign', json=data)
        print(response.text)


if __name__ == "__main__":
    ApiRequest.ApiMain(['login']).run(tokenName, htmwg)
