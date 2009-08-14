from __future__ import with_statement

from django.db.models.loading import get_models
from django.test import TestCase

from fixture.loadable.django_loadable import DjangoFixture
from fixture.django_testcase import FixtureTestCase

from project.app import models
from fixtures import AuthorData, BookData

class FixtureLoadTest(FixtureTestCase):
    datasets = [AuthorData]

    def test_fixture_load(self):
        self.assertTrue(models.Author.objects.count(), 2)

class DependencyLoadTest(FixtureTestCase):
    datasets = [BookData]

    def test_fixture_load(self):
        self.assertTrue(models.Author.objects.count(), 2)
        self.assertTrue(models.Book.objects.count(), 2)

class ManualLoadTest(TestCase):

    def test_fixture_load(self):
        for model in get_models(models):
            assert 0 == model.objects.count()

        dj_fixture = DjangoFixture()
        with dj_fixture.data(AuthorData, BookData):
            assert models.Author.objects.get(first_name='Frank').books.count() == 1

        for model in get_models(models):
            assert 0 == model.objects.count()