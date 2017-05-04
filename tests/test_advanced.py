# -*- coding: utf-8 -*-

from .context import cognitive_textanalytics

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertTrue(cognitive_textanalytics.hmm())


if __name__ == '__main__':
    unittest.main()