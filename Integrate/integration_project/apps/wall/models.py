from __future__ import unicode_literals

from django.db import models

class Message(models.Model):
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		
class Comment(models.Model):
	message_id = models.ForeignKey(Message)
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		