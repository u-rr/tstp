import urllib.request
from urllib.parse import urljoin  # URLを扱うモジュールを追加
from bs4 import BeautifulSoup as BS

class Scraper:
    def __init__(self, site):
        self.site = site
        self.titles = set()  # 収集済みURLを入れておく変数

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = 'html.parser'
        sp = BS(html, parser)
        with open('output.txt', 'w') as f:
            for tag in sp.find_all(class_="article-title"):
                title = tag.get_text()
                if title is None:
                    continue
                # if 'atcl/contents' not in url:  # 'atcl/contents' を含まないURLは対象外にする
                #     continue
                # full_url = urljoin(r.url, url)  # ドメイン名を含むURLに変換
                if title in self.titles:  # 既に収集済みのURLは対象外にする
                    continue
                self.titles.add(title)  # 収集済みURLに追加
                print('\n' + title)  # URLを表示
                f.write(title + "\n")

news = 'https://xtrend.nikkei.com/atcl/contents/new/'  # ニュース取得元サイトを変更
Scraper(news).scrape()
