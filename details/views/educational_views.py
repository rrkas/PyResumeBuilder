from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from details.forms import EducationalDetailsEditForm
from details.models import EducationalDetail


@login_required
def education_details_home(request):
    details = EducationalDetail.objects.filter(user=request.user).order_by(
        "-year_of_passing"
    )
    context = {
        "details": details,
    }
    return render(
        request, "educational_details/educational_details_view.html", context=context
    )


@login_required
def education_details_new(request):
    if request.method == "POST":
        form = EducationalDetailsEditForm(False, request.POST)
        if form.is_valid():
            details = form.save(commit=False)
            details.user = request.user
            details.save()
            return redirect("educational-details-home")
    form = EducationalDetailsEditForm(False)
    context = {
        "form": form,
    }
    return render(
        request,
        "educational_details/educational_details_edit_view.html",
        context=context,
    )
