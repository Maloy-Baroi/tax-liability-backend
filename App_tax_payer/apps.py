from django.apps import AppConfig


class AppTaxPayerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'App_tax_payer'

    def ready(self):
        import App_tax_payer.signals
