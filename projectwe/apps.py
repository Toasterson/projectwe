from django.apps import AppConfig


class ProjectWeConfig(AppConfig):
    name = 'projectwe'

    def ready(self):
        import projectwe.signals
        super(ProjectWeConfig, self).ready()
