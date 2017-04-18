from django.shortcuts import render, redirect
from models import Product

def index(request):
	products = Product.objects.all()
	context ={"products":products}
	return render(request, "restfulRoutes/index.html", context)

def show(request, id):
	products = Product.objects.filter(id=id)
	context ={"products":products[0]}
	return render(request, "restfulRoutes/show.html", context)

def new(request):
	return render(request, "restfulRoutes/new.html")

def edit(request, id):
	products = Product.objects.filter(id=id)
	context ={"products":products[0]}
	return render(request, "restfulRoutes/edit.html", context)
	
def create(request):
	name = request.POST['name']
	desc = request.POST['desc']
	price = request.POST['price']
	Product.objects.create(name= name, desc=desc, price=price)
	return redirect('/')

def update(request, id):
	products = Product.objects.get(id=id)
	products.name = request.POST['name']
	products.desc = request.POST['desc']
	products.price = request.POST['price']
	products.save()
	print"*************************************"
	print"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
	return redirect('/')


def destroy(request, id):
	Product.objects.filter(id=id).delete()
	return redirect('/')
