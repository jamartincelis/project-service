from django.urls import path

from project.views import ProjectList, ProjectDetail, NewProjectWidget


urlpatterns = [
    path('new-project-widget/', NewProjectWidget.as_view()),
    path('user/<str:user>/project/', ProjectList.as_view()),
    path('user/<str:user>/project/<str:pk>/', ProjectDetail.as_view()),
]
