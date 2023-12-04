from django.urls import path

from . import views

urlpatterns = [
    # ex: /main/
    path("", views.index, name="index"),
    # ex: /main/users/kashiwade
    path("users/<username>", views.users, name="detail"),
]
