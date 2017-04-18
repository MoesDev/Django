from django.shortcuts import render, redirect
import random
import string

# Create your views here.

def index(request):
	if "count" not in request.session:
		request.session["count"]=1
	random_str = {"random_string" : randomnum()}
	return render(request, 'randomword/index.html', random_str)

def randomnum(size=14, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

def generate(request):
	if request.method == "POST":
		request.session["count"] += 1
		return redirect ('/')

	
