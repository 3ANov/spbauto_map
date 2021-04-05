from django.db.models.signals import post_save
from django.dispatch import receiver

from problem_register.models import ProblemLabel
from problem_register.tasks import add_places_task


@receiver(post_save, sender=ProblemLabel, dispatch_uid='save_problem_label_after_change')
def start_task_add_places_info_for_problem(sender, instance, **kwargs):
    print('Запущен сигнал post_save')
    add_places_task.delay(instance.id)

