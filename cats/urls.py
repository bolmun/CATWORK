from django.urls import path, re_path
from . import views as cat_views

app_name = "cats"

urlpatterns = [
    path("<int:pk>", cat_views.CatDetail.as_view(), name="detail"),
    path("search/", cat_views.SearchView.as_view(), name="search"),
]
