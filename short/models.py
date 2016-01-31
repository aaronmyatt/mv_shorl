from django.db import models
from django.utils.translation import ugettext_lazy as _
from base64 import b64encode

class Shorten(models.Model):
    user = models.ForeignKey('users.User')
    url = models.URLField(_('Url'), blank=False)
    encoded = models.URLField(_('Encoded'), db_index=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        super(Shorten, self).save()
        self.encoded = self.encode()
        super(Shorten, self).save()

    def encode(self):
        return b64encode(bytes(str(self.id),
                               encoding='UTF-8'))

    @classmethod
    def decode(cls, code):
        try:
            return cls.objects.get().url
        except cls.DoesNotExist:
            # TODO raise a message/error
            pass
