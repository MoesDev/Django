from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import bcrypt

class UserManager(models.Manager):
	def login(self, email, password, request):
		if len(User.usermanager.filter(email=email)) < 1:
			messages.error(request,"Email does not exist", extra_tags='loginError')
			return False
		else:
			user= User.usermanager.get(email=email)
			hashed = user.password.encode('utf-8')
			enteredPass = bcrypt.hashpw(password.encode('utf-8'), hashed)
			if hashed == enteredPass:
				request.session['loginEmail']=""
				return (True, user.id)

			else:
				request.session['loginEmail']= email
				messages.error(request, "-Email and/or password are not valid", extra_tags='loginError')
				return False


class User(models.Model):
	firstName=models.CharField(max_length=60)
	lastName=models.CharField(max_length=100)
	email=models.EmailField(max_length=150)
	password=models.CharField(max_length=30)
	usermanager = UserManager()


		