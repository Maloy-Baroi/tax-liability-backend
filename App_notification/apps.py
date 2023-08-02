from django.apps import AppConfig


class AppNotificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'App_notification'

    def ready(self):
        import App_notification.signals
