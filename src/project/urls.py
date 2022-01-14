from django.urls import path

from project.views import ProjectList, ProjectDetail, NewProjectWidget


urlpatterns = [
    path('new-project-widget/', NewProjectWidget.as_view()),
    path('user/<str:user>/projects/', ProjectList.as_view()),
    path('user/<str:user>/projects/<str:pk>/', ProjectDetail.as_view()),
]
