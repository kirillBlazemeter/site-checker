__author__ = 'Kirill'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from grail import BaseTest
import sys

page_elements = {"/": ['#try_it_now>a', 'TRY IT NOW'],
                 "/features": ['#features_page_text_left>h3', '100% Compatible with JMeter'],
                 "/pricing": ['.billed-annually', '1 Year (discounted)'],
                 "/why-we-blaze": ['#we_blaze_top_image>p', 'Performance testing has changed.'],
                 "/blog": ['.more-link', 'Read more...'],
                 "/performance": ['.pub_category>a[href$="616"]', 'Performance Testing'],
                 "/blogs-on-author/669": ['.blog_author_block>p>a', 'Dmitri Tikhanski'],
                 "/blog/view-webcast-load-testing-bootcamp":
                     ['.block-title', 'You might also find these useful:'], "/search/node/test%20type%3Ablog":
                     ['#main__content--responsive>h2', 'Search Results for'], "/support":
                     ['#support_opacity_layer>p', 'We\'re here to ensure your success.'],
                 "/about": ['.leader_info>h1', 'Alon Girmonsky'], "/customers": ['[href$=ticketfly]', 'READ MORE'],
                 "/partners": ['.region.region-content-left>h2', 'ECOSYSTEMS'],
                 "/join-our-team": ['.view-content>h3', 'DEVELOPMENT'],
                 "/usecases": ['#f1', 'PERFORMANCE TESTING'], "/personas?devops": ['.personas_info>h1>span', 'Frank'],
                 "/contact-us": ['a[href$=tab-1]', 'SALES'], "/terms-service":
                     ['.field-item.even>h2', 'BLAZEMETER TERMS OF USE'],
                 "/privacy-policy": ['.field-item.even>h2', 'BLAZEMETER PRIVACY POLICY'],
                 "/third-party-licences": ['.field-item.even>h2', "Software License Acknowledgements"]}

driver_param = ''


class SiteTest(BaseTest):
    def test(self):

        if sys.argv[1].__eq__('prod'):
            self.main_url = "https://blazemeter.com"
        elif sys.argv[1].__eq__('qa'):
            self.main_url = "https://wwwqa.blazemeter.com"
        elif sys.argv[1].__eq__('dev'):
            self.main_url = "https://wwwdev.blazemeter.com"
        else:
            self.main_url = "https://wwwqa.blazemeter.com"
        for i in range(2, len(sys.argv)):
            driver_param = sys.argv[i]
            if driver_param.__eq__("Chrome"):
                self.driver = webdriver.Chrome()
                self.driver.implicitly_wait(30)
                self.driver.set_window_size(1920, 1080)
                page_elements["/"] = ['#try_it_now>a', 'TRY IT NOW']
            elif driver_param.__eq__("iPhone4"):
                mobile_emulation = {"deviceName": "Apple iPhone 4"}
                chrome_options = Options()
                chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
                self.driver = webdriver.Chrome(chrome_options=chrome_options)
                self.driver.implicitly_wait(30)
                page_elements["/"] = ['#mobile_version_try_it_now', 'TRY IT NOW']
            elif driver_param.__eq__("iPhone5"):
                mobile_emulation = {"deviceName": "Apple iPhone 5"}
                chrome_options = Options()
                chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
                self.driver = webdriver.Chrome(chrome_options=chrome_options)
                self.driver.implicitly_wait(30)
                page_elements["/"] = ['#mobile_version_try_it_now', 'TRY IT NOW']
            elif driver_param.__eq__("Firefox"):
                self.driver = webdriver.Firefox()
                self.driver.implicitly_wait(30)
                self.driver.set_window_size(1920, 1080)
                page_elements["/"] = ['#try_it_now>a', 'TRY IT NOW']
            elif driver_param.__eq__("Nexus7"):
                mobile_emulation = {"deviceName": "Google Nexus 7"}
                chrome_options = Options()
                chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
                self.driver = webdriver.Chrome(chrome_options=chrome_options)
                self.driver.implicitly_wait(30)
                page_elements["/"] = ['#mobile_version_try_it_now', 'TRY IT NOW']
            else:
                self.driver = webdriver.Firefox()
                self.driver.implicitly_wait(30)
                self.driver.set_window_size(1920, 1080)
            self.over_check(self.driver)
            self.driver.quit()

    def over_check(self, driver):
        try:
            for url in page_elements.keys():
                if not (url.__contains__('/personas')) and not (
                    driver_param.__eq__("iPhone4") or driver_param.__eq__("iPhone5")):
                     driver.get(self.main_url + url)
                     locator = page_elements.get(url)
                     driver.find_element(By.CSS_SELECTOR, locator[0]).is_displayed(), "Element is absent on the page!"
                     assert driver.find_element(By.CSS_SELECTOR, locator[0]).text.__eq__(locator[1]), "Text is wrong!"
        except:
            self.driver.quit()
            raise Exception("There is no such element")
