from django.shortcuts import render
from .forms import bookForm,signupForm

def home(request):
     return render(request,'home.html')
def menu(request):
     return render(request,'menu.html')
def blog(request):
     return render(request,'blog.html')
def booking(request):
     if request.method=="POST":
          form=bookForm(request.POST)
          if form.is_valid():
               form.save()
               return render(request,'home.html')
     else:
          form=bookForm()
          return render(request,'booking.html')
def contact(request):
     return render(request,'contact.html')
def team(request):
     return render(request,'team.html')
def about(request):
     return render(request,'about.html')
def rest(request):
     return render(request,'rest.html')
def signup(request):
     if request.method == "POST":
          form = signupForm(request.POST)
          if form.is_valid():
               form.save()
               return render(request,'menu.html')
     else:
          form = signupForm()
          return render(request, 'register.html')



