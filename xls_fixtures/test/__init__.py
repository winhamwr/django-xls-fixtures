import os
import sys
import logging
import unittest

from django.core.management import call_command
log = logging.getLogger('nose.xls_fixtures')

from test_serializer import *

class test_project(unittest.TestCase):
    def setUp(self):
        self.old_settings = os.environ.get('DJANGO_SETTINGS_MODULE', None)
        self.old_path = sys.path

        os.environ['DJANGO_SETTINGS_MODULE'] = 'xls_fixtures.test.project.settings'
        sys.path.append(os.path.join(os.path.dirname(__file__)))

    def test_project(self):
        call_command('test', 'app')

    def tearDown(self):
        os.environ['DJANGO_SETTINGS_MODULE'] = self.old_settings
        sys.path = self.old_path