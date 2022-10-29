from .models import Ticket
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from urllib import request
from .models import registers
from datetime import datetime
from .forms import PersonalDataForm
from django.contrib import messages



def main(request):
    return render(request,'main.html')

def index(request):
	if request.user.is_anonymous:
		return redirect('/login')
    
	tickets = Ticket.objects.order_by('-created_at')[:5]
	return render(request,'index.html', {'tickets': tickets})

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/index')
            
        else:
            return render(request,"login.html")
    return render(request,"login.html")

def registeruser(request):
	if request.method == "POST":
		username= request.POST.get("name")
		name= request.POST.get("flname")
		email= request.POST.get("email")
		phone = request.POST.get("phone")
		desc = request.POST.get("desc")
		registered = registers(username=username,name=name,email=email,phone=phone,desc=desc,date=datetime.today())
		registered.save()
		messages.success(request, 'Your Query has been sent!')
	return render(request,'register.html')

def newuser(request):
	if request.method == "POST":
		form = PersonalDataForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = PersonalDataForm()
	return render (request=request, template_name="newuser.html", context={"register_form":form})


def logoutuser(request):
    logout(request)
    return redirect('/login')

def ticket_by_id(request, ticket_id):
	ticket = Ticket.objects.get(pk=ticket_id)
	return render(request, 'firstpage.html', {'ticket':ticket})