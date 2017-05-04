# coding: utf-8

"""
    Azure Machine Learning - Text Analytics

    The Text Analytics API is a suite of text analytics web services built with Azure Machine Learning.   The API can be used to analyze unstructured text for tasks such as sentiment analysis, key phrase extraction and language detection.   No training data is needed to use this API; just bring your text data.   This API uses advanced natural language processing techniques to deliver best in class predictions.    Further documentation can be found in https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-text-analytics-quick-start

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class KeyPhraseBatchResultItemV2(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, key_phrases=None, id=None):
        """
        KeyPhraseBatchResultItemV2 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'key_phrases': 'list[str]',
            'id': 'str'
        }

        self.attribute_map = {
            'key_phrases': 'keyPhrases',
            'id': 'id'
        }

        self._key_phrases = key_phrases
        self._id = id

    @property
    def key_phrases(self):
        """
        Gets the key_phrases of this KeyPhraseBatchResultItemV2.
        A list of representative words or phrases. The number of key phrases returned is proportional to the number of words in the input document.

        :return: The key_phrases of this KeyPhraseBatchResultItemV2.
        :rtype: list[str]
        """
        return self._key_phrases

    @key_phrases.setter
    def key_phrases(self, key_phrases):
        """
        Sets the key_phrases of this KeyPhraseBatchResultItemV2.
        A list of representative words or phrases. The number of key phrases returned is proportional to the number of words in the input document.

        :param key_phrases: The key_phrases of this KeyPhraseBatchResultItemV2.
        :type: list[str]
        """

        self._key_phrases = key_phrases

    @property
    def id(self):
        """
        Gets the id of this KeyPhraseBatchResultItemV2.
        Unique document identifier.

        :return: The id of this KeyPhraseBatchResultItemV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this KeyPhraseBatchResultItemV2.
        Unique document identifier.

        :param id: The id of this KeyPhraseBatchResultItemV2.
        :type: str
        """

        self._id = id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, KeyPhraseBatchResultItemV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
