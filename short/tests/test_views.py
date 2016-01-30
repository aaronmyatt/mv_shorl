from django.test import RequestFactory as rf

from test_plus.test import TestCase

from ..views import (
    url_encode
)


class TestUrlEncodeView(TestCase):

    def test_get_returns_view(self):
        self.assertGoodView('shorten:encode')

    def test_get_contains_template(self):
        response = self.get('shorten:encode')
        t = 'Shorten a URL by entering it in the box below.'
        self.assertContains(response, t)

    def test_post_contains_submitted_url(self):
        form={'url':'http://www.google.com'}
        response = self.post('shorten:encode', data=form)
        self.assertContains(response, form['url'])

class TestUrlDecodeView(TestCase):

    def test_get_returns_view(self):
        self.assertGoodView('shorten:decode', pattern='http://www.encodeme.com')

    def test_handles_a_variety_of_patterns(self):
        self.assertGoodView('shorten:decode', pattern='Fj90WMNjnas')
        self.assertGoodView('shorten:decode', pattern='https://www.google.com')



# class TestUserUpdateView(BaseUserTestCase):
#
#     def setUp(self):
#         # call BaseUserTestCase.setUp()
#         super(TestUserUpdateView, self).setUp()
#         # Instantiate the view directly. Never do this outside a test!
#         self.view = UserUpdateView()
#         # Generate a fake request
#         request = self.factory.get('/fake-url')
#         # Attach the user to the request
#         request.user = self.user
#         # Attach the request to the view
#         self.view.request = request
#
#     def test_get_success_url(self):
#         # Expect: '/users/testuser/', as that is the default username for
#         #   self.make_user()
#         self.assertEqual(
#             self.view.get_success_url(),
#             '/users/testuser/'
#         )
#
#     def test_get_object(self):
#         # Expect: self.user, as that is the request's user object
#         self.assertEqual(
#             self.view.get_object(),
#             self.user
#         )
