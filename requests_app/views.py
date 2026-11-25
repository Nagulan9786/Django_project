from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AccessRequestForm
from .models import AccessRequest


@login_required
def request_list(request):
    requests = AccessRequest.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "requests_app/request_list.html", {"requests": requests})


@login_required
def request_create(request):
    if request.method == "POST":
        form = AccessRequestForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("request_list")
    else:
        form = AccessRequestForm()
    return render(request, "requests_app/request_form.html", {"form": form})