from django.urls import path
from Noteapp import views
from django.contrib.auth import views as ad 

urlpatterns = [
	path('',views.home,name='hm'),
	path('abt/',views.about,name='ab'),
	path('cnt/',views.contact,name='cn'),
	path('lg/',ad.LoginView.as_view(template_name='html/login.html'),name="log"),
	path('reg/',views.regi,name="rg"),
	path('ds/',views.dashboard,name="dsh"),
	path('lgo/',ad.LogoutView.as_view(template_name='html/logout.html'),name="lgo"),
	path('pro/',views.profile,name="profile"),
	path('com/',views.complaint,name="cp"),
	path('updf/',views.updpf,name="upf"),
	path('ch/',views.cgf,name="cg"),
	path('rst/',ad.PasswordResetView.as_view(template_name="html/resetpassword.html"),name="reset_password"),
	path('rst_done/',ad.PasswordResetDoneView.as_view(template_name="html/resetpassworddone.html"),name="password_reset_done"),
	path('rst_cf/<uidb64>/<token>/',ad.PasswordResetConfirmView.as_view(template_name="html/reset_password_confirm.html"),name="password_reset_confirm"),
	path('rst_cmplt/',ad.PasswordResetCompleteView.as_view(template_name="html/reset_password_complete.html"),name="password_reset_complete"),
]