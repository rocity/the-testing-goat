from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
            )

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Rey has heard about a cool new online to-do app. He goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # He notices the page title and header mention to-do  lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )

        # He types "Make coffee" into a text box (Rey can't work when he is sleepy)
        inputbox.send_keys('Make coffee')

        # When he hits enter, he is taken to a new URL,
        # and now the page lists "1: Make coffee" as an item in a
        # to-do list table
        inputbox.send_keys(Keys.ENTER)
        rey_list_url = self.browser.current_url
        self.assertRegex(rey_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Make coffee')

        # There is still a text box inviting him to add another item.
        # He enters "Go to the toilet" (Rey is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Go to the toilet')
        inputbox.send_keys(Keys.ENTER)
        
        # The page updates again, and now shows both items on his list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('1: Make coffee'),
        self.check_for_row_in_list_table('2: Go to the toilet'),

        # Now a new user, Warrin comes along to the site.

        ## We use a new browser session to make sure that no information
        ## of Rey's is coming through from cookies etc #
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Warrin visits the home page. There is no sign of Rey's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Make coffee', page_text)
        self.assertNotIn('Go to the toilet', page_text)

        # Warrin starts a new list by entering a new item.
        # he is less interesting than Rey...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Warrin gets his own unique URL
        warrin_list_url = self.browser.current_url
        self.assertRegex(warrin_list_url, '/lists/.+')
        self.assertNotEqual(warrin_list_url, rey_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Make coffee', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both go back to sleep
        