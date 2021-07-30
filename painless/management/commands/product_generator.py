from django.core.management.base import BaseCommand
from ..generator.general import CmsDataGenerator, ProductDataGenerator
from django.utils.translation import ugettext_lazy as _
from painless.utils.generators.pictures import pic_producer


class Command(BaseCommand):
    help = 'Create random product'

    def add_arguments(self, parser):
        # parser.add_argument('-f', '--faq', type=int, help=_('Indicates the number of project to be created'))
        # parser.add_argument('-p', '--product', type=int, help=_('Indicates the number of project to be created'))
        # parser.add_argument('-s', '--slider', type=int, help=_('Indicates the number of project to be created'))
        pass

    def handle(self, *args, **kwargs):
        # faq_num = kwargs['faq']
        # product_num = kwargs['product']
        # slider_num = kwargs['slider']
        pass
        data_generator = ProductDataGenerator()
        data_generator.process_create()
        self.stdout.write(
            self.style.SUCCESS(f'Data is Generated.')
        )
