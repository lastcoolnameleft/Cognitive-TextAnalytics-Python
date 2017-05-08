"""Regression tests for Text Analytics API
"""
import unittest
import logging
from .context import cognitive_textanalytics
from . import config
logging.getLogger('bravado_core').setLevel(logging.ERROR)
logging.getLogger('swagger_spec_validator').setLevel(logging.ERROR)

class LanguageTestSuite(unittest.TestCase):
    """API test cases."""

    def test_detect_language_simple(self):
        """Functional test for Detect Language
        """
        input_text = "it was the best of times"
        client = cognitive_textanalytics.language.Language(config.URL, config.KEY)
        lang = client.detect(input_text)
        self.assertEqual('English', lang)
