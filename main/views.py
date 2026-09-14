from django.shortcuts import render
from main.models import Experience, Education

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
    context = {
           "name" : name,
           "education_list": Education.objects.all(),
            }
    return render(request, "education.html", context)
