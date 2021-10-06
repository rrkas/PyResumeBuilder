from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from details.forms import ExperienceItemEditForm
from details.models import ExperienceItem


@login_required
def experience_home(request):
    experience = ExperienceItem.objects.filter(user=request.user).order_by(
        "-start_date"
    )
    for i, item in enumerate(experience):
        item.__setattr__("index", i + 1)

    context = {
        "experience": experience,
    }
    return render(request, "experience/experience_view.html", context=context)


@login_required
def experience_new(request):
    if request.method == "POST":
        form = ExperienceItemEditForm(False, request.POST)
        if form.is_valid():
            details = form.save(commit=False)
            details.user = request.user
            details.save()
            return redirect("experience-home")
    form = ExperienceItemEditForm(False)
    context = {
        "form": form,
    }
    return render(
        request,
        "experience/experience_edit_view.html",
        context=context,
    )


@login_required
def experience_edit(request, index):
    try:
        detail = ExperienceItem.objects.filter(user=request.user).order_by(
            "-start_date"
        )[index - 1]
    except ExperienceItem.DoesNotExist:
        detail = None
    except IndexError:
        raise Http404
    if request.method == "POST":
        form = ExperienceItemEditForm(True, request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return redirect("experience-home")
        if "__all__" in form.errors:
            form.errors["Others"] = form.errors["__all__"]
            del form.errors["__all__"]
        messages.error(request, form.errors, extra_tags="danger")
    form = ExperienceItemEditForm(True, instance=detail)
    context = {"form": form}
    return render(
        request,
        "experience/experience_edit_view.html",
        context=context,
    )


@login_required
@require_http_methods(["POST"])
def experience_delete(request, index):
    try:
        detail = ExperienceItem.objects.filter(user=request.user).order_by(
            "-start_date"
        )[index - 1]
    except ExperienceItem.DoesNotExist:
        detail = None
    except IndexError:
        raise Http404
    if detail:
        detail.delete()
    else:
        messages.error(request, "Error deleting!", extra_tags="danger")
    return redirect("experience-home")
