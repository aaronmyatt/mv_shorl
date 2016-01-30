# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the url_encode view
    url(
        regex=r'^encode$',
        view=views.url_encode,
        name='encode'
    ),
    # URL pattern for the url_decode view
    url(
        regex=r'^(?P<pattern>.*)$',
        view=views.url_decode,
        name='decode'
    )
]
