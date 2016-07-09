from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Rey has heard about a cool new online to-do app. He goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

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

        # When he hits enter, the page updates, and now the page lists
        # "1: Make coffee" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Make coffee' for row in rows),
            "New to-do item did not appear in table"
            )

        # There is still a text box inviting him to add another item.
        # He enters "Go to the toilet" (Rey is very methodical)
        self.fail('Finish the test!')


        # The page updates again, and now shows both items on his list

        # Rey wonders whether the site will remember his list. Then he sees that
        # the site has generated a unique URL for him

        # He visits that URL - his to-do list is still there

        # Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')