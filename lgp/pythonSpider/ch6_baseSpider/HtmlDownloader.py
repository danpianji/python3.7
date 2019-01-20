# -*- coding: UTF-8 -*-

import requests

class HtmlDownloader:
    def download(self, url):
        #下载url网页
        if url is None:
            return None
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
        response = requests.get(url, headers=headers)
        if response.status_code!=200:
            return None
        response.encoding('utf-8')
        return response.text
