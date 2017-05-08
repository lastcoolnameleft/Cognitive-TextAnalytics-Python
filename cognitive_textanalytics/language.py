import logging
from bravado.client import SwaggerClient

logging.getLogger('bravado_core').setLevel(logging.ERROR)
logging.getLogger('swagger_spec_validator').setLevel(logging.ERROR)

class Language():
    """Language dection class
    """

    def __init__(self, url, key):
        """Constructor
        """
        self.url = url
        self.key = key
        self.client = SwaggerClient.from_url(url, config={'use_models': False})
        self.headers = {"headers": {"Ocp-Apim-Subscription-Key": key}}

    def request(self, data):
        """Performs detect request

        Args:
            data: Object data for the request

        Returns:
            API Response data (as dictionary)
        """
        return self.client.languages.Detect_Language(
            batchInputV2=data,
            _request_options=self.headers).result()

    def detect(self, input_text):
        """Detect langage for an array of string
        This method is intended to fulfill a simple request
        It expects a string of text to translate and returns the most likely language

        Args:
            input_text: The string to be translated

        Returns:
            A string of the top language detected
        """
        data = dict(documents=[dict(id='id', text=input_text)])
        response = self.request(data)
        result = response['documents'][0]['detectedLanguages'][0]['name']
        return result
    
    def detect_details(self, input_text):
        """Detect langage for an array of string
        This method is intended to fulfill a simple request
        It expects a string of text to translate and returns the full API response

        Args:
            input_text: The string to be translated

        Returns:
            A string of the top language detected
        """
        data = dict(documents=[dict(id='id', text=input_text)])
        return self.request(data)

    def detect_bulk(self, input_array):
        """Detect langage for an array of strings

        Args:
            input_array: Array of strings to be translated

        Returns:
            Array of languages, ordered by the input array
        """

        # Guido bless list comprehension
        data = [dict(id=i, text=x) for i, x in enumerate(input_array, 1)]
        response = self.request(data)
        return result


