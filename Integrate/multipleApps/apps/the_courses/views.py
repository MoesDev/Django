from django.shortcuts import render, redirect
from .models import Course

def index(request):
	if 'validate' not in request.session:
		request.session['validate']=""
		request.session['desc']=""
	course = Course.objects.all()
	context ={"courses": course}
	return render(request, "the_courses/index.html", context)

def create(request):
	course_name = request.POST['name']
	description = request.POST['description']
	if len(course_name) == 0:
		request.session['validate']="**Must enter name of course**"
		request.session['desc'] = request.POST['description']
	else:
		request.session['desc'] = ""
		request.session['validate']=""
		Course.objects.create(name=course_name, description=description)
	return redirect('courses:index')

def remove(request, id):
	Course.objects.filter(id=id).delete()
	return redirect('courses:index')
