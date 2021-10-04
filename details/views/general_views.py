from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from details.forms import GeneralDetailsEditForm
from details.models import GeneralDetail


@login_required
def general_details_home(request):
    try:
        details = GeneralDetail.objects.get(user=request.user)
    except GeneralDetail.DoesNotExist:
        details = None
    context = {
        "details": details,
    }
    return render(request, "general_details/general_details_view.html", context=context)


@login_required
def general_details_edit(request):
    try:
        details = GeneralDetail.objects.get(user=request.user)
    except GeneralDetail.DoesNotExist:
        details = None
    if request.method == "POST":
        form = GeneralDetailsEditForm(request.POST, request.FILES, instance=details)
        if form.is_valid():
            details = form.save(commit=False)
            if not details.user:
                details.user = request.user
            details.save()
            return redirect("general-details-home")
        if "__all__" in form.errors:
            form.errors["Others"] = form.errors["__all__"]
            del form.errors["__all__"]
        messages.error(request, form.errors, extra_tags="danger")
    form = GeneralDetailsEditForm(instance=details)
    return render(
        request, "general_details/general_details_edit_view.html", {"form": form}
    )
