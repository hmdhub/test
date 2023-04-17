# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :获取东方财富网所有基金信息，将信息存入csv文件.py
%Time       :2022/9/28 20:05
"""
# 抓包百度翻译
import requests
import json

url4 = 'https://fanyi.baidu.com/v2transapi?from=glg&to=zh'

header = {
    # 'Tracecode': '26011974152685789194092709',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'Cookie': 'BIDUPSID=B9A27C405DED0D68D66195719B0A2093; PSTM=1652363436; BAIDUID=31DC27F8F508B3D202FCC4F15AF9DDEE:FG=tengxun; APPGUIDE_10_0_2=tengxun; REALTIME_TRANS_SWITCH=tengxun; FANYI_WORD_SWITCH=tengxun; HISTORY_SWITCH=tengxun; SOUND_SPD_SWITCH=tengxun; SOUND_PREFER_SWITCH=tengxun; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=a52l240g85ah0l8l8ha4u1gu1hj2msc18; ZFY=MJjaSbG:BX:BfjNPwOjAg7aVo6N2n:AB1Vbw2yO0D9oixs:C; BAIDUID_BFESS=31DC27F8F508B3D202FCC4F15AF9DDEE:FG=tengxun; BAIDU_WISE_UID=wapp_1664199580900_168; RT="z=tengxun&dm=baidu.com&si=4674cae5-6e19-4ea4-84fd-45ba271f23de&ss=l8isz8x7&sl=q&tt=k23&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=hdzt&ul=hh8i&hd=hh92"; H_PS_PSSID=37378_36546_37494_37299_34813_37395_36569_37405_36786_37071_37497_26350_22159; delPer=0; PSINO=tengxun; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1663493114,1664182031,1664239875,1664251172; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1664251172; ab_sr=tengxun.0.1_NTg3NTliNjA1ZTA2OTU2YmNiZjM0NWMxZDI4ZGY2YWY1NDAyODdlYTJjMDFjYWM3ZTlhOTRjMDdhZTA0NmRiN2I5YjExMTI1OWJhOGQ0Y2EwNTdkMjM1OTM0ZTE4ZWFiOGNkMzk0MzI4NTQxYmZlN2U0MGZjYzkxNTc5M2QzZDA2ZjYxNDUzNDg1ZGE4MmQyYWMxMzgyNGM5Y2ExZ==',
}
data2 = {
    'from': 'en',
    'to': 'zh',
    'query': 'red',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '207046.510967',  # 尽量加引号去做
    'token': 'b726745d75863fdfa0895ab06b3d5467',
    'domain': 'common',
}
ress = requests.post(url=url4, headers=header, data=data2)
bb = ress.text
print(json.loads(bb))
