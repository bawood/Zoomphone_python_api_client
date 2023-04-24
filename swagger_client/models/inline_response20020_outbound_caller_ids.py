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

class InlineResponse20020OutboundCallerIds(object):
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
        'is_default': 'bool',
        'name': 'str',
        'number': 'str'
    }

    attribute_map = {
        'is_default': 'is_default',
        'name': 'name',
        'number': 'number'
    }

    def __init__(self, is_default=None, name=None, number=None):  # noqa: E501
        """InlineResponse20020OutboundCallerIds - a model defined in Swagger"""  # noqa: E501
        self._is_default = None
        self._name = None
        self._number = None
        self.discriminator = None
        if is_default is not None:
            self.is_default = is_default
        if name is not None:
            self.name = name
        if number is not None:
            self.number = number

    @property
    def is_default(self):
        """Gets the is_default of this InlineResponse20020OutboundCallerIds.  # noqa: E501

        Whether the outbound caller ID is the default one: if `true`, the outbound caller ID is the default caller ID.  # noqa: E501

        :return: The is_default of this InlineResponse20020OutboundCallerIds.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this InlineResponse20020OutboundCallerIds.

        Whether the outbound caller ID is the default one: if `true`, the outbound caller ID is the default caller ID.  # noqa: E501

        :param is_default: The is_default of this InlineResponse20020OutboundCallerIds.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def name(self):
        """Gets the name of this InlineResponse20020OutboundCallerIds.  # noqa: E501

        Outbound caller name.  # noqa: E501

        :return: The name of this InlineResponse20020OutboundCallerIds.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20020OutboundCallerIds.

        Outbound caller name.  # noqa: E501

        :param name: The name of this InlineResponse20020OutboundCallerIds.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this InlineResponse20020OutboundCallerIds.  # noqa: E501

        Outbound caller number.  # noqa: E501

        :return: The number of this InlineResponse20020OutboundCallerIds.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this InlineResponse20020OutboundCallerIds.

        Outbound caller number.  # noqa: E501

        :param number: The number of this InlineResponse20020OutboundCallerIds.  # noqa: E501
        :type: str
        """

        self._number = number

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
        if issubclass(InlineResponse20020OutboundCallerIds, dict):
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
        if not isinstance(other, InlineResponse20020OutboundCallerIds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
