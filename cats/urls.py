from django.urls import path, re_path
from . import views as cat_views

app_name = "cats"

urlpatterns = [
    path("<int:pk>/", cat_views.CatDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", cat_views.EditCatView.as_view(), name="edit"),
    path("<int:pk>/photos/", cat_views.CatPhotoView.as_view(), name="photos"),
    path(
        "<int:cat_pk>/photos/<int:photo_pk>/delete/",
        cat_views.delete_photo,
        name="delete-photo",
    ),
    path("<int:pk>/photos/add", cat_views.AddPhotoView.as_view(), name="add-photo"),
    path("search/", cat_views.SearchView.as_view(), name="search"),
]
