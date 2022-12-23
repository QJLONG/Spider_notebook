# target: https://movie.douban.com/top250
import requests
import re
import csv


class DB250:
    def __init__(self):
        self.url = 'https://movie.douban.com/top250?start=0'
        self.num = 100
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                          "Chrome/106.0.0.0 Safari/537.36 "

    def get_content(self):
        headers = {
            "User-Agent": self.user_agent
        }
        if self.num % 25 == 0:
            pages = self.num / 25
        else:
            pages = self.num // 25 + 1

        comp = re.compile(r'<li>.*?<div class="item">.*?<em class="">(?P<id>\d+)</em>'
                          r'.*?<span class="title">(?P<name>.*?)</span>.*?<div class="bd">'
                          r'.*?<br>.*?(?P<time>\d+)&nbsp.*?<div class="star">.*?'
                          r'<span class="rating_num" property="v:average">(?P<star>.*?)</span>'
                          r'.*?<span>(?P<num>\d+)人评价</span>', re.S)

        result = []
        for i in range(int(pages)):
            resp = requests.get(self.url, headers=headers)
            resp.encoding = 'utf-8'
            its = comp.finditer(resp.text)
            for it in its:
                # print(it.group("id"))
                # print(it.group("name"))
                # print(it.group("time"))
                # print(it.group("star"))
                # print(it.group("num"))
                res_dict = it.groupdict()
                res_dict["id"] = int(res_dict["id"]) + i*25
                result.append(res_dict)
        return result


if __name__ == '__main__':
    solution = DB250()
    dicts = solution.get_content()
    f = open("data.csv", mode="w", encoding="utf-8")
    csv_writer = csv.writer(f)
    for dic in dicts:
        print(dic)
        csv_writer.writerow(dic.values())
        break




