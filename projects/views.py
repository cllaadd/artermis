from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from tasks.models import Task
from projects.forms import ProjectForm
from django.contrib.auth.decorators import login_required

# import pandas as pd
# from plotly.offline import plot
# import plotly.express as px

# @login_required
# def show_timeline(request,id):
#     project = get_object_or_404(Project, id=id)
#     qs = Task.objects.filter(project)
#     tasks_data = [
#         {
#             'Project': project.name,
#             'Start': task.start_date,
#             'Finish': task.due_date,
#             'Responsible': task.assignee
#         } for x in qs
#     ]
#     df = pd.DataFrame(tasks_data)
#     fig = px.timeline(
#         df, x_start="Start", x_end="Finish", y="Project", color="Responsible"
#     )
#     fig.update_yaxes(autorange="reversed")
#     gantt_plot = plot(fig, output_type="div")
#     context = {'plot_div': gantt_plot}
#     return render(request, 'index.html', context)
#  ask 92 how they made thier graph


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "project": project,
    }
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)


@login_required
def edit_project(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("show_project", id)
    else:
        form = ProjectForm(instance=project)
    context = {
        "project": project,
        "form": form,
    }
    return render(request, "projects/edit.html", context)


@login_required
def delete_project(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == "POST":
        project.delete()
        return redirect("show_my_tasks")
    context = {"project": project}
    return render(request, "projects/delete.html", context)
