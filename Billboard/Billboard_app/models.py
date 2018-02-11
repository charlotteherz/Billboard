# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Post(models.Model):
    posts_pub_date = models.DateTimeField('date posted')
    posts_title = models.CharField(max_length=100)
    posts_text = models.CharField(max_length = 255)
    posts_author = models.CharField(max_length=100)
