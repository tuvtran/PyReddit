from tests.functional.base import BaseFunctionalTest


class NewVisitorTest(BaseFunctionalTest):

    def test_user_can_go_to_webpage(self):

        self.browser.get(self.live_server_url)

        # User goes to webpage and see Reddit in the tile
        self.assertIn('Reddit', self.browser.title)
