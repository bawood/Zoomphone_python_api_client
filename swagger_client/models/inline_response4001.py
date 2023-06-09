# coding: utf-8

"""
    Zoom Phone API

    The Zoom Phone API allows developers to access information from Zoom. You can use this API to build private services or public applications on the [Zoom App Marketplace](http://marketplace.zoom.us). To learn how to get your credentials and create private/public applications, read our [OAuth](https://developers.zoom.us/docs/integrations/oauth/) documentation. All endpoints are available via `https` and are located at `api.zoom.us/v2/`.  For instance, you can list all users on an account via `https://api.zoom.us/v2/users/`.  **Note**: You will get `403` response `Zoom Phone has not been enabled for this account` if the phone account is not set up.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse4001(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'str',
        'message': 'str',
        'errors': 'list[InlineResponse4001Errors]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'errors': 'errors'
    }

    def __init__(self, code=None, message=None, errors=None):  # noqa: E501
        """InlineResponse4001 - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._message = None
        self._errors = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if errors is not None:
            self.errors = errors

    @property
    def code(self):
        """Gets the code of this InlineResponse4001.  # noqa: E501

        Error code  # noqa: E501

        :return: The code of this InlineResponse4001.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InlineResponse4001.

        Error code  # noqa: E501

        :param code: The code of this InlineResponse4001.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this InlineResponse4001.  # noqa: E501

        Brief description of the error.  # noqa: E501

        :return: The message of this InlineResponse4001.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse4001.

        Brief description of the error.  # noqa: E501

        :param message: The message of this InlineResponse4001.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def errors(self):
        """Gets the errors of this InlineResponse4001.  # noqa: E501


        :return: The errors of this InlineResponse4001.  # noqa: E501
        :rtype: list[InlineResponse4001Errors]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this InlineResponse4001.


        :param errors: The errors of this InlineResponse4001.  # noqa: E501
        :type: list[InlineResponse4001Errors]
        """

        self._errors = errors

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse4001, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse4001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
