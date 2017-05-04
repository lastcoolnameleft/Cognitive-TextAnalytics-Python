"""Regression tests for Text Analytics API
"""
import unittest
import cognitive_textanalytics
from . import config

class ApiTestSuite(unittest.TestCase):
    """API test cases."""

    def test_detect_language_api(self):
        """Regression test for Detect Language
        """
        api_instance = cognitive_textanalytics.swagger_client.DefaultApi()
        number_of_languages_to_detect = 2
        ocp_apim_subscription_key = config.KEY
        input_id = "myid"
        input_text = "it was the best of times"
        inputv2 = cognitive_textanalytics.swagger_client.InputV2(id=input_id, text=input_text)
        batch_input_v2 = cognitive_textanalytics.swagger_client.BatchInputV2([inputv2])

        api_response = api_instance.detect_language(
            number_of_languages_to_detect=number_of_languages_to_detect,
            ocp_apim_subscription_key=ocp_apim_subscription_key, batch_input_v2=batch_input_v2)

        self.assertEqual(1, len(api_response.documents))
        self.assertEqual('myid', api_response.documents[0].id)
        self.assertEqual(1, len(api_response.documents[0].detected_languages))
        self.assertEqual('English', api_response.documents[0].detected_languages[0].name)

if __name__ == '__main__':
    unittest.main()
