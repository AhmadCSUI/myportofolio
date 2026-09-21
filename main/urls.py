from django.urls import path

from main.views import (
    show_main, show_experience, show_education,
    create_education, edit_education, delete_education, get_educations_json,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    # Education CRUD
    path("education/add/", create_education, name="create_education"),
    path("education/<uuid:education_id>/edit/", edit_education, name="edit_education"),
    path("education/<uuid:education_id>/delete/", delete_education, name="delete_education"),
    path("api/educations/", get_educations_json, name="get_educations_json"),
]
