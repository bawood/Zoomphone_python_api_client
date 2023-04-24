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

class InlineResponse20042Members(object):
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
        'display_name': 'str',
        'extension_id': 'str',
        'extension_number': 'int',
        'extension_type': 'str'
    }

    attribute_map = {
        'display_name': 'display_name',
        'extension_id': 'extension_id',
        'extension_number': 'extension_number',
        'extension_type': 'extension_type'
    }

    def __init__(self, display_name=None, extension_id=None, extension_number=None, extension_type=None):  # noqa: E501
        """InlineResponse20042Members - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._extension_id = None
        self._extension_number = None
        self._extension_type = None
        self.discriminator = None
        if display_name is not None:
            self.display_name = display_name
        if extension_id is not None:
            self.extension_id = extension_id
        if extension_number is not None:
            self.extension_number = extension_number
        if extension_type is not None:
            self.extension_type = extension_type

    @property
    def display_name(self):
        """Gets the display_name of this InlineResponse20042Members.  # noqa: E501

        Member name.  # noqa: E501

        :return: The display_name of this InlineResponse20042Members.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InlineResponse20042Members.

        Member name.  # noqa: E501

        :param display_name: The display_name of this InlineResponse20042Members.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def extension_id(self):
        """Gets the extension_id of this InlineResponse20042Members.  # noqa: E501

        Extension ID.  # noqa: E501

        :return: The extension_id of this InlineResponse20042Members.  # noqa: E501
        :rtype: str
        """
        return self._extension_id

    @extension_id.setter
    def extension_id(self, extension_id):
        """Sets the extension_id of this InlineResponse20042Members.

        Extension ID.  # noqa: E501

        :param extension_id: The extension_id of this InlineResponse20042Members.  # noqa: E501
        :type: str
        """

        self._extension_id = extension_id

    @property
    def extension_number(self):
        """Gets the extension_number of this InlineResponse20042Members.  # noqa: E501

        Extension number.  # noqa: E501

        :return: The extension_number of this InlineResponse20042Members.  # noqa: E501
        :rtype: int
        """
        return self._extension_number

    @extension_number.setter
    def extension_number(self, extension_number):
        """Sets the extension_number of this InlineResponse20042Members.

        Extension number.  # noqa: E501

        :param extension_number: The extension_number of this InlineResponse20042Members.  # noqa: E501
        :type: int
        """

        self._extension_number = extension_number

    @property
    def extension_type(self):
        """Gets the extension_type of this InlineResponse20042Members.  # noqa: E501

        Extension type  # noqa: E501

        :return: The extension_type of this InlineResponse20042Members.  # noqa: E501
        :rtype: str
        """
        return self._extension_type

    @extension_type.setter
    def extension_type(self, extension_type):
        """Sets the extension_type of this InlineResponse20042Members.

        Extension type  # noqa: E501

        :param extension_type: The extension_type of this InlineResponse20042Members.  # noqa: E501
        :type: str
        """
        allowed_values = ["user", "call_queue", "shared_line_group", "common_area_phone"]  # noqa: E501
        if extension_type not in allowed_values:
            raise ValueError(
                "Invalid value for `extension_type` ({0}), must be one of {1}"  # noqa: E501
                .format(extension_type, allowed_values)
            )

        self._extension_type = extension_type

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
        if issubclass(InlineResponse20042Members, dict):
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
        if not isinstance(other, InlineResponse20042Members):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
