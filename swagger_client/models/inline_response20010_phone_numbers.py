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

class InlineResponse20010PhoneNumbers(object):
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
        'id': 'str',
        'number': 'str',
        'source': 'str'
    }

    attribute_map = {
        'id': 'id',
        'number': 'number',
        'source': 'source'
    }

    def __init__(self, id=None, number=None, source=None):  # noqa: E501
        """InlineResponse20010PhoneNumbers - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._number = None
        self._source = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if number is not None:
            self.number = number
        if source is not None:
            self.source = source

    @property
    def id(self):
        """Gets the id of this InlineResponse20010PhoneNumbers.  # noqa: E501

        Unique identifier of the assigned phone number.  # noqa: E501

        :return: The id of this InlineResponse20010PhoneNumbers.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20010PhoneNumbers.

        Unique identifier of the assigned phone number.  # noqa: E501

        :param id: The id of this InlineResponse20010PhoneNumbers.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def number(self):
        """Gets the number of this InlineResponse20010PhoneNumbers.  # noqa: E501

        The phone number.  # noqa: E501

        :return: The number of this InlineResponse20010PhoneNumbers.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this InlineResponse20010PhoneNumbers.

        The phone number.  # noqa: E501

        :param number: The number of this InlineResponse20010PhoneNumbers.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def source(self):
        """Gets the source of this InlineResponse20010PhoneNumbers.  # noqa: E501

        Source  # noqa: E501

        :return: The source of this InlineResponse20010PhoneNumbers.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this InlineResponse20010PhoneNumbers.

        Source  # noqa: E501

        :param source: The source of this InlineResponse20010PhoneNumbers.  # noqa: E501
        :type: str
        """
        allowed_values = ["internal", "external"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

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
        if issubclass(InlineResponse20010PhoneNumbers, dict):
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
        if not isinstance(other, InlineResponse20010PhoneNumbers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
