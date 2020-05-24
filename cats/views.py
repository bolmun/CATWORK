from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models, forms


class HomeView(ListView):

    model = models.Cat
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "cats"


def cat_detail(request, pk):
    try:
        cat = models.Cat.objects.get(pk=pk)
        return render(request, "cats/cat_details.html", {"cat": cat})
    except models.Cat.DoesNotExist:
        return redirect(reverse("core:home"))


def search(request):
    form = forms.SearchForm()
    return render(request, "cats/search.html", {"form": form})
