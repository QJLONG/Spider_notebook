'''
Description: 实现搜索功能
Language: UTF-8
Author: hummer
Date: 2023-01-19 17:48:33
'''
import requests 
from threading import Thread
from bs4 import BeautifulSoup


class NovSearch(Thread):

    def __init__(self, title="斗罗大陆"):
        Thread.__init__(self)
        self.title = title
        self.url = "http://www.mbiqukan.com/search/?searchkey="  # http://www.mbiqukan.com/search/?searchkey=

    def getSearchPage(self):
        self.result = []
        for i in range(5):
            res_url = self.url + self.title + "&page=" + str(i+1) 
            resp = requests.get(self.url)
            soup = BeautifulSoup(resp.text, "html.parser")
            div = soup.find("div", attrs={"class": "content"})
            for dl in div.find_all("dl"):
                nov_name = dl.a.attrs["title"]
                author = dl.find_all("dd")[1].a.text
                self.result.append({nov_name: author})
        return self.result
    
    def run(self):
        res = self.getSearchPage()
        print(res)
        return res
        
    
if __name__ == "__main__":
    sea = NovSearch()
    print(sea.getSearchPage())