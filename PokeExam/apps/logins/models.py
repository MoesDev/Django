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
	name=models.CharField(max_length=60)
	alias=models.CharField(max_length=100)
	email=models.EmailField(max_length=150)
	password=models.CharField(max_length=200)
	pokes=models.IntegerField(default=0)
	poking=models.ManyToManyField("self", through='PokeHistory', symmetrical=False, through_fields=('poker','pokee'), related_name='pokeRecord')
	birthday=models.DateTimeField()
	created_at=models.DateTimeField(auto_now_add = True)
	updated_at=models.DateTimeField(auto_now = True)
	usermanager = UserManager()

	def pokeCreate(self, poker):
		poking = PokeHistory.objects.get_or_create(pokee=self, poker=poker)
		return poking

	def pokeShow(self):
		poker = self
		poking = PokeHistory.objects.filter(pokee=poker)
		return poking

	def pokeFilter(self, poker):
		poker = self
		poking = PokeHistory.objects.filter(pokee=self, poker=poker)
		return poking


class PokeHistory(models.Model):
	poker=models.ForeignKey(User, related_name='poker')
	pokee=models.ForeignKey(User, related_name='pokee')
	friendPokes=models.IntegerField(default=0)
	created_at=models.DateTimeField(auto_now_add = True)
	updated_at=models.DateTimeField(auto_now = True)



		