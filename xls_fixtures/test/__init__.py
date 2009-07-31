import os
import sys
import logging

os.environ['DJANGO_SETTINGS_MODULE'] = 'xls_fixtures.test.project.settings'
sys.path.append(os.path.join(os.path.dirname(__file__)))

from django.core.management import call_command
log = logging.getLogger('nose.xls_fixtures')

def setup():
    call_command('test', 'app')
