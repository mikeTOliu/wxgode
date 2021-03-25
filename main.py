from massage import message
from gode import GateGodeData
import time
apikey="*******"
no=3
Secret = "******"
corpid = '******'

flage=0
def __main__():
    hgode=GateGodeData(apikey,no)
    pr=(hgode['price'])
    price=float(pr)
    if price<340:
        hgodedata=makestr(hgode)
        message(hgodedata,Secret,corpid)
        flage=1
    print("价格",price)
    print("时间",time.localtime().tm_hour, "；",time.localtime().tm_min)
def makestr(hgode):
    hgodedata=''
    for key in hgode:
            hgodedata=hgodedata+(key+":"+hgode[key])+"\n"
    #print(hgodedata)
    return hgodedata

while flage==0:
    if time.localtime().tm_hour==0 and time.localtime().tm_min<14:
        flage=0
    __main__()
    time.sleep(900)