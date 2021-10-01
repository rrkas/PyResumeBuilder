from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from details.forms import GeneralDetailsEditForm
from details.models import GeneralDetails


@login_required
def general_details_home(request):
    try:
        details = GeneralDetails.objects.get(user=request.user)
    except GeneralDetails.DoesNotExist:
        details = None
    context = {
        "details": details,
    }
    return render(request, "general_details/general_details_view.html", context=context)


@login_required
def general_details_edit(request):
    try:
        details = GeneralDetails.objects.get(user=request.user)
    except GeneralDetails.DoesNotExist:
        details = None
    if request.method == "POST":
        form = GeneralDetailsEditForm(request.POST, request.FILES, instance=details)
        if form.is_valid():
            details = form.save(commit=False)
            if not details.user:
                details.user = request.user
            details.save()
            return redirect('general-details-home')
        messages.error(request, form.errors)
    form = GeneralDetailsEditForm(instance=details)
    return render(request, "general_details/general_details_edit_view.html", {"form": form})
