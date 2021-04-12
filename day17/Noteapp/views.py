from django.shortcuts import render,redirect
from Noteapp.forms import UsForm,ComplaintForm
from django.core.mail import send_mail
from NoteSharing import settings
from django.contrib import messages
from django.contrib.auth.models import User
from Noteapp.models import ImProfile
# Create your views here.
def home(re):
	return render(re,'html/home.html')
def about(re):
	return render(re,'html/about.html')
def contact(re):
	return render(re,'html/contact.html')
def regi(re):
	if re.method=="POST":
		a=UsForm(re.POST)
		if a.is_valid():
			a.save()
			return redirect('/lg')
	a=UsForm()
	return render(re,'html/register.html',{'u':a})
def dashboard(re):
	return render(re,'html/dashboard.html')
def profile(req):
	return render(req,'html/profile.html')
def complaint(request):
	if request.method=="POST":
		data=ComplaintForm(request.POST)
		if data.is_valid():
			subject='Confirmation_Complaint'
			body="thank you for complaining "+request.POST['p_name']
			receiver=request.POST['p_email']
			sender=settings.EMAIL_HOST_USER
			send_mail(subject,body,sender,[receiver])
			data.save()
			messages.success(request,"successfully sent your mail to "+receiver)
			return redirect('/')
	form=ComplaintForm()
	return render(request,'html/complaint.html',{'c':form})


def updpf(request):
	if request .method=="POST":
		u=UtupForm(request.POST,instance=request.user)
	    i=ImForm(request.POST,request.Files,instance=request.user.improfile)
	    if u.is_valid() and i.is_valid():
	    	u.save()
	    	i.save()
	    	return redirect('/pro')
	u=UtupForm(instance=request.user)
	i=ImForm(instance=request.user.improfile)
	return render(request,'html/updateprofile.html',{'us':u,"imp":i})
