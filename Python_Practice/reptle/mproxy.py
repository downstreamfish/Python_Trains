import urllib.request

url = "http://whatismyip.com.tw"
proxy_support = urllib.request.ProxyHandler({'http':'183.159.93.12'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

print(html)
