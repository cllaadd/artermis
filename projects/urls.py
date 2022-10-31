from django.urls import path
from projects.views import (
    list_projects,
    show_project,
    create_project,
    edit_project,
    delete_project,
)

urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("<int:id>/", show_project, name="show_project"),
    path("create/", create_project, name="create_project"),
    path("<int:id>/edit/", edit_project, name="edit_project"),
    path("<int:id>/delete/", delete_project, name="delete_project"),
]
