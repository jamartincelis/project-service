from django.urls import path

from monitoring.views import HealthCheckApiView, SentryApiView


urlpatterns = [
    path('health-check/', HealthCheckApiView.as_view()),
    path('sentry/', SentryApiView.as_view()),
]
