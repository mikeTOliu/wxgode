import requests,json
def GateGodeData(apikey,no):
    url="https://api.jisuapi.com/gold/shgold?appkey="+apikey
    r=requests.get(url)
    godejson=r.json()
    hgode=godejson['result'][no]
    return hgode
