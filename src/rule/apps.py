from django.apps import AppConfig


class RuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rule'

    def ready(self):
        import rule.signals
