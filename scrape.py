import urllib.request, re
html = urllib.request.urlopen('https://news.un.org/en/').read().decode('utf-8')
urls = re.findall(r'https://[^"\s\'>]+\.(?:jpg|jpeg|png)', html)
for u in list(set(urls))[:10]:
    print(u)
