from __future__ import unicode_literals

from django.db import models
from ..the_courses.models import Course
from ..logins.models import User, UserManager
 

class Class(models.Model):
	course_id = models.ForeignKey(Course, default=0)
	user_id = models.ForeignKey(User, default=0)
	

