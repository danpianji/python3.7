import urllib.request

response = urllib.request.urlopen("http://zhizhu.com")
data = response.read()
print (data)