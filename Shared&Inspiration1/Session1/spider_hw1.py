import scrapy


class ReviewSpider(scrapy.Spider):
    name = "HOMEWORK"

    def start_requests(self):
        url_1 = ['https://www.itworldcanada.com/tag/cybersecurity']
        url_2 = ['https://cybersecuritynews.com/tag/malware/']

        for i in range(10):
            print(url_1[0] + '/page/' + str(i + 1))
            url_1.append(url_1[0] + '/page/' + str(i + 1))

        for url in url_1:
            yield scrapy.Request(url=url, callback=self.parse_cyber_security)

        for i in range(4):
            print(url_2[0] + '/page/' + str(i + 1))
            url_2.append(url_2[0] + '/page/' + str(i + 1))

        for url in url_2:
            yield scrapy.Request(url=url, callback=self.parse_malware)

    def parse_cyber_security(self, response):
        all_listings = response.xpath('//*[@id = "content"]/div/div')
        for item in all_listings:
            title = item.xpath('h3/a/text()').get()
            summary = item.xpath('p/text()').get()
            time_article = item.xpath('span / span[1]/text()').get()

            if title == None:
                yield None

            else:
                data = {
                    'title': title,
                    'summary': summary,
                    'time': time_article,
                    "category": "cyberSecurity"
                }
                yield data

    def parse_malware(self, response):
        all_listings = response.xpath('//*[ @ id = "td-outer-wrap"]/div/div/div/div/div/div/div/div/div')
        for item in all_listings:
            title = item.xpath('h3/a/text()').get()
            time_article = item.xpath('div / span/time/text()').get()

            if title == None:
                yield None

            else:
                data = {
                    'title': title,
                    'time': time_article,
                    "category": "malware"
                }
                yield data
