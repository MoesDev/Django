from django.shortcuts import render, redirect
import random
import time


# Create your views here.
def index(request):

	if "gold" not in request.session:
		request.session['result']=[]
		request.session['gold']=int(0)

	return render(request, 'ninjagold/index.html')

def process(request):
	if request.method == "POST":
		clock=time.strftime('%m/ %d, %Y %H:%M')
		winnings=0
		amount=""
		if request.POST['action']=='farm':
		
			winnings =random.randint(10,20)
			
		elif request.POST['action'] == 'cave':
			winnings=random.randint(5,10)	

		elif request.POST['action'] == 'house':
			winnings=random.randint(2,5)
			
			
		elif request.POST['action'] == 'casino':
			winnings=random.randint(-50,50)

		request.session['gold']+=winnings
		if winnings >=0:
			amount="Earned "
		else:
			amount="Loss of "
		logstring=amount + str(winnings)+ " golds from the farm" + str("\n") + clock
		request.session['result'].append(logstring)

	return redirect('/')




