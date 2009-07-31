from __future__ import with_statement

from django.test import TestCase

from django_loadable import DjangoFixture
from fixture import DataSet, style

from project.app import models
from fixtures import *

dj_fixture = DjangoFixture(env=models, style=style.NamedDataStyle())

class FixtureLoadTest(TestCase):

    def test_fixture_load(self):
        assert_empty(models)
        with dj_fixture.data(AuthorData, BookData):
            assert models.Author.objects.get(first_name='Frank').books.count() == 1
        assert_empty(models)