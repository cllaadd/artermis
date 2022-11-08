from django.urls import path
from tasks.views import (
    create_task,
    show_my_tasks,
    edit_task,
    delete_task,
    # complete_task,
)

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("<int:id>/edit/", edit_task, name="edit_task"),
    path("<int:id>/delete/", delete_task, name="delete_task"),
    # path("<int:id>/complete/", complete_task, name="complete_task"),
    path("mine/", show_my_tasks, name="show_my_tasks"),
]
