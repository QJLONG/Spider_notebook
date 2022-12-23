import requests

resp = requests.get("https://www.ikmeiju.com/play/31780-0-0.html")
print(resp.text)