from django.shortcuts import render
from main.models import Experience

# Create your views here.

def show_main(request):
    context = {
        "name": "Ahmad",
        "npm": "2506541894",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Sukatidur"
            " Sukakucing"
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Ahmad",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)
