from django.shortcuts import render
from .models import Class
from ..the_courses.models import Course
from ..logins.models import User, UserManager
from django.db.models import Count


def index(request):
	courses = Course.objects.all()
	students = User.usermanager.all()
	

	context={'courses':courses, 'students':students}
	return render(request, "multiApps/index.html", context)

def classInfo(request):
	count = Course.objects.annotate(numUsers= Count('id'))
	return redirect('index:index')


