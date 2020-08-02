from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from .forms import UserUpdateForm, ProfileUpdateForm
from django.db.models import Q
from .models import Subject,Category,Book
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#from django.http import HttpResponse
#from django.template import loader

def index(request):
    return render(request,'homepage/index.html')

        
def seperate(request,subject):
    title=str(subject)
    subject=Subject.objects.get(sub_title__startswith=title)
    return render(request,'homepage/seperate.html',{'subject':subject})
    #return HttpResponse("<h1>Book name:</h2>")


def search(request):
    query=request.GET.get('q')

    if query:
        category=Category.objects.filter(Q(year__icontains=query) | Q(branch__icontains=query))
        subject=Subject.objects.filter(Q(sub_title__icontains=query))
        book=Book.objects.filter(Q(book_title__icontains=query) | Q(author__icontains=query))
    return render(request,"homepage/search.html",{'category':category,'subject':subject,'book':book})

def signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                category=Category.objects.all()
                return render(request,'homepage/year.html',{'category':category})
    return render(request, 'homepage/signup.html', {"form": form})

def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    category=Category.objects.all()
                    return render(request,'homepage/year.html',{'category':category})
            else:
                return render(request, 'homepage/log_in.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'homepage/log_in.html', {'error_message': 'Invalid login'})
    return render(request, 'homepage/log_in.html')

def log_out(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'homepage/log_in.html', context)

def year(request):
    """if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:"""
    category=Category.objects.all()
    return render(request,'homepage/year.html',{'category':category})

def fy(request):
    category=Category.objects.filter(branch="Fy")
    return render(request,'homepage/year.html',{'category':category})


def it(request):
    category=Category.objects.filter(branch="Information Technology")
    return render(request,'homepage/year.html',{'category':category})


def mech(request):
    category=Category.objects.filter(branch="Mechanical")
    return render(request,'homepage/year.html',{'category':category})


def comp(request):
    category=Category.objects.filter(branch="Computer Technology")
    return render(request,'homepage/year.html',{'category':category})


def extc(request):
    category=Category.objects.filter(branch="Electronics and Telecommunication")
    return render(request,'homepage/year.html',{'category':category})


def instru(request):
    category=Category.objects.filter(branch="Instrumentation")
    return render(request,'homepage/year.html',{'category':category})


def civil(request):
    category=Category.objects.filter(branch="Civil")
    return render(request,'homepage/year.html',{'category':category})



def more(request,year):
    year=str(year)
    category=Category.objects.get(year__startswith=year)
    subject=Subject.objects.all()
    return render(request,'homepage/more.html',{'category':category,'subject':subject})

def detail(request,title):
    #return HttpResponse("<h1>Book name: "+str(title)+"</h2>")
    title=str(title)
    book=Book.objects.get(book_title__startswith=title)
    return render(request,'homepage/bk_detail.html',{'bk':book})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'homepage/profile.html', context)
