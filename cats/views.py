from django.http import Http404
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from users import mixins as user_mixins
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


class EditCatView(UpdateView):

    model = models.Cat
    template_name = "cats/cat_edit.html"
    fields = (
        "name",
        "city",
        "gender",
        "is_neutered",
        "birthdate",
        "estimated_age",
        "appearance",
        "mom_cat",
        "dad_cat",
        "bro_sis",
        "health_condition",
        "rescue_story",
        "adopted",
    )

    def get_object(self, queryset=None):
        cat = super().get_object(queryset=queryset)
        if cat.care_taker.pk != self.request.user.pk:
            raise Http404()
        return cat


class CatPhotoView(user_mixins.LoggedInOnlyView, DetailView):

    model = models.Cat
    template_name = "cats/cat_photos.html"

    def get_objct(self, queryset=None):
        cat = super().get_object(queryset=queryset)
        if cat.care_taker.pk != self.request.user.pk:
            raise Http404()
        return cat


@login_required
def delete_photo(request, cat_pk, photo_pk):
    user = request.user
    try:
        cat = models.Cat.objects.get(pk=cat_pk)
        if cat.care_taker.pk != user.pk:
            messages.error(request, "Cannot delete the photo!")
        else:
            models.Photo.objects.filter(pk=photo_pk).delete()
            messages.success(request, "Photo deleted!")
        return redirect(reverse("cats:photos", kwargs={"pk": cat_pk}))
    except models.Cat.DoesNotExist:
        return redirect(reverse("core:home"))


class AddPhotoView(user_mixins.LoggedInOnlyView, SuccessMessageMixin, FormView):

    model = models.Photo
    template_name = "cats/create_photo.html"
    fields = ("caption", "file")
    form_class = forms.CreatePhotoForm

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.save(pk)
        messages.success(self.request, "Photo added")
        return redirect(reverse("cats:photos", kwargs={"pk": pk}))
