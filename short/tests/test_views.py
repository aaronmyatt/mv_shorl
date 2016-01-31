from django.test import RequestFactory as rf
from test_plus.test import TestCase
from base64 import b64encode

from ..views import (
    url_encode
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

    def test_get_returns_view(self):
        self.assertGoodView('shorten:decode', pattern='http://www.encodeme.com')

    def test_handles_a_variety_of_patterns(self):
        self.assertGoodView('shorten:decode', pattern='Fj90WMNjnas')
        self.assertGoodView('shorten:decode', pattern='https://www.google.com')

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

