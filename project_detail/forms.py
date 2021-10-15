from django import forms

from project_detail.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "start_date", "expected_end_date", "git_link", "drive_folder_id"]
