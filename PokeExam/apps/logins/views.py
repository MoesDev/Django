from django.shortcuts import render, redirect
from .models import User, UserManager, PokeHistory
from django.contrib import messages
import re
import bcrypt

def index(request):
	if "pageClear" not in request.session:
		request.session['pageClear']=True
		request.session['userID']=0
	else:
		request.session['fname_signedIn']=""
	if request.session['pageClear'] ==True:
		clear(request)
	context={"users": User.usermanager.all()}
	load_index_pg= render(request, "logins/index.html", context)
	clear(request)
	request.session['userID']=0
	return load_index_pg

def register(request):
	firstName = request.POST['f_name']
	lastName = request.POST['l_name']
	email = request.POST['reg_email'].lower()
	password = request.POST['reg_pw']
	confPassword = request.POST['conf_reg_pw']
	birthday = request.POST['birthday']

	emailRegXpass = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
	nameRegXpass = re.compile(r'^[a-zA-Z]+\s?[a-zA-Z]+$')
	namespaceRegXpass = re.compile(r'^\s*[a-zA-Z]+\s?[a-zA-Z]+\s*$')
	first=firstName
	last=lastName
	valEm=email
	doesEMailExist=User.usermanager.filter(email=email)
	if len(firstName) < 2 or len(lastName) < 2:
		validate="-Enter Name and Alias (Must be 2 or more characters)"
	elif not nameRegXpass.match(firstName):
		if namespaceRegXpass.match(firstName):
			validate = "-Names should NOT Start or End with spaces. Please be sure you did not type an empty space at the beginning or ending of your name"
		else:
			validate = "-Names can only contain letters, -- NO numbers, symbols, or special characters"
	elif not nameRegXpass.match(lastName):
		if namespaceRegXpass.match(lastName):
			validate = "-Names should NOT Start or End with spaces. Please be sure you did not type an empty space at the beginning or ending of your name"
		else:
			validate = "-Names can only contain letters, --NO numbers, symbols, or special characters"
	elif len(email) == 0:
		validate = "-Must Enter Email"
	elif not emailRegXpass.match(email):
		validate = "-Email invalid, please enter valid email"
	elif len(doesEMailExist) > 0:
		validate = "-Email already exists in database. Login Below or register with a different email."
	elif password != confPassword or len(password) < 8 or len(password) > 30:
		validate = "-Password and Confirm Password incorrect (Must match and be at least 8 characters - no more than 30)"
	else:
		request.session['pageClear']=True
		pwhash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
		User.usermanager.create(name= firstName, alias=lastName, email=email.lower(), password= pwhash, birthday=birthday)
		userDir=User.usermanager.filter(email=email)
		the_new_users_id=userDir[0].id
		request.session['userID']=the_new_users_id
		return redirect('logins:success')
	request.session['validate']=validate
	request.session['fname']=first
	request.session['lname']=last
	request.session['valEmail']=valEm
	return redirect('logins:index')

	

def login(request):
	entered_email = request.POST['login_email'].lower()
	entered_password = request.POST['login_password']
	user = User.usermanager.login(entered_email, entered_password, request)

	if user == False:
		return redirect('logins:index')
	else:
		request.session['userID']=user[1]
		request.session['pageClear']=True
		return redirect('logins:success')
		

def success(request):
	
	if request.session['userID']== 0:
		return redirect('logins:not_signed_in')
	else:
		showFriendPokes= User.pokeShow(User.usermanager.get(id=request.session['userID']))
		countFriends = len(showFriendPokes)
		signedInUser= User.usermanager.get(id=request.session['userID'])
		context={"users": User.usermanager.all(), "signedIn":signedInUser, "friendPs":showFriendPokes, "countFriends": countFriends }
		return render(request,"logins/pokePage.html", context)

def delete(request, id):
	User.usermanager.filter(id=id).delete()
	return redirect('logins:index')

def clear(request):
	request.session['validate']=""
	request.session['fname']=""
	request.session['lname']=""
	request.session['valEmail']=""
	request.session['loginEmail']=""
	request.session['pageClear']=False
	return redirect('logins:index')

def signout(request):
	request.session['userID']=0
	return redirect('logins:index')

def not_signed_in(request):
	return render(request, "logins/not_signed_in.html")


def pokes(request, id):
	poke = User.usermanager.get(id=id)

	addFriendPokes= User.pokeCreate(poke, User.usermanager.get(id=request.session['userID']))
	addFriendPokes[0].friendPokes = addFriendPokes[0].friendPokes + 1
	addFriendPokes[0].save()
	newPokeNum = poke.pokes + 1
	poke.pokes = newPokeNum
	poke.save()
	return redirect('logins:success')

