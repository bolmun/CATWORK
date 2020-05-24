from django.urls import path, re_path
from . import views as cat_views

app_name = "cats"

urlpatterns = [
    path("<int:pk>", cat_views.cat_detail, name="detail"),
    path("search/", cat_views.search, name="search"),
]
