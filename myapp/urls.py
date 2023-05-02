from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('', views.login_user, name='login'),
    path('form/', views.malpracticeform, name = 'malform'),
    path('homepage/', views.homepage, name = 'homepage'),
    path('login/', views.login_user, name = 'login'),
    path('search/', views.searchstudent, name = 'sstudent'),
    path('actiont/', views.action, name = 'actiont'),
    path('signup/', views.signup, name = 'signup'),
    path('savedetails/', views.saveDetails, name = 'savedetails'),
    #path('', include(myapp.urls)),
    #path('', views.homepage, name = 'home'),
]
