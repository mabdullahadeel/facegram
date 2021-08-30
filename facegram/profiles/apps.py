from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'facegram.profiles'

    def ready(self):
        try:
            import facegram.profiles.signals  # noqa F401
        except ImportError:
            pass
