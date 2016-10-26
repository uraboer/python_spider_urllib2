#coding:utf-8
from baike_spider import html_downloader
from baike_spider import html_outputer
from baike_spider import html_parser
from baike_spider import url_manager


class SpiderMain(object):
    def __init__(self):  #初始化
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count=1
        self.urls.add_new_url(root_url) #入口url添加管理器
        while self.urls.has_new_url(): #开启循环
            try:
                new_url=self.urls.get_new_url()

                print 'craw %d : %s' %(count,new_url)

                html_cont=self.downloader.download(new_url) #下载页面
                new_urls,new_data=self.parser.parse(new_url,html_cont) #解析数据
                self.urls.add_new_urls(new_urls) #将新url补充进管理器
                self.outputer.collect_data(new_urls) #收集数据

                if count ==1000:
                    break
                count =count +1
            except:
                print 'craw failed'

        self.outputer.output_html()


if __name__=="__main__":
    root_url="http://baike.baidu.com/view/21087.html"
    obj_spider=SpiderMain() #主入口
    obj_spider.craw(root_url) #启动爬虫





