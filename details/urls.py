from django.urls import path

from .views import general_views, technical_views, educational_views, experience_views

# general
urlpatterns = [
    path("general/", general_views.general_details_home, name="general-details-home"),
    path(
        "general/edit/", general_views.general_details_edit, name="general-details-edit"
    ),
]

# technical
urlpatterns += [
    path(
        "technical/",
        technical_views.technical_details_home,
        name="technical-details-home",
    ),
    path(
        "technical/edit/",
        technical_views.technical_details_edit,
        name="technical-details-edit",
    ),
    # extra URLs
    path(
        "technical/extra-url/new/",
        technical_views.technical_details_url_new,
        name="technical-details-extra-url-new",
    ),
    path(
        "technical/extra-url/<int:index>/edit/",
        technical_views.technical_details_url_edit,
        name="technical-details-extra-url-edit",
    ),
    path(
        "technical/extra-url/<int:index>/delete/",
        technical_views.technical_details_url_delete,
        name="technical-details-extra-url-delete",
    ),
]

# educational
urlpatterns += [
    path(
        "educational/",
        educational_views.education_details_home,
        name="educational-details-home",
    ),
    path(
        "educational/new",
        educational_views.education_details_new,
        name="educational-details-new",
    ),
    path(
        "educational/<int:index>/edit",
        educational_views.education_details_edit,
        name="educational-details-edit",
    ),
    path(
        "educational/<int:index>/delete",
        educational_views.education_details_delete,
        name="educational-details-delete",
    ),
]

# experience
urlpatterns += [
    path(
        "experience/",
        experience_views.experience_home,
        name="experience-home",
    ),
    path(
        "experience/new",
        experience_views.experience_new,
        name="experience-new",
    ),
    path(
        "experience/<int:index>/edit",
        experience_views.experience_edit,
        name="experience-edit",
    ),
    path(
        "experience/<int:index>/delete",
        experience_views.experience_delete,
        name="experience-delete",
    ),
    path(
        "experience/<str:email>/<int:index>/doc",
        experience_views.experience_doc,
        name="experience-doc",
    ),
]
