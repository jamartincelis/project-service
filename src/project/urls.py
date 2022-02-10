from django.urls import path

from project.views import ProjectList, ProjectDetail, NewProjectWidget


urlpatterns = [
    path('new-project-widget/', NewProjectWidget.as_view()),
    path('', ProjectList.as_view()),
    path('<str:pk>/', ProjectDetail.as_view()),
]
