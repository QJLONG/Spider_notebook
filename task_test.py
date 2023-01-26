'''
Description: 
Language: UTF-8
Author: hummer
Date: 2023-01-07 18:57:40
'''
from threading import Thread
import time

class Task(Thread):
    def __init__(self, parm=None):
        super().__init__()
        self.parm = parm

    def run(self):
        time.sleep(3)
        self.result = 200

    def get_result(self):
        return f"result:{200}"


if __name__ == '__main__':
    task1 = Task(1)
    task2 = Task(2)
    task1.start()
    task2.start()
    
    