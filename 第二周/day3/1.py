# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上午上课笔记.py
%Time       :2022/9/28 11:02
"""
import requests
import json
# GET带传参的方法






url2 = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
'Cookie': 'BIDUPSID=D739101F09792253CA80F8E5120348D7; PSTM=1649995524; BAIDUID=D739101F09792253790567986E524422:FG=1; BAIDUID_BFESS=D739101F09792253790567986E524422:FG=1; ZFY=IUHbpcTikSeyGHVKn2Wtx:AohkLMmOvRvGQ:AAmINZsy4:C; BA_HECTOR=0105a5210l2k2kahahah825t1hj75o81b; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_PS_PSSID=37374_36554_37361_37300_36885_34812_37486_37398_36569_37406_36786_37500_26350_37489_37372_37450; delPer=0; PSINO=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1664325414,1664333556; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1664333601; ab_sr=1.0.1_MzAzZGY4MjA0MWE4OGE4Mzc5Y2M3MmM2N2ZiMDAzMGU0ZjY1Mzk5MDE2N2RiMzQyMWYyNzI0MmFjNDM3YjIwMGQ2YTc5YzljMTliNGQ3M2IyMTU1ZDc4MWQwMGMyY2FlZTQxN2UzZWRmNjQ2MTMwMjRmNmMwYzQxNjMyNzFlMmNlNGE1NzE4ODg5ODkwMjdmZDEyMjg2MzMxOWQ0MTM4MA=='
}
date = {
'from': 'en',
'to': 'zh',
'query': 'do',
'transtype': 'realtime',
'simple_means_flag': 3,
'sign': 602137.906024,
'token': 'a5973ea3138352d0aeacbb4614a2f02c',
'domain': 'common'
}
res = requests.post(url=url2,headers=header,data=date)
aa = res.text
print(json.loads(aa))


# 设置代理
