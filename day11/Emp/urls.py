from django.urls import path
from Emp import views

urlpatterns = [
   path('',views.home,name="hm"),
   path('abt/',views.about,name="ab"),
   path('con/',views.contact,name="na"),
   path('log/',views.login,name="lo"),
   path('reg/',views.register,name="re"),
   
]