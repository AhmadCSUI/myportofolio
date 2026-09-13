from django.shortcuts import render
from main.models import Experience, Docs

# Create your views here.
full_name = "Ahmad S. Zorya"
name = "Ahmad"
npm = "2506541894"
likes = {"cats", "kittens", "substantive discussion"}
dislikes = {"benjamin netanyahu", "idle talks", "insincerity"}

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
        "name":name,
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_docs(request):
    context = {
            "name": name,
<<<<<<< Updated upstream
            "docs_list": Docs.objects.all(),
=======
            "docs_list" = Docs.objects.all(),
>>>>>>> Stashed changes
            }
    return render(request, "docs.html", context)
