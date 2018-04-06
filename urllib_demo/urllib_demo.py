import urllib.request
import urllib.parse

req = urllib.request.urlopen("https://www.google.com")

print(req.read())

url = 'https://www.google.pl/search'
values = {'q':'python tutorials pl'}

data = urllib.parse.urlencode(values)
print(data)
data = data.encode('utf-8')
print(data)
print(req)
resp = urllib.request.urlopen(req)
print(resp)
resp_data = resp.read()
print(resp_data)


headers = {}
headers['User_Agent'] = "Mozilla/5.0 (X11; Linux i686)"

req = urllib.request.Request(url, headers = headers)
print(req)
resp = urllib.request.urlopen(req)
print(resp)
resp_data = resp.read()
print(resp_data)
