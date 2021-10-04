from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from details.forms import TechnicalDetailsEditForm, TechnicalDetailsExtraURLsEditForm
from details.models import TechnicalDetail, TechnicalDetailsExtraURL


@login_required
def technical_details_home(request):
    try:
        details = TechnicalDetail.objects.get(user=request.user)
    except TechnicalDetail.DoesNotExist:
        details = None
    context = {
        "details": details,
    }
    return render(
        request, "technical_details/technical_details_view.html", context=context
    )


@login_required
def technical_details_edit(request):
    try:
        details = TechnicalDetail.objects.get(user=request.user)
    except TechnicalDetail.DoesNotExist:
        details = None
    if request.method == "POST":
        form = TechnicalDetailsEditForm(request.POST, instance=details)
        if form.is_valid():
            details = form.save(commit=False)
            if not details.user:
                details.user = request.user
            details.save()
            return redirect("technical-details-home")
        if "__all__" in form.errors:
            form.errors["Others"] = form.errors["__all__"]
            del form.errors["__all__"]
        messages.error(request, form.errors, extra_tags="danger")
    form = TechnicalDetailsEditForm(instance=details)
    return render(
        request, "technical_details/technical_details_edit_view.html", {"form": form}
    )


# extra URLs


@login_required
def technical_details_url_new(request):
    if request.method == "POST":
        form = TechnicalDetailsExtraURLsEditForm(False, request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            if not url.user:
                url.user = request.user
            url.save()
            return redirect("technical-details-home")
        if "__all__" in form.errors:
            form.errors["Others"] = form.errors["__all__"]
            del form.errors["__all__"]
        messages.error(request, form.errors, extra_tags="danger")
    form = TechnicalDetailsExtraURLsEditForm(False)
    return render(
        request,
        "technical_details/technical_details_url_edit_view.html",
        {"form": form},
    )


@login_required
def technical_details_url_edit(request, index):
    try:
        url = TechnicalDetailsExtraURL.objects.filter(user=request.user)[index - 1]
    except TechnicalDetail.DoesNotExist:
        url = None
    except IndexError:
        raise Http404
    if request.method == "POST":
        form = TechnicalDetailsExtraURLsEditForm(True, request.POST, instance=url)
        if form.is_valid():
            form.save()
            return redirect("technical-details-home")
        if "__all__" in form.errors:
            form.errors["Others"] = form.errors["__all__"]
            del form.errors["__all__"]
        messages.error(request, form.errors, extra_tags="danger")
    form = TechnicalDetailsExtraURLsEditForm(instance=url)
    return render(
        request,
        "technical_details/technical_details_url_edit_view.html",
        {"form": form},
    )


@login_required
@require_http_methods(["POST"])
def technical_details_url_delete(request, index):
    try:
        url = TechnicalDetailsExtraURL.objects.filter(user=request.user)[index - 1]
    except TechnicalDetail.DoesNotExist:
        url = None
    except IndexError:
        raise Http404
    if url:
        url.delete()
    else:
        messages.error(request, "Error deleting!", extra_tags="danger")
    return redirect("technical-details-home")
