# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Create your models here.


@python_2_unicode_compatible
class Contacts(models.Model):
    author = models.ForeignKey('auth.User', verbose_name=_('author'))
    title = models.CharField(_('title'), max_length=200)
    phone = models.CharField(_('phone'), max_length=200)
    email = models.CharField(_('e-mail'), max_length=200)
    text = models.TextField(_('text'))
    image = models.ImageField(_('image'), upload_to='contacts/%Y/%m/%d', blank=True, null=True)
    created_date = models.DateTimeField(_('created date'),
                                        default=timezone.now, blank=True, null=True)
    published_date = models.DateTimeField(_('published date'),
                                          blank=True, null=True)

    class Meta:
        ordering = ('title',)
        verbose_name = _('contacts')
        verbose_name_plural = _('contacts')

    def __str__(self):
        return self.title
