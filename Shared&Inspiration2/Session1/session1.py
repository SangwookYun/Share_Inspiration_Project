import requests
import re
from bs4 import BeautifulSoup

regex = re.compile('[\s\r\n]{2,}')


class BaseScraping:
    def __call__(self, url):
        res = requests.get(url)
        soup = BeautifulSoup(res.content, "lxml")  # enables to parse xml, html
        print(soup)
        items = soup.find_all("div", {"class": "category-listing"})
        for item in items:
            title = item.find("h3", {"class": "article-title"}).text.strip()
            summary = item.find("p", {"class": "teaser-text"}).text.strip()
            yield {
                'title': title,
                "summary": summary
            }


if __name__ == '__main__':
    URL = "https://www.itworldcanada.com/tag/cybersecurity"

    # base_scraping = BaseScraping();
    it = BaseScraping()(URL)
    while True:
        try:
            data = next(it)
            print(f"data: {data}")
        except StopIteration:
            break;

    print(f"Completed")
