from django.urls import path

from . import general_views

urlpatterns = [
    path("general/", general_views.general_details_home, name="general-details-home"),
    path("general/edit/", general_views.general_details_edit, name="general-details-edit"),
]
