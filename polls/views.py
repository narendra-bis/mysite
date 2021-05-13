from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

# def myhome(request):
# 	return render(request,'polls/myhome.html')


def myhome(request):
	template = loader.get_template('polls/myhome.html')
	return HttpResponse(template.render())
	

def add(request):
	if request.method == "POST":
		if "addn" in request.POST:
			import pdb;pdb.set_trace()
			val1 = int(request.POST['inputa'])
			val2 = int(request.POST['inputb'])
			total = val1 + val2
			return render(request,'polls/add.html',{'addn':total})
		elif "subn" in request.POST:
			val1 = int(request.POST['inputa'])
			val2 = int(request.POST['inputb'])
			subtract = val1 - val2
			return render(request,'polls/add.html',{'subn':subtract})
	return render(request,'polls/add.html')