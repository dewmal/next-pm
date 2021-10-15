from django.urls import path
from .views import project_create

urlpatterns = [
    path("create", project_create)
]