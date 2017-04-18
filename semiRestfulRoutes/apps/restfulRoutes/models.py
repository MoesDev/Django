from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=60)
	desc = models.CharField(max_length=250)
	price = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add = True)
	update_at = models.DateTimeField(auto_now = True)
