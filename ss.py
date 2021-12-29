import http.client
conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
s = conn.getresponse().read()
s = str(s)
print(s[2:-1])