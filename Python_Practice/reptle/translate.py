import urllib.request
import urllib.parse
import json
import time

while True:
    contents = input("请输入要翻译的文本: ")
    if contents == 'q':
        break
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    '''
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    '''
    data = {}
    data['i'] = contents
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1525422846755'
    data['sign'] = '1fcfbc1f630604161d8f136989c120c9'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'

    data = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data)

    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
    response = urllib.request.urlopen(req)

    html = response.read().decode('utf-8')

    target = json.loads(html)
    print('你想翻译的:{}'.format(target['translateResult'][0][0]['src']))
    print('翻译的结果是: {}'.format(target['translateResult'][0][0]['tgt']))

    '''
    print(html)
    '''
    time.sleep(5)
