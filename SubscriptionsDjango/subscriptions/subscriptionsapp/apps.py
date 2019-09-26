from django.apps import AppConfig


class SubscriptionsappConfig(AppConfig):
    name = 'subscriptionsapp'
    def ready(self):
        # Makes sure all signal handlers are connected
        from . import handlers  # noqa