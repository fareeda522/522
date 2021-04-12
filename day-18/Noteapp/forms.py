from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from Noteapp.models import Complaintbox,ImProfile



class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter password"}),)
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}),)
	class Meta:
		model=User
		fields=['username']
		widgets={"username":forms.TextInput(attrs={
			"class":"form-control","placeholder":"enter username",
			}),

		}

class ComplaintForm(forms.ModelForm):
	class Meta:
		model=Complaintbox
		fields="__all__"

class UtupForm(forms.ModelForm):
   	class Meta:
   		model=User
   		fields=["username","email"]
   		widgets={"username":forms.TextInput(attrs={"class":"form-control",}),"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Update Emailid"}),}




class ImForm(forms.ModelForm):
	class Meta:
		model=ImProfile
		fields=["age","gender","impf"]
		widgets={
		"age":forms.NumberInput(attrs={"class":"form-control","placeholder":"update your age",}),
		"gender":forms.NumberInput(attrs={"class":"form-control","placeholder":"update your gender",}),
		}

class ChpwdForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter old password"})),
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter new password"})),
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter confirm password"})),
	class Meta:
		model=User
		fields=['oldpassword','newpassword','confirmpassword']

 