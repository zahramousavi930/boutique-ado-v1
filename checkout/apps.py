from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals

class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'
