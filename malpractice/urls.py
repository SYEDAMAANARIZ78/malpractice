from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('', views.login_user, name = 'login'),
    path('form/', views.malpracticeform, name = 'malform'),
    path('homepage/', views.homepage, name = 'homepage'),
    path('login/', views.login_user, name = 'login'),
    path('search/', views.searchstudent, name = 'sstudent'),
    path('actiont/', views.action, name = 'actiont'),
    path('signup/', views.signup, name = 'signup'),
    path('savedetails/', views.saveDetails, name = 'savedetails'),
    path('showresult/', views.showresult, name = 'showresult'),
    path('actiontk/', views.actiontk, name = 'actiontk'),
    path('update/', views.update, name = 'update'),
]
