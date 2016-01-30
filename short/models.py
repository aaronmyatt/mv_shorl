from django.db import models
from django.utils.translation import ugettext_lazy as _

class Shorten(models.Model):
    user = models.ForeignKey('users.User')
    url = models.URLField(_('Url'), blank=False)
    encoded = models.URLField(_('Encoded'), blank=False, db_index=True)

    def encode(self, url):
        return url

    def decode(self, code):
        return self.id
