import requests

target = "https://fanyi.baidu.com/sug"
word = ""
while True:
    word = input("Please input your word:\n")
    if word == "-1":
        print("Process has been terminated.\n")
        break
    dat = {
        "kw": word
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }

    resp = requests.post(url=target, data=dat, headers=headers)
    solution = resp.json()["data"][0]
    print(f'{solution["k"]}:{solution["v"]}\n')


