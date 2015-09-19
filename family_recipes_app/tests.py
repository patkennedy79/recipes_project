# -*- coding: utf-8 -*-
from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase

class HomeNewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_it_worked_site_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Kennedy Family Recipes', self.browser.title)

#    def test_it_worked_site_body_text(self):
#        self.browser.get('http://localhost:8000')
#        self.assertIn('From pancakes to homemade granola', self.browser.find_element_by_id("summary").text)

    def test_about_page_site_title(self):
        self.browser.get('http://localhost:8000/about/')
        self.assertIn('', self.browser.title)

#    def test_about_page_body_text(self):
#        self.browser.get('http://localhost:8000')
#        self.assertIn('This is the ABOUT page for the Kennedy Family Recipe site.', self.browser.find_element_by_id("summary").text)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
