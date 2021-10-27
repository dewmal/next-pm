from django import forms

from project_detail.models import Project, Task, Step


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "start_date", "expected_end_date", "git_link", "drive_folder_id"]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "start_time", "expected_hours", "project", "pull_requests","status"]


class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ["name", "status", "start_time", "comment", "end_time", "task", "commits"]
