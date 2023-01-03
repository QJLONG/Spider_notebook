#-*- coding: UTF-8 -*_
import requests
from contextlib import closing

class ProgressBar(object):
    def __init__(self, title, count=0.0, run_status=None, fin_status=None, total=100.0, unit='', sep='/', chunk_size=1.0):
        super(ProgressBar, self).__init__()
        self.info = "[%s] %s %.2f %s %s %.2f %s"
        self.title = title
        self.total = total
        self.count = count
        self.chunk_size = chunk_size
        self.status = run_status or ""
        self.fin_status = fin_status or ""
        self.unit = unit
        self.sep = sep

    # 函数名前加两个下划线表示函数为内置函数，在类的内部会自动重命名为_ClassName__FunctionName
    # 这样做的目的是为了防止子类对其进行重写
    def __get_info(self):
        # [名称] 状态 进度 单位 分割线 总数 单位
        # 变量前加一个下划线用于警告说明这是一个私有变量，外部类不要去访问它。但实际上，外部类还是可以访问到这个变量。
        _info = self.info % (self.title, self.status, self.count/self.chunk_size, self.unit, self.sep, self.total/self.chunk_size, self.unit)
        return _info

    def refresh(self, count=1, status=None):
        self.count += count
        self.status = status or self.status
        end_str = "\r"
        if self.count >= self.total:
            end_str = '\n'
            self.status = status or self.fin_status
        print(self.__get_info(), end=end_str)


if __name__ == '__main__':
    print('*' * 100)
    print('\t\t\t\t欢迎使用文件下载小助手')
    print('*' * 100)
    url = input("请输入需要下载的文件连接:\n")
    filename = url.split('/')[-1]
    parm = filename.split("?")[-1]
    filename = filename.replace("?"+parm, "")
    with closing(requests.get(url, stream=True)) as response:
        chunk_size = 1024
        content_size = int(response.headers['content-length'])
        if response.status_code == 200:
            print('文件大小:%0.2f KB' % (content_size / chunk_size))
            progress = ProgressBar("%s下载进度" % filename,
                                    total = content_size,
                                    unit = "KB",
                                    chunk_size = chunk_size,
                                    run_status = "正在下载",
                                    fin_status = "下载完成")
            with open(filename, "wb") as file:
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    progress.refresh(count=len(data))
        else:
            print("链接异常")

            


# p = ProgressBar("123")
# print(dir(p))
