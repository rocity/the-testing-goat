from selenium import webdriver
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
        self.fail('Finish the test!')

        # He is invited to enter a to-do item straight away

        # He types "Make coffee" into a text box (Rey can't work when he is sleepy)

        # There is still a text box inviting him to add another item.
        # He enters "Go to the toilet" (Rey is very methodical)

        # The page updates again, and now shows both items on his list

        # Rey wonders whether the site will remember his list. Then he sees that
        # the site has generated a unique URL for him

        # He visits that URL - his to-do list is still there

        # Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')