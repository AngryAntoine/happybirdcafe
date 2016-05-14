from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Create your models here.


@python_2_unicode_compatible
class Greeting(models.Model):
    title = models.CharField(_('title'), max_length=200)
    greeting_text = models.TextField(_('greeting text'))
    button_text = models.CharField(_('button text'), max_length=20)

    class Meta:
        ordering = ('title',)
        verbose_name = _('greeting')
        verbose_name_plural = _('greetings')

    def __str__(self):
        return self.title
