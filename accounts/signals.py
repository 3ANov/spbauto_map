from django.contrib.auth.models import Group
from django_registration.signals import user_registered


def user_created(sender, user, request, **kwargs):
    group = Group.objects.get(name='users')
    group.user_set.add(user)
    user.save()


user_registered.connect(user_created)
