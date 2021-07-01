from django.apps import AppConfig


class TextanalyzerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'textanalyzer'

    def __str__(self):
        return self.name
