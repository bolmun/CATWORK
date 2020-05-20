from django.urls import path
from cats import views as cat_views

app_name = "core"

urlpatterns = [
    path("", cat_views.HomeView.as_view(), name="home"),
]
