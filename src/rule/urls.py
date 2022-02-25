from django.urls import path

from rule.views import RuleDetail, RuleList


urlpatterns = [
    path('', RuleList.as_view(), name="list_create"),
    path('<str:pk>/', RuleDetail.as_view(), name="detail")
]
