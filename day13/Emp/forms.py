
from Emp.models import UsrRg
from django import forms




class UsregForm(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','password']
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control bg-muted","placeholder":"enter username","required":True,}),
		"password":forms.PasswordInput(attrs={"class":"form-control bg-muted","placeholder":"enter password","required":True,}),
		"email":forms.EmailInput(attrs={"class":"form-control bg-muted","placeholder":"enter email","required":True,})

		}
