from django.shortcuts import render, redirect
from .models import Message, Comment

def index(request):
	message = Message.objects.all()
	comment = Comment.objects.all()
	context = {'messages': message,'comments':comment}
	return render(request, "wall/index.html", context)

def message(request):
	if request.method == "POST":
		Message.objects.create(message=request.POST['message'],)
	return redirect('/')

def comment(request, id):
	if request.method == "POST":
		the_message = Message.objects.get(id=id)
		Comment.objects.create(comment=request.POST['comment'], message_id=the_message)
	return redirect('/')
