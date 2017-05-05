"""Regression tests for Text Analytics API
"""
import unittest
import logging
from bravado.client import SwaggerClient
from . import config
logging.getLogger('bravado_core').setLevel(logging.ERROR)
logging.getLogger('swagger_spec_validator').setLevel(logging.ERROR)

class ApiTestSuite(unittest.TestCase):
    """API test cases."""

    def test_detect_language_api_simple(self):
        """Regression test for Detect Language
        """
        number_of_languages_to_detect = 2
        input_id = "myid"
        input_text = "it was the best of times"

        headers = {"headers": {"Ocp-Apim-Subscription-Key": config.KEY}}
        client = SwaggerClient.from_url(config.URL, config={'use_models': False})

        batch_data = dict(documents=[dict(id=input_id, text=input_text)])
        api_response = client.languages.Detect_Language(
            batchInputV2=batch_data,
            _request_options=headers).result()

        self.assertEqual(1, len(api_response['documents']))
        self.assertEqual('myid', api_response['documents'][0]['id'])
        # detectedLanguages is closer to spec than auto-generated code (detected_languages)
        self.assertEqual(1, len(api_response['documents'][0]['detectedLanguages']))
        self.assertEqual('English', api_response['documents'][0]['detectedLanguages'][0]['name'])

    def test_detect_language_api_models(self):
        """Regression test for Detect Language
        """
        input_id = "myid"
        input_text = "it was the best of times"

        headers = {"headers": {"Ocp-Apim-Subscription-Key": config.KEY}}
        client = SwaggerClient.from_url(config.URL)

        input_model = client.get_model("InputV2")
        input_data = input_model(id=input_id, text=input_text)
        batch_input_model = client.get_model("BatchInputV2")
        batch_input = batch_input_model(documents=[input_data])
        api_response = client.languages.Detect_Language(
            batchInputV2=batch_input,
            _request_options=headers).result()

        self.assertEqual(1, len(api_response['documents']))
        self.assertEqual('myid', api_response['documents'][0]['id'])
        # detectedLanguages is closer to spec than auto-generated code (detected_languages)
        self.assertEqual(1, len(api_response['documents'][0]['detectedLanguages']))
        self.assertEqual('English', api_response['documents'][0]['detectedLanguages'][0]['name'])
