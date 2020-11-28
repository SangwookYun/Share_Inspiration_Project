import json
import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver

regex = re.compile('[\s\r\n]{2,}')
driver = webdriver.Chrome('./chromedriver.exe')  # initiating the webdriver.


class BaseScraping:
    def __call__(self, url):
        driver.get(url)
        time.sleep(5)  # to ensure that the page is loaded
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")  # enables to parse xml, html
        items = soup.find_all("div", {"class": "section"})

        # driver.find_element_by_xpath('//*[@id=trust')
        # driver.find_element_by_xpath('//button[@class="feedback-close-button"]').click()
        driver.find_element_by_xpath('//button[@class="truste-button2"]').click()

        # this is to generate png files for each section
        list_all_sections = driver.find_elements_by_xpath('//*[@id="loioc8145542c2564bb29f6cf2fb6fe67b90"]/div/div')
        idx = 1
        for item in list_all_sections:
            item.screenshot("file_{}.png".format(idx))
            idx += 1

        # this is to generate json file by scrapying the webpage
        idx = 1
        for item in items:
            title = item.find("h2", {"class": "section_title"}).text.strip()
            description = item.find("p", {"class": "p"}).text.strip()
            screenshot_path = './file_{}.png'.format(idx)
            data = {
                "title": title,
                "description": description,
                "screenshot": screenshot_path  # assume it is relative path
            }
            idx += 1
            yield data


if __name__ == '__main__':
    scrap_results = [];
    URL = "https://help.sap.com/viewer/9433604f14ac4ed98908c6d4e7d8c1cc/1905/en-US/c8145542c2564bb29f6cf2fb6fe67b90.html"
    it = BaseScraping()(URL)

    while True:
        try:
            data = next(it)
            scrap_results.append(data)
        except StopIteration:
            break;

    with open("sap_wiki_sangwookYun.json", "w") as outfile:
        json.dump(scrap_results, outfile, indent=2)

    print(f"Completed")
