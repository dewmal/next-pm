"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from graphene_django.views import GraphQLView

from next_pm.urls import urlpatterns as next_pm_urls
from project_detail.urls import urlpatterns as project_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(next_pm_urls)),
    url(r'^project/', include(project_urls)),
    url(r"graphql", GraphQLView.as_view(graphiql=True)),
]
