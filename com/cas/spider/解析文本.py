import requests
import json
import sys
import io
import os

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'll="118318"; bid=VphkMecYUeI; __yadk_uid=RmReW2rcZ2z0mvK7XU2Hk5lbJRkh9Xmt; viewed="1140457"; gr_user_id=06ee0f44-322d-4247-93ac-de144da52338; _vwo_uuid_v2=DC05E55FE4B8188FEF5DD65F5152BE5D2|7eed6e6d696f6c06984eef171f438b14; __utmz=30149280.1576832766.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=30149280; dbcl2="2241899:Qr3KzLK8mY4"; push_doumail_num=0; push_noty_num=0; __utmv=30149280.224; ck=QxRM; douban-fav-remind=1; __gads=ID=c2c2b4d1b545c075:T=1576833631:S=ALNI_ManfN_EbMMtHwjeyAGIuRlVSkk3kw; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.426358312.1576832766.1576840609.1576845825.3; __utmt=1; loc-last-index-location-id="118318"; _pk_id.100001.8cb4=9fac3e30c5487d2c.1576832764.3.1576845892.1576840608.; __utmb=30149280.8.10.1576845825',
    'Host': 'www.douban.com',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

def download(picPath, src, id):
    # 路径不存在则创建
    if not os.path.exists(picPath):
        os.mkdir(picPath)
    # 路径不是目录则创建
    if not os.path.isdir(picPath):
        os.madir(picPath)
    dir = picPath + '/' + str(id) + '.jpg'
    print(src)
    try:
        pic = requests.get(src)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('Sorrry,image cannot downloaded, url is error{}.'.format(src))

def query_img(query, downloadUrl, headers):
    realUrl = downloadUrl.format(query)
    print(realUrl)
    response = requests.get(realUrl, headers=headers, timeout=30)
    respJson = json.loads(response.text, encoding='utf-8')
    picPath = '//Users//xianglong//IdeaProjects//cas-python//img'
    for image in respJson['images']:
        download(picPath, image['src'], image['id'])

if __name__ == '__main__':
    query = '李孝利'
    url = 'https://www.douban.com/j/search_photo?q=\'{}\'&limit=20&start=0'
    query_img(query,url,headers)
