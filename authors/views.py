from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.http import Http404
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def register_view(request):
    
    regiter_form_data = request.session.get("regiter_form_data", None)
    form = RegisterForm(regiter_form_data)
    return render(request, "authors/pages/register_view.html", context={
        "form": form,
        "form_action": reverse('authors:register_create')
    })
def register_create(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session["regiter_form_data"] = POST

    form = RegisterForm(request.POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, "your user is created, please log in")
        del(request.session["regiter_form_data"])

    return redirect("authors:register")

def login_view(request):
    form = LoginForm()
    return render(request, "authors/pages/login.html", context={
        "form": form,
        "form_action": reverse("authors:login_create")
    })

def login_create(request):
    return render(request, "authors/pages/login.html")