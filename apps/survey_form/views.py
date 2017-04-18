from django.shortcuts import render, redirect


# Create your views here.
def index(request):
	if "count" not in request.session:
		request.session["count"]=0
	request.session["name"]=""
	request.session["location"] = ""
	request.session["language"] = ""
	request.session["comment"] = ""
	return render(request, "survey_form/index.html")

def process(request):
	if request.method =="POST":
		print ("*"*80)
		request.session["count"]+=1
		request.session["name"] = request.POST['name']
		request.session["location"] = request.POST['location']
		request.session["language"] = request.POST['language']
		request.session["comment"] = request.POST['comment']
	return redirect('/result')

def result(request):
	return render(request, "survey_form/result.html")
