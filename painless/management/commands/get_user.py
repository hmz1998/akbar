from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

import random
from django.utils.translation import ugettext_lazy as _

class Command(BaseCommand):
    help = 'If example user is created, you can access it from management.'

    def add_arguments(self, parser):
        parser.add_argument('-p', '--prefix', type=str, help=_('Define a username prefix'))

    def handle(self, *args, **kwargs):
        prefix = kwargs['prefix']

        if prefix:
            users = User.objects.filter(username__startswith = f'{prefix}_')
            user = random.choice(users)
            self.stdout.write(f'username: {user.username}')
        else:
            users = User.objects.filter(username__startswith = f'candidate_')
            user = random.choice(users)
            self.stdout.write(f'username: {user.username}')