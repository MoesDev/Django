from __future__ import unicode_literals

from django.db import models
from ..logins.models import User
from ..wall.models import Message, Comment

class Test(models.Model):
	title = models.CharField(max_length=45)
	blog_creator = models.ForeignKey(Message, default=0)
	comment_creator = models.ForeignKey(Comment, default=0)
	user_creator = models.ForeignKey(User, default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		
