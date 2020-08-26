"""
Management command for updating entitlements modes.
"""


import logging
from textwrap import dedent

from django.core.management import BaseCommand

from entitlements.models import CourseEntitlement

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


class Command(BaseCommand):
    """
    Management command for updating entitlements mode.

    Example usage:

    # Process entitlement for given user_id, order_number and new mode:
    $ ./manage.py lms --settings=devstack_docker update_entitlement_mode \
    <user_id> <order_number> <new_mode>
    """
    help = dedent(__doc__).strip()

    def add_arguments(self, parser):
        parser.add_argument(
            'user_id',
            help='User id of entitlement'
        )

        parser.add_argument(
            'order_number',
            help='Order number of entitlement'
        )

        parser.add_argument(
            'entitlement_mode',
            help='Entitlement mode to change to.'
        )

    def handle(self, *args, **options):
        logger.info('Updating entitlement_mode for provided Entitlement.')

        user_id = options['user_id']
        order_number = options['order_number']
        entitlement_mode = options['entitlement_mode']

        CourseEntitlement.objects.update_or_create(
            user_id=user_id, order_number=order_number,
            defaults={'mode': entitlement_mode},
        )

        logger.info('entitlement_mode successfully updated for Entitlement.')
