# target: https://shijiazhuang.zbj.com/search/service/?kw=mysql

import requests
from lxml import etree
import csv
import sys


def get_content(key_word):
    resp = requests.get("https://shijiazhuang.zbj.com/search/service/?kw=" + key_word)
    resp.encoding = 'utf-8'
    f = open(key_word + ".csv", "w", encoding='utf-8')
    csv_writer = csv.writer(f)

    # analysis the html
    html_tree = etree.HTML(resp.text)

    # get divs from the html tree
    divs_list = html_tree.xpath('//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div')

    for div in divs_list:  # process each div
        try:
            price = div.xpath("./div/div[3]/div[1]/span/text()")[0].strip("￥")
            # print(price)
            title = key_word.join(div.xpath("./div/div[3]/a[1]/text()"))
            # print(title)
            company_info = div.xpath("./div[1]/a[1]/div[2]/div[1]/div/text()")[0]
            # print(company_info)
            star = div.xpath("./div[1]/a[1]/div[2]/div[2]/span/text()")[0]
            # print(star)
            csv_writer.writerow([title, price, company_info, star])
        except BaseException as e:
            print("Can't find it!!!")
            sys.exit(0)


def main():
    key_word = input("Please input your keyword which to search:\n")
    get_content(key_word)
    print("Over!!!")


if __name__ == '__main__':
    main()
