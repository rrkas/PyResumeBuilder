from django.shortcuts import render

from .models import HomeMenuItem


def home(request):
    context = {
        "menus": [
            HomeMenuItem(
                image_name="general_details.png",
                url_name="general-details-home",
                menu_name="General Details",
            ),
            HomeMenuItem(
                image_name="technical_details.png",
                url_name="technical-details-home",
                menu_name="Technical Details",
            ),
            HomeMenuItem(
                image_name="educational_details.png",
                url_name="educational-details-home",
                menu_name="Educational Details",
            ),
            HomeMenuItem(
                image_name="experience.png",
                url_name="experience-home",
                menu_name="Experience",
            ),
            HomeMenuItem(
                image_name="skills.png",
                url_name="skills-home",
                menu_name="Skills",
            ),
        ]
    }
    return render(request, "common/home.html", context=context)


def about(request):
    return render(request, "common/about.html")
