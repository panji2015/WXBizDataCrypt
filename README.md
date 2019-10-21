# WXBizDataCrypt
python for wx data crypt
微信小程序 加密数据的解密方法

## setup
pip install wxdc

## usage
```
from wxdc.WXBizDataCrypt import WXBizDataCrypt  

wx_data = '...'  
wx_iv = '...5R4xc+TQ=='  
wx_session_key = '...jUAGA=='  

APPID = '...'  

pc = WXBizDataCrypt(APPID, wx_session_key)  
print(pc.decrypt(wx_data, wx_iv))  
```

