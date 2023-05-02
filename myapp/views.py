from django.shortcuts import render
from django.template import loader
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myapp.forms import MalpracticentryForm,LoginnForm
from myapp.models import Malpracticentry,Login
from django.urls import reverse
# Create your views here.

def homepage(request):
    return render(request, "homepage1.html", {})
     

def login_user(request):
    records = Login.objects.all()
	# Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(request.POST)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return render(request,'homepage1.html')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html', {'records':records})
    
def malpracticeform(request):
    if request.method == 'POST':
        form = MalpracticentryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MalpracticentryForm()
    return render(request, "malpracticeform.html")

def saveDetails(request):
    print(request)
    form = MalpracticentryForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/homepage/')
    return render(request, 'homepage1.html')

def searchstudent(request):
    return render(request, 'searchstudent.html')

def showresult(request):
    val = request.GET['registrationnumber']
    mydata = Malpracticentry.objects.filter(registrationnumber=val).values()
    template = loader.get_template('showresult.html')
    context = {'data': mydata,}
    return HttpResponse(template.render(context, request))

def action(request):
    return render(request, "actiontaken.html")

def actiontk(request):
    val = request.POST.get('registrationnumber')
    val1 = request.POST.get('subjectcode')
    actiontk = Malpracticentry.objects.filter(registrationnumber=val, subjectcode=val1).values()
    template = loader.get_template('update.html')
    context = {'data': actiontk,}
    return HttpResponse(template.render(context, request))

def update(request):
    print(request.POST)
    current_record = Malpracticentry.objects.get(registrationnumber=request.POST['registrationnumber'],subjectcode=request.POST['subjectcode'])
    print(current_record)
    form = MalpracticentryForm(request.POST or None, instance=current_record)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/homepage/')
    return render(request, 'homepage1.html')
    
def signup(request):
    return render(request, "signup.html")