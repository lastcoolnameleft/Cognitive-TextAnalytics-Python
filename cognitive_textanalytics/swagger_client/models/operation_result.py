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


class OperationResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, status=None, created_date_time=None, last_action_date_time=None, operation_type=None, operation_processing_result=None, message=None):
        """
        OperationResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'str',
            'created_date_time': 'datetime',
            'last_action_date_time': 'datetime',
            'operation_type': 'str',
            'operation_processing_result': 'OperationProcessingResult',
            'message': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'created_date_time': 'createdDateTime',
            'last_action_date_time': 'lastActionDateTime',
            'operation_type': 'operationType',
            'operation_processing_result': 'operationProcessingResult',
            'message': 'message'
        }

        self._status = status
        self._created_date_time = created_date_time
        self._last_action_date_time = last_action_date_time
        self._operation_type = operation_type
        self._operation_processing_result = operation_processing_result
        self._message = message

    @property
    def status(self):
        """
        Gets the status of this OperationResult.
        Operation status.

        :return: The status of this OperationResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this OperationResult.
        Operation status.

        :param status: The status of this OperationResult.
        :type: str
        """
        allowed_values = ["notStarted", "running", "failed", "cancelled", "succeeded"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created_date_time(self):
        """
        Gets the created_date_time of this OperationResult.
        Operation creation date time (ISO 8601 literal).

        :return: The created_date_time of this OperationResult.
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """
        Sets the created_date_time of this OperationResult.
        Operation creation date time (ISO 8601 literal).

        :param created_date_time: The created_date_time of this OperationResult.
        :type: datetime
        """

        self._created_date_time = created_date_time

    @property
    def last_action_date_time(self):
        """
        Gets the last_action_date_time of this OperationResult.
        Operation last status change date time (ISO 8601 literal).

        :return: The last_action_date_time of this OperationResult.
        :rtype: datetime
        """
        return self._last_action_date_time

    @last_action_date_time.setter
    def last_action_date_time(self, last_action_date_time):
        """
        Sets the last_action_date_time of this OperationResult.
        Operation last status change date time (ISO 8601 literal).

        :param last_action_date_time: The last_action_date_time of this OperationResult.
        :type: datetime
        """

        self._last_action_date_time = last_action_date_time

    @property
    def operation_type(self):
        """
        Gets the operation_type of this OperationResult.
        Name of API endpoint that created the operation.

        :return: The operation_type of this OperationResult.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this OperationResult.
        Name of API endpoint that created the operation.

        :param operation_type: The operation_type of this OperationResult.
        :type: str
        """

        self._operation_type = operation_type

    @property
    def operation_processing_result(self):
        """
        Gets the operation_processing_result of this OperationResult.
        Operation result. Specific format varies according to the operation type. Exists only in case the operation has reached a 'Succeeded' state.

        :return: The operation_processing_result of this OperationResult.
        :rtype: OperationProcessingResult
        """
        return self._operation_processing_result

    @operation_processing_result.setter
    def operation_processing_result(self, operation_processing_result):
        """
        Sets the operation_processing_result of this OperationResult.
        Operation result. Specific format varies according to the operation type. Exists only in case the operation has reached a 'Succeeded' state.

        :param operation_processing_result: The operation_processing_result of this OperationResult.
        :type: OperationProcessingResult
        """

        self._operation_processing_result = operation_processing_result

    @property
    def message(self):
        """
        Gets the message of this OperationResult.
        Error message. Exists only in case the operation has reached a 'Failed' state.

        :return: The message of this OperationResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this OperationResult.
        Error message. Exists only in case the operation has reached a 'Failed' state.

        :param message: The message of this OperationResult.
        :type: str
        """

        self._message = message

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
        if not isinstance(other, OperationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
