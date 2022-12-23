import requests

target_url = "https://user.17k.com/ck/user/login"

# resp = requests.get(target_url)
# resp.encoding = 'utf-8'# print(resp.text)

# Create a session:
session = requests.session()

# Login:
data = {
	"loginName": "18632443632",
	"password": "zxfspx32148649."
}
resp = session.post(target_url, data=data)
# View Cookies:
# print(resp.cookies)

resp = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
resp.encoding =  'utf-8'
print(resp.text)
