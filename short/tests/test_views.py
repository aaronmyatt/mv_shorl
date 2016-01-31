from base64 import b64encode
from unittest.mock import MagicMock, patch
from django.test import RequestFactory as rf

from test_plus.test import TestCase


from ..views import (
    url_encode,
    url_decode
)
from ..models import (
    Shorten
)

URL = '/encode'
form={'url':'http://www.google.com'}

class BaseUserTestCase(TestCase):
    form={'url':'http://www.google.com'}

    def setUp(self):
        self.user = self.make_user()
        self.get_request = rf().get(URL)
        self.post_request = rf().post(URL, data=form)
        self.get_request.user = self.user
        self.post_request.user = self.user


class TestUrlEncodeView(BaseUserTestCase):

    def test_get_returns_view(self):
        response = url_encode(self.get_request)
        self.response_200(response)

    def test_get_contains_template(self):
        response = url_encode(self.get_request)
        t = 'Shorten a URL by entering it in the box below.'
        self.assertContains(response, t)

    def test_post_contains_submitted_url(self):
        response = url_encode(self.post_request)
        self.assertContains(response, form['url'])


class TestUrlDecodeView(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.short = Shorten(
            url=form['url'],
            user=self.user
        )
        self.short.save()

        self.encoded = self.short.encoded
        self.get_request = rf().get(self.encoded)
        self.get_request.user = self.user

    def test_get_returns_redirect(self):
        response = url_decode(self.get_request, self.encoded)
        self.response_302(response)

    def test_get_calls_ShortenDOTdecode(self):
        with patch('short.models.Shorten.decode') as mock_decode:
            response = url_decode(self.get_request, self.encoded)
            self.assertTrue(mock_decode.called)

    def test_get_calls_redirects_to_decode_return_value(self):
        with patch('short.models.Shorten.decode') as mock_decode:
            mock_decode.return_value = form['url']
            response = url_decode(self.get_request, self.encoded)
            self.response_302(response)
            self.assertEqual(response.url, form['url'])


class TestShortenModel(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.short = Shorten(
            url=form['url'],
            user=self.user
        )
        self.short.save()

    def test_urlencode_returns_shortened_url(self):
        should_be = b64encode(bytes('2',
                                    encoding='UTF-8'))
        self.assertEqual(self.short.encoded, should_be)

    def test_decode_returns_shortened_url(self):

        encoded = b64encode(bytes('1',
                                    encoding='UTF-8'))
        should_be = Shorten.decode(code=encoded)
        self.assertEqual(should_be, form['url'])

