from django import forms

from project_detail.models import Project, Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "start_date", "expected_end_date", "git_link", "drive_folder_id"]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "start_date", "expected_hours", "project"]
