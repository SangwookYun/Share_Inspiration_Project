import scrapy


class ReviewSpider(scrapy.Spider):
    name = "SAPSAC"

    def start_requests(self):
        urls = ['https://www.trustradius.com/products/sap-analytics-cloud/reviews?qs=pros-and-cons']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # review title
        # // *[ @ id = "product_reviews"] / div / section / div[2] / div[1] / article / div[2] / h3 / a
        # // *[ @ id = "product_reviews"] / div / section / div[2] / div[2] / article / div[2] / h3 / a
        # // *[ @ id = "product_reviews"] / div / section / div[2] / div[3] / article / div[2] / h3 / a
        # review score
        # // *[ @ id = "product_reviews"]/div/section/div[2]/div[1]/article/div[2]/div[2]/div[1]/div[2]/span[2]
        # review pros
        # // *[ @ id = "question-5ed5410f398b8c00308423b8-response-body"] / div / div[1] / ul
        # review cons
        # // *[ @ id = "question-5ed5410f398b8c00308423b8-response-body"] / div / div[3] / ul

        all_listings = response.xpath('//*[@id="product_reviews"]/div/section/div/div/article')
        for item in all_listings:
            pros_list = []
            cons_list = []
            score = item.xpath('div[2]/div[2]/div[1]/div[2]/span[2]/text()').get().replace(' out of 10', '')
            pros = item.xpath('div/div/div/div/div/div/div/div[1]/ul/li//div[2]/text()')
            cons = item.xpath('div/div/div/div/div/div/div/div[3]/ul/li//div[2]/text()')

            for comment in pros:
                pros_list.append(comment.get())

            for comment in cons:
                cons_list.append(comment.get())

            if len(pros_list) == 0 & len(cons_list) == 0:
                yield None
            else:
                data = {
                    'score': int(score),
                    'pros': pros_list,
                    'cons': cons_list
                }
                yield data
