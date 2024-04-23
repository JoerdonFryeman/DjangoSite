# Pycharm configuration -> Additional Arguments: test base

from django.test import TestCase


class TestUsers(TestCase):
    all_views = (
        '//login', '//registration', '//profile', '//password_change_form', '//back_to_profile',
        '//password_reset_form', '//password_reset_done', '//password_reset_confirm',
        '//password_reset_complete', '//add_post', '//delete'
    )

    def test_all_views(self):
        count = 0
        for i in self.all_views:
            response = self.client.get(i)
            self.assertEqual(response.status_code, 200)
            count += 1
            print(f'Ran {count} {i} views test')
