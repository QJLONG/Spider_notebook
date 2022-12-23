# target_domain: https://www.dytt89.com/
import re
import requests
import csv


# 获取子链接
def get_href(domain):
    resp = requests.get(domain, verify=False)
    resp.encoding = 'gbk'
    ul_comp = re.compile(r"经典大片.*?<ul>(?P<ul>.*?)</ul>", re.S)
    ul_search = ul_comp.search(resp.text)
    ul_text = ul_search.group("ul")
    url_comp = re.compile(r'''<li><a href='(?P<url>.*?)'.*?《(?P<name>.*?)》.*?</a>''', re.S)
    url_iter = url_comp.finditer(ul_text)
    url_list = []
    for it in url_iter:
        url_list.append(domain + it.group("url").strip("/"))
    return url_list


# 获取子页面内容
def get_info(url):
    resp = requests.get(url, verify=False)
    resp.encoding = 'gbk'
    res_comp = re.compile(r'<div id="downlist".*?<tr>.*?<a href="(?P<download_href>.*?)">', re.S)
    info_search = res_comp.search(resp.text)
    download_link = info_search.group("download_href")
    name_search = re.search(r"=\[电影天堂www.dytt89.com\](?P<name>.*?)&", download_link, re.S)
    dict = {}
    dict["name"] = name_search.group("name")
    dict["link"] = download_link
    return dict


if __name__ == '__main__':
    domain = 'https://www.dytt89.com/'
    url_list = get_href(domain)
    dict_list = []
    for url in url_list:
        dict_list.append(get_info(url))

    f = open("data.csv", "w", encoding='gbk')
    csv_writer = csv.writer(f)
    for dic in dict_list:
        csv_writer.writerow(dic.values())
    f.close()
    print("Over!")
