# WXBizDataCrypt
python for wx data crypt
微信小程序 加密数据的解密方法

## setup
pip install wxdc

## usage
"""
from wxdc.WXBizDataCrypt import WXBizDataCrypt  

wx_data = 'KuUhCf+tlCOdYw5JASgFHpHv/fKWnJYgp73zaUAJkUqxeXZJrXYgVtLOhdNwQSaHSsItZ7xY/UdNvLOElredtmHVOkxssMycImz3GYjKhcp4hc6gIJLnl0fet/ddbWri/PGLMt4WGTx/t9WXhYYHqSWPCGI8pAioffKjPiL163kFxyjjv0L9rFWRSoKdf9mTutMdRfty31vvrGMR7dBJ23q4rnOAA6E2CizISap8FISNcNQkjB3VKsZz8QphkyBnwyRt9pz49md8HLUb/PJIYyV3rE0myXQ/y359dsHvpnzL5dlfVkR1cPzXQx5xGGIFwQ6rMvn72p8AP5pTPwTr5k3AUFbz/IwclSXuYSzSmi6iH6L7Js5CRXCZR3hYaGrQ9C0233XUtdBj5v8niOSoiexYFlruc/Le15rAa/Y2id/ATJYptFDhbSQviZiaw6QqAIBUrakgEeWhi6VxcuehcNMu4nmLi1ysdMeFM1qIrxct85Bakcghra9hSCFA6zTl'  
wx_iv = '91Z6VGlI6l54pA5R4xc+TQ=='  
wx_session_key = 'UCfDhXrHGYeAuHPQYjUAGA=='  

APPID = '...'  

pc = WXBizDataCrypt(APPID, wx_session_key)  
print(pc.decrypt(wx_data, wx_iv))  
"""

