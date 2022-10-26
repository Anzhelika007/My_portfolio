from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.index_render, name="index"),
    path("<int:id>/", views.project_detail, name="project_detail"),
]