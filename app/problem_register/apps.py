from django.apps import AppConfig


class ProblemRegisterConfig(AppConfig):
    name = 'problem_register'

    def ready(self):
        import problem_register.signals
