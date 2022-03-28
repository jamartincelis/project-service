from django.urls import path

from project.views import ProjectList, ProjectDetail, Savings


urlpatterns = [
    path('', ProjectList.as_view(), name="list_create"),
    path('savings/', Savings.as_view(), name="savings"),
    path('<str:pk>/', ProjectDetail.as_view(), name="detail")
]
