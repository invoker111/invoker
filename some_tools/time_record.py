import time
import datetime


class Timer(object):
    def __init__(self):
        self.start = 0
        self.for_start = 0
        self.end = 0
        self.for_end = 0
        self.pause = 1

    def began(self):
        self.start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def get(self, how):
        self.end = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.for_start = datetime.datetime.strptime(self.start, '%Y-%m-%d %H:%M:%S')
        self.for_end = datetime.datetime.strptime(self.end, '%Y-%m-%d %H:%M:%S')
        second = (self.for_end - self.for_start).seconds
        if how == 'second':
            return str(second)
        elif how == 'minute':
            return '%d:%d' % (second // 60, second % 60)

