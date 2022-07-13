from django.shortcuts import render
from .models import ipo_models
from .forms import ipoform,signupform
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def ipoviews(r):
    form = ipoform
    if r.method == 'POST':
        form = ipoform(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    return render(r, 'ipo.html', {'form': form})

def home(r):
    return render(r, 'home.html')

@login_required
def details(r):
    obj = ipo_models.objects.all()
    return render(r, 'details.html',{'obj':obj})

def logout(r):
    return render(r,'home.html')



def signup(r):
    form=signupform

    if r.method=='POST':
        form=signupform(r.POST)
        if form.is_valid():


            user=form.save()
            user.set_password(user.password)
            user.save()
            form.save()
        return HttpResponseRedirect("/accounts/login")


    return  render(r,'signup.html',{'form':form})
