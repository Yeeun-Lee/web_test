# 파이썬 2와 3간의 호환성 유지
from __future__ import unicode_literals
import string
import random
# from six import python_2_unicode_compatible

from django.db import models
from django import forms

from django.template.defaultfilters import slugify

# for url pattern
from django.urls import reverse
# Create your models here.
def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
# @python_2_unicode_compatible
class Post(models.Model):
    writer = models.CharField(max_length=100)
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField(max_length=6, unique=True,
                            default=rand_slug(),
                            verbose_name='slug')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now = True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'my_post'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs = {'slug': self.slug})
    def get_previous_post(self):
        return self.get_previous_by_modify_date()
    def get_next_post(self):
        return self.get_next_by_modify_date()
    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)
class Notice(models.Model):
    writer = models.CharField(max_length=100, default='parrotadmin')
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField(max_length=6, unique=True,
                            default=rand_slug(),
                            verbose_name='slug')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)

    class Meta:
        verbose_name = 'notice'
        verbose_name_plural = 'notices'
        db_table = 'parrot'
        ordering = ('-modify_date',)
    def get_previous_post(self):
        return self.get_previous_by_modify_date()
    def get_next_post(self):
        return self.get_next_by_modify_date()
    def save(self, *args, **kwargs):
        self.slug = self.slug or ssslugify(self.title)
        super().save(*args, **kwargs)

class Submission(models.Model):
    user_name = models.CharField(max_length=100, default = 'parrotadmin')
    user_ranking = models.FloatField(default=0)
    submission_file = models.FileField(upload_to='documents/',
                                       default=None)
    submission_time = models.DateTimeField('Submission Date', auto_now_add=True)

    class Meta:
        verbose_name = 'submission'
        verbose_name_plural = 'submissions'
        db_table = 'parrot_con'
        ordering = ('-user_ranking',)
class FileForm(forms.Form):
    title = forms.CharField(max_length = 100)
    csvfile = forms.FileField(
        label = 'Select a file',
        help_text='only csv file(ex/prediction)'
    )