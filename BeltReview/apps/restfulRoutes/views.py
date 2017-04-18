from django.shortcuts import render, redirect
from models import Book, Review
from django.contrib import messages

def index(request):
	books = Book.objects.all()
	context ={"books":books}
	return render(request, "restfulRoutes/index.html", context)

def show(request, id):
	books = Book.objects.filter(id=id)
	context ={"books":books[0]}
	return render(request, "restfulRoutes/show.html", context)

def new(request):
	if 'bookTitle' not in request.session:
		request.session['bookTitle']=""
	addBookPage = render(request, "restfulRoutes/addBooks.html")
	request.session['bookTitle']=""
	return addBookPage

def edit(request, id):
	books = Book.objects.filter(id=id)
	context ={"books":books[0]}
	return render(request, "restfulRoutes/edit.html", context)
	
def create(request):
	book = request.POST['book']
	otherAuthor = request.POST['otherAuthor']
	checkAuthor = Book.objects.filter(author=otherAuthor)
	if otherAuthor != "" and len(checkAuthor) == 0:
		author = otherAuthor
	elif len(checkAuthor) > 0:
		message.error("Author entered is already in provided list. Please erase from 'add' area and select from drop down")
		request.session['bookTitle']=book
		return redirect('books:new')
	else:
		author = request.POST['author']
	Book.objects.create(bookTitle= book, author=author, price=price)
	return redirect('books:create')

def update(request, id):
	books = Book.objects.get(id=id)
	books.name = request.POST['name']
	books.desc = request.POST['desc']
	books.price = request.POST['price']
	books.save()
	print"*************************************"
	print"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
	return redirect('/')


def destroy(request, id):
	Book.objects.filter(id=id).delete()
	return redirect('/')
