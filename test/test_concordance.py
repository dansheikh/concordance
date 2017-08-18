import unittest
import app


class TestConcordance(unittest.TestCase):
    @classmethod
    def setupClass(cls):
        app._setup()

    def test_concordance(self):
        corpus = 'resources/the_plane_tree.txt'
        sentences = app._tokenize(corpus)
        (order, table) = app._index(sentences)

        self.assertEqual(order[0], 'a')
        self.assertEqual(table['a']['frequency'], 2)
