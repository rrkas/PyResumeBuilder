from django.urls import path

from . import views

urlpatterns = [
    path("general/", views.general_details_home, name="general-details-home"),
    path("general/edit/", views.general_details_edit, name="general-details-edit"),
]
