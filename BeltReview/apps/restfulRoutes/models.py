from __future__ import unicode_literals

from django.db import models
from logins.models import User, UserManager

class Book(models.Model):
	bookTitle = models.CharField(max_length=200)
	user_id = models.ForeignKey(logins.User)
	author = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add = True)
	update_at = models.DateTimeField(auto_now = True)

class Review(models.Model):
	book = models.ForeignKey(Book)
	review = models.TextField(max_length=400)
	stars = models.IntegerField()
	user_comment = models.ManytoManyField(logins.User)
	created_at = models.DateTimeField(auto_now_add = True)
	update_at = models.DateTimeField(auto_now = True)
