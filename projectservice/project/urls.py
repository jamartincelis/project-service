from django.urls import path

from project.views import HealthCheckApiView, ProjectDetail, ProjectList


urlpatterns = [
    path('health-check/', HealthCheckApiView.as_view()),
    path('', ProjectList.as_view()),
    path('<str:pk>/', ProjectDetail.as_view()),
]
