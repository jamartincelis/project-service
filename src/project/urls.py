from django.urls import path

from project.views import ProjectList, ProjectDetail, NewProjectWidget


urlpatterns = [
    path('new-project-widget/', NewProjectWidget.as_view(), name="new-project-widget"),
    path('', ProjectList.as_view(), name="list_create"),
    path('<str:pk>/', ProjectDetail.as_view(), name="detail")
]
