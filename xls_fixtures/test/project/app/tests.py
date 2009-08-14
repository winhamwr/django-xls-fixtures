from __future__ import with_statement

from django.db.models.loading import get_models
from django.test import TestCase

from django_loadable import DjangoFixture
from fixture import DataSet, style

from project.app import models
from fixtures import AuthorData, BookData

dj_fixture = DjangoFixture(env=models, style=style.NamedDataStyle())

class FixtureLoadTest(TestCase):

    def test_fixture_load(self):
        for model in get_models(models):
            assert 0 == model.objects.count()

        with dj_fixture.data(AuthorData, BookData):
            assert models.Author.objects.get(first_name='Frank').books.count() == 1

        for model in get_models(models):
            assert 0 == model.objects.count()