from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from details.forms import EducationalDetailsEditForm
from details.models import EducationalDetail


@login_required
def education_details_home(request):
    details = EducationalDetail.objects.filter(user=request.user).order_by(
        "-year_of_passing"
    )
    for i, detail in enumerate(details):
        detail.__setattr__("index", i + 1)

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


@login_required
def education_details_edit(request, index):
    try:
        detail = EducationalDetail.objects.filter(user=request.user).order_by(
            "-year_of_passing"
        )[index - 1]
    except EducationalDetail.DoesNotExist:
        detail = None
    except IndexError:
        raise Http404
    if request.method == "POST":
        form = EducationalDetailsEditForm(True, request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return redirect("educational-details-home")
        if "__all__" in form.errors:
            form.errors["Others"] = form.errors["__all__"]
            del form.errors["__all__"]
        messages.error(request, form.errors, extra_tags="danger")
    form = EducationalDetailsEditForm(True, instance=detail)
    context = {"form": form}
    return render(
        request,
        "educational_details/educational_details_edit_view.html",
        context=context,
    )


@login_required
@require_http_methods(["POST"])
def education_details_delete(request, index):
    try:
        detail = EducationalDetail.objects.filter(user=request.user).order_by(
            "-year_of_passing"
        )[index - 1]
    except EducationalDetail.DoesNotExist:
        detail = None
    except IndexError:
        raise Http404
    if detail:
        detail.delete()
    else:
        messages.error(request, "Error deleting!", extra_tags="danger")
    return redirect("educational-details-home")
