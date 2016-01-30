from django.test import RequestFactory as rf

from test_plus.test import TestCase

from ..views import (
    url_encode
)


class TestUrlEncodeView(TestCase):

    def test_get_returns_view(self):
        self.assertGoodView('shorten:encode')

class TestUrlDecodeView(TestCase):

    def test_get_returns_view(self):
        self.assertGoodView('shorten:decode')




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
