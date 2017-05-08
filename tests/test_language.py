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

    def test_detect_language_details(self):
        """Functional test for Detect Language
        """
        input_text = "it was the best of times"
        client = cognitive_textanalytics.language.Language(config.URL, config.KEY)
        api_response = client.detect_details(input_text)
        self.assertEqual(1, len(api_response['documents']))
        self.assertEqual('id', api_response['documents'][0]['id'])
        # detectedLanguages is closer to spec than auto-generated code (detected_languages)
        self.assertEqual(1, len(api_response['documents'][0]['detectedLanguages']))
        self.assertEqual('English', api_response['documents'][0]['detectedLanguages'][0]['name'])
