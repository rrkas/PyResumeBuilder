from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from details.forms import SkillsItemEditForm
from details.models import SkillItem


@login_required
def skills_home(request):
    skills = SkillItem.objects.filter(user=request.user).order_by(
        "-skill_level", "skill_name"
    )
    for i, skill in enumerate(skills):
        skill.__setattr__("index", i + 1)

    context = {
        "skills": skills,
    }
    return render(request, "skills/skills_view.html", context=context)


@login_required
def skills_new(request):
    if request.method == "POST":
        form = SkillsItemEditForm(False, request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect("skills-home")
    form = SkillsItemEditForm(False)
    context = {
        "form": form,
    }
    return render(
        request,
        "skills/skills_edit_view.html",
        context=context,
    )


@login_required
def skills_edit(request, index):
    try:
        skill = SkillItem.objects.filter(user=request.user).order_by(
            "-skill_level", "skill_name"
        )[index - 1]
    except SkillItem.DoesNotExist:
        skill = None
    except IndexError:
        raise Http404
    if request.method == "POST":
        form = SkillsItemEditForm(True, request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect("skills-home")
        if "__all__" in form.errors:
            form.errors["Others"] = form.errors["__all__"]
            del form.errors["__all__"]
        messages.error(request, form.errors, extra_tags="danger")
    form = SkillsItemEditForm(True, instance=skill)
    context = {"form": form}
    return render(
        request,
        "skills/skills_edit_view.html",
        context=context,
    )


@login_required
@require_http_methods(["POST"])
def skills_delete(request, index):
    try:
        skill = SkillItem.objects.filter(user=request.user).order_by(
            "-skill_level", "skill_name"
        )[index - 1]
    except SkillItem.DoesNotExist:
        skill = None
    except IndexError:
        raise Http404
    if skill:
        skill.delete()
    else:
        messages.error(request, "Error deleting!", extra_tags="danger")
    return redirect("skills-home")
