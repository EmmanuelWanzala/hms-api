from django.apps import AppConfig


class HmsappConfig(AppConfig):
    name = 'hmsapp'


    def ready(self):
        import hmsapp.signals