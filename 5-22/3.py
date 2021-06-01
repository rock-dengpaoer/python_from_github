from time import time
from threading import Thread

import requests


class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/Hao' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    resp = requests.get('http://api.tianapi.com/txapi/aqi/index?key=&area=上海')
    data_model = resp.json()
    # for mm_dict in data_model['newslist']:
    #     url = mm_dict['picUrl']
    #     DownloadHanlder(url).start()
    print(data_model)


if __name__ == '__main__':
    main()