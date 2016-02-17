__author__ = 'Kirill'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from grail import BaseTest
import ConfigParser
import os

page_elements = {"/": ['#get_started_button_top'],
                 "/features": ['#features_page_image_right>img'],
                 "/pricing": ['.billed-annually'], "/why-we-blaze": ['#we_blaze_top_image>p'],
                 "/blog": ['.field-content>a'], "/performance": ['.pub_category>a[href$="616"]'],
                 "/blogs-on-author/669": ['.new-blog-author-linkedin[href$=dmitritikhanski]'],
                 "/blog/how-run-external-commands-and-programs-locally-and-remotely-jmeter":
                     ['.new_blog_get_started_button'], "/search/node/test%20type%3Ablog":
                     ['#main__content--responsive>h2>span'], "/support": ['#search_button_support_page'],
                 "/about": ['[href$=alongirmonsky]'], "/customers": ['[href$=ticketfly]'],
                 "/partners": ['#become-partner'], "/join-our-team": ['.job-expander'],
                 "/usecases": ['#f1'], "/personas?devops": ['#devops>img'], "/personas?perfomance":
                     ['#perfomance>img'], "/contact-us": ['a[href$=tab-1]'], "/terms-service":
                     ['.field-item.even>h2'], "/privacy-policy": ['.field-item.even>h2'],
                 "/third-party-licences": ['.field-item.even>h2']}

config = ConfigParser.RawConfigParser()


class SiteTest(BaseTest):
    global driver

    @classmethod
    def setUpClass(cls):
        path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__))))
        mobile_emulation = {"deviceName": "Apple iPhone 4"}
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        config.read(os.path.join(path, 'settings.properties'))
        cls.url = config.get('urlSection', 'site_url')
        driver_param = config.get('BrowserSection', 'browser')
        if driver_param.__eq__("Chrome"):
            cls.driver = webdriver.Chrome()
            cls.driver.implicitly_wait(30)
            cls.driver.set_window_size(1920, 1080)
        elif driver_param.__eq__("iPhone4"):
             cls.driver = webdriver.Chrome(chrome_options=chrome_options)
             cls.driver.implicitly_wait(30)
             page_elements["/"] = ['#top_button']
        elif driver_param.__eq__("Firefox"):
            cls.driver = webdriver.Firefox()
            cls.driver.implicitly_wait(30)
            cls.driver.set_window_size(1920, 1080)

    def test_over_(self):
        self.over_check(self.driver)

    def over_check(self, driver):
        for url in page_elements.keys():
            driver.get(self.url + url)
            for element in page_elements.get(url):
                driver.find_element(By.CSS_SELECTOR, element).is_displayed(), "Element is absent on the page"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
