""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/9/28 9:18
file :下午篇1.PY
"""""
import  requests
# 百度贴吧案例加分页
def tieba(url,begin_page,end_page):
    for page in range(begin_page,end_page+1):
        pn = (page-1)*50
        file_name = "第" +str(page) +"页.html"
        full_url = url +'&pn='+str(pn)
        html = load_page(full_url,file_name)
        write_page(html,file_name)
def load_page(url,file_name):
    headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    return response.text
def write_page(html,filename):
    with open(filename,mode = 'w+',encoding="utf-8") as file:
        file.write(html)
if __name__ == '__main__':
    kw = input("请输入你要搜索的贴吧名")
    begin_page = int(input('请输入起始页'))
    end_page = int(input('请输入结束页'))
    url = 'http://tieba.baidu.com/f?'
    # key = {'kw': kw}
    url = url + kw
    tieba(url,begin_page,end_page)