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
	path('updf/',views.updpf,name="upf")
]