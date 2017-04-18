from django.shortcuts import render, redirect
from .models import User, UserManager
import re
import bcrypt

def index(request):
	if "pageClear" not in request.session:
		request.session['pageClear']=True
		request.session['userID']=0
	if request.session['pageClear'] ==True:
		clear(request)
	context={"users": User.usermanager.all()}
	result= render(request, "logins/index.html", context)
	clear(request)
	return result

def register(request):
	firstName = request.POST['f_name']
	lastName = request.POST['l_name']
	email = request.POST['reg_email'].lower()
	password = request.POST['reg_pw']
	confPassword = request.POST['conf_reg_pw']

	emailRegXpass = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
	nameRegXpass = re.compile(r'^[a-zA-Z]+$')
	first=firstName
	last=lastName
	valEm=email
	doesEMailExist=User.usermanager.filter(email=email)
	print doesEMailExist
	print "***********************************************"
	print len(doesEMailExist)
	if len(firstName) < 2 or len(lastName) < 2:
		validate="-Enter First and Last Name (Must be 2 or more characters)"
	elif not nameRegXpass.match(firstName):
		validate = "-Names can only contain letters"
	elif not nameRegXpass.match(lastName):
		validate = "-Names can only contain letters"
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
		User.usermanager.create(firstName= firstName, lastName=lastName, email=email.lower(), password= pwhash)
		userDir=User.usermanager.filter(email=email)
		the_new_users_id=userDir[0].id
		request.session['userID']=the_new_users_id
		return redirect('/user/success')
	request.session['validate']=validate
	request.session['fname']=first
	request.session['lname']=last
	request.session['valEmail']=valEm
	return redirect('/')

	

def login(request):
	entered_email = request.POST['login_email'].lower()
	entered_password = request.POST['login_password']
	user = User.usermanager.login(entered_email, entered_password, request)

	if user == False:
		return redirect('/')
	else:
		request.session['userID']=user[1]
		request.session['pageClear']=True
		return redirect('/user/success')
		

def success(request):
	if request.session['userID']== 0:
		return redirect('/not_signed_in')
	else:
		signedInUser= User.usermanager.get(id=request.session['userID'])
		context = {"users":signedInUser}
		return render(request,"logins/success.html", context)

def delete(request, id):
	User.usermanager.filter(id=id).delete()
	return redirect('/')

def clear(request):
	request.session['validate']=""
	request.session['fname']=""
	request.session['lname']=""
	request.session['valEmail']=""
	request.session['loginEmail']=""
	request.session['pageClear']=False
	return redirect('/')

def signout(request):
	request.session['userID']=0
	return redirect('/')

def not_signed_in(request):
	return render(request, "logins/not_signed_in.html")
	