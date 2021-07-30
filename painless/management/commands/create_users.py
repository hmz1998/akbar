from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from django.utils.translation import ugettext_lazy as _

class Command(BaseCommand):
    help = 'Create random normal users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=_('Indicates the number of users to be created'))
        parser.add_argument('-p', '--prefix', type=str, help=_('Define a username prefix'))
        parser.add_argument('-a', '--admin', action='store_true', help=_('Create an admin account'))

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs['prefix']
        admin = kwargs['admin']

        if admin:
            for index, user_info in enumerate(self.get_normal_users(total, prefix)):
                User.objects.create_superuser(**user_info)
                self.stdout.write(self.style.SUCCESS(f'candidate-{index+1} with username: {user_info["username"]} (ADMIN) is created.'))
        else:
            for index, user_info in enumerate(self.get_normal_users(total, prefix)):
                User.objects.create_user(**user_info)
                self.stdout.write(self.style.SUCCESS(f'candidate-{index+1} with username: {user_info["username"]} (TYPICAL) is created.'))

    def get_normal_users(self, total, prefix = None, *args, **kwargs):
        if prefix:
            return [
                {
                    'username': f'{prefix}_{get_random_string()}', 
                    'email':f'candidate.{nth_user}@gmail.com', 
                    'password': '1234',
                }    
                for nth_user in range(total)
            ]
        else:
            return [
                {
                    'username': f'candidate_{get_random_string()}', 
                    'email': f'candidate.{nth_user}@gmail.com', 
                    'password': '1234',
                }    
                for nth_user in range(total)
            ]
