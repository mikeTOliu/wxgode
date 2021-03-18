import requests,json
def GateGodeData(apikey,no):
    url="https://api.jisuapi.com/gold/shgold?appkey="+apikey
    r=requests.get(url)
    hgodedata=''
    godejson=r.json()
    hgode=godejson['result'][no]
    for key in hgode:
        hgodedata=hgodedata+(key+":"+hgode[key])+"\n"
    print(hgodedata)
    return hgodedata
