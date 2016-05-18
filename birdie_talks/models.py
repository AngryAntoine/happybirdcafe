# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Create your models here.


@python_2_unicode_compatible
class Article(models.Model):
    author = models.ForeignKey('auth.User', verbose_name=_('author'))
    title = models.CharField(_('title'), max_length=200)
    text = models.TextField(_('article text'))
    image = models.ImageField(_('image'), upload_to='articles/%Y/%m/%d', blank=True, null=True)

    created_date = models.DateTimeField(_('created date'),
                                        default=timezone.now)
    published_date = models.DateTimeField(_('published date'),
                                          blank=True, null=True)

    def publish(self):
        self.save()

    class Meta:
        ordering = ('title',)
        verbose_name = _('article')
        verbose_name_plural = _('articles')

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Recommendation(models.Model):
    author = models.ForeignKey('auth.User', verbose_name=_('author'))
    title = models.CharField(_('title'), max_length=200)
    text = models.TextField(_('article text'))
    image = models.ImageField(_('image'), upload_to='articles/%Y/%m/%d', blank=True, null=True)
    created_date = models.DateTimeField(_('created date'),
                                        default=timezone.now)
    published_date = models.DateTimeField(_('published date'),
                                          blank=True, null=True)

    def publish(self):
        self.save()

    class Meta:
        ordering = ('title',)
        verbose_name = _('recommendation')
        verbose_name_plural = _('recommendation_articles')

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Feeder(models.Model):
    author = models.ForeignKey('auth.User', verbose_name=_('author'))
    title = models.CharField(_('title'), max_length=200)
    text = models.TextField(_('article text'))
    pupil_name = models.CharField(_('pupil name'), max_length=50, null=True, blank=True)
    pupil_age = models.PositiveIntegerField(_('pupil age'), null=True, blank=True)
    school = models.CharField(_('school'), max_length=100, null=True, blank=True)
    price = models.PositiveIntegerField(_('price'), blank=True, null=True)
    image = models.ImageField(_('image'), upload_to='articles/%Y/%m/%d', blank=True, null=True)
    created_date = models.DateTimeField(_('created date'),
                                        default=timezone.now, blank=True, null=True)
    published_date = models.DateTimeField(_('published date'),
                                          blank=True, null=True)

    class Meta:
        ordering = ('title',)
        verbose_name = _('feeder')
        verbose_name_plural = _('feeders')

    def __str__(self):
        return self.title
