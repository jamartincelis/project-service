from django.urls import path

from rule.views import RuleDetail, RuleList


urlpatterns = [
    path('<str:pk>/', RuleDetail.as_view()),
    path('', RuleList.as_view()),
]
