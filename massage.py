import requests
import json
def gettoken(Secret,corpid): 
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'
    getr = requests.get(url=url.format(corpid,Secret))
    access_token = getr.json().get('access_token')
    print(access_token)
    return access_token
def message(msg,Secret,corpid):
    access_token=gettoken(Secret,corpid)
    data = {
        "touser" : "@all",   # 向这些用户账户发送
        #"toparty" : "pushsever",   # 向这些部门发送
        "msgtype" : "text",
        "agentid" : 1000002,                       # 应用的 id 号
        "text" : {
            "content" : msg
        },
        "safe":0
    }
    r = requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(access_token),
                data=json.dumps(data))
    print(r.json())
