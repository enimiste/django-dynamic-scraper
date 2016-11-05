__author__ = 'elbachirnouni'

from scrapy.http import HtmlResponse
from selenium import webdriver
from os.path import realpath, dirname
import logging
from seleniums import WebDriverWait


class JSMiddleware(object):
    def process_request(self, request, spider):
        if request.meta.get('js'):  # you probably want a conditional trigger
            spider.log('Using PhantomJs', logging.INFO)
            self.driver = webdriver.PhantomJS(realpath(dirname(__file__) + '/../phantomjs211/bin/phantomjs'))
            self.driver.set_window_size(1120, 550)
            WebDriverWait(self.driver, spider.phantomjs_wait).timout()  # 20 sec
            self.driver.get(request.url)
            body = self.driver.page_source
            return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)
        return
