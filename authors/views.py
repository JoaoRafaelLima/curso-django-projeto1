from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import Http404


# Create your views here.
def register_view(request):
    regiter_form_data = request.session.get("regiter_form_data", None)
    form = RegisterForm(regiter_form_data)
    return render(request, "authors/pages/register_view.html", context={
        "form": form
    })
def register_create(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session["regiter_form_data"] = POST

    form = RegisterForm(request.POST)
    return redirect("authors:register")