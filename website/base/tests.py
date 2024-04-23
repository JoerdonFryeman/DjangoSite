# Pycharm configuration -> Additional Arguments: test users

from django.test import TestCase


class TestBase(TestCase):
    all_views = (
        '//', '//content', '//about', '//contact', '//terms_and_privacy', '//email_was_sent', '//page_not_found'
    )

    def test_all_views(self):
        count = 0
        for i in self.all_views:
            response = self.client.get(i)
            self.assertEqual(response.status_code, 200)
            count += 1
            print(f'Ran {count} {i} views test')
