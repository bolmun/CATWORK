from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models, forms


class HomeView(ListView):

    model = models.Cat
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "cats"


class CatDetail(DetailView):
    model = models.Cat


class SearchView(View):
    def get(self, request):

        city = request.GET.get("city")

        if city:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

                name = form.cleaned_data.get("name")
                gender = form.cleaned_data.get("gender")
                appearance = form.cleaned_data.get("appearance")
                is_neutered = form.cleaned_data.get("is_neutered")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                if name != "Anonymous":
                    filter_args["name__startswith"] = name

                if gender is not None:
                    filter_args["gender"] = gender

                if appearance is not None:
                    filter_args["appearance"] = appearance

                if is_neutered is True:
                    filter_args["is_neutered"] = True

                qs = models.Cat.objects.filter(**filter_args).order_by("-created")

                paginator = Paginator(qs, 10, orphans=5)

                page = request.GET.get("page", 1)

                cats = paginator.get_page(page)

                return render(request, "cats/search.html", {"form": form, "cats": cats})

        else:

            form = forms.SearchForm()

        return render(request, "cats/search.html", {"form": form})
