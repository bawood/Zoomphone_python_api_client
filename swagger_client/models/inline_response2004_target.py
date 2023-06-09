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

class InlineResponse2004Target(object):
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
        'extension_number': 'str',
        'id': 'str',
        'phone_number': 'str'
    }

    attribute_map = {
        'display_name': 'display_name',
        'extension_id': 'extension_id',
        'extension_number': 'extension_number',
        'id': 'id',
        'phone_number': 'phone_number'
    }

    def __init__(self, display_name=None, extension_id=None, extension_number=None, id=None, phone_number=None):  # noqa: E501
        """InlineResponse2004Target - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._extension_id = None
        self._extension_number = None
        self._id = None
        self._phone_number = None
        self.discriminator = None
        if display_name is not None:
            self.display_name = display_name
        if extension_id is not None:
            self.extension_id = extension_id
        if extension_number is not None:
            self.extension_number = extension_number
        if id is not None:
            self.id = id
        if phone_number is not None:
            self.phone_number = phone_number

    @property
    def display_name(self):
        """Gets the display_name of this InlineResponse2004Target.  # noqa: E501

        The display name.  # noqa: E501

        :return: The display_name of this InlineResponse2004Target.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InlineResponse2004Target.

        The display name.  # noqa: E501

        :param display_name: The display_name of this InlineResponse2004Target.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def extension_id(self):
        """Gets the extension_id of this InlineResponse2004Target.  # noqa: E501

        The extension ID or contact center setting ID.  # noqa: E501

        :return: The extension_id of this InlineResponse2004Target.  # noqa: E501
        :rtype: str
        """
        return self._extension_id

    @extension_id.setter
    def extension_id(self, extension_id):
        """Sets the extension_id of this InlineResponse2004Target.

        The extension ID or contact center setting ID.  # noqa: E501

        :param extension_id: The extension_id of this InlineResponse2004Target.  # noqa: E501
        :type: str
        """

        self._extension_id = extension_id

    @property
    def extension_number(self):
        """Gets the extension_number of this InlineResponse2004Target.  # noqa: E501

        The extension number.  # noqa: E501

        :return: The extension_number of this InlineResponse2004Target.  # noqa: E501
        :rtype: str
        """
        return self._extension_number

    @extension_number.setter
    def extension_number(self, extension_number):
        """Sets the extension_number of this InlineResponse2004Target.

        The extension number.  # noqa: E501

        :param extension_number: The extension_number of this InlineResponse2004Target.  # noqa: E501
        :type: str
        """

        self._extension_number = extension_number

    @property
    def id(self):
        """Gets the id of this InlineResponse2004Target.  # noqa: E501

        The user, common area, Zoom Room, Cisco/Polycom room, auto receptionist, call queue, or shared line group ID.  # noqa: E501

        :return: The id of this InlineResponse2004Target.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2004Target.

        The user, common area, Zoom Room, Cisco/Polycom room, auto receptionist, call queue, or shared line group ID.  # noqa: E501

        :param id: The id of this InlineResponse2004Target.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def phone_number(self):
        """Gets the phone_number of this InlineResponse2004Target.  # noqa: E501

        The phone number to forward to in E164 format.  # noqa: E501

        :return: The phone_number of this InlineResponse2004Target.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this InlineResponse2004Target.

        The phone number to forward to in E164 format.  # noqa: E501

        :param phone_number: The phone_number of this InlineResponse2004Target.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

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
        if issubclass(InlineResponse2004Target, dict):
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
        if not isinstance(other, InlineResponse2004Target):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
