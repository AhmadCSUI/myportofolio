from django.shortcuts import render
from main.models import Experience, Education
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import EducationForm

# Create your views here.
name = "Ahmad"
full_name = "Ahmad S Zorya"
npm = 2506541894

def show_main(request):
    context = {
        "name": name,
        "npm": npm,
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Sukatidur"
            " Sukakucing"
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": name,
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    json_response = get_educations_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [education.object for education in educations]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name":name,
        "educations_list": educations,
        "title_query": title_query,
    }
    return render(request, "education.html", context)

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:education")

# def show_education(request):
#     json_response = get_educations_json(reqeust)
#     educations = serializers.deserialize(
#             "json",
#             json_response.content.decode("urf-8"),
#         )
#
#     educations = [Education.object for pro
#     context = {
#            "name" : name,
#            "education_list": Education.objects.all(),
#             }
#     return render(request, "education.html", context)

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name":name,
        "form": form,
    }
    return render(request, "education_form.html", context)

def get_educations_json(request):
    title_query = request.GET.get("title", "").strip()
    educations = Education.objects.all()

    if title_query:
        educations = educations.filter(title__icontains=title_query)

    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")
