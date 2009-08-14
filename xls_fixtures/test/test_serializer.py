import unittest, os.path

from xls_fixtures.serializer import Deserializer

class test_deserialize(unittest.TestCase):

    def test_book_load(self):
        test_book = open(
            os.path.dirname(__file__),
            'project',
            'app',
            'fixtures',
            'no_relations.xls', 'rb')

        book_data = test_book.read()
        ds = Deserializer(book_data)
