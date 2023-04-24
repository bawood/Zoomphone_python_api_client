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

class InlineResponse20074ToMembers(object):
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
        'owner': 'InlineResponse20074Owner',
        'phone_number': 'str'
    }

    attribute_map = {
        'display_name': 'display_name',
        'owner': 'owner',
        'phone_number': 'phone_number'
    }

    def __init__(self, display_name=None, owner=None, phone_number=None):  # noqa: E501
        """InlineResponse20074ToMembers - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._owner = None
        self._phone_number = None
        self.discriminator = None
        if display_name is not None:
            self.display_name = display_name
        if owner is not None:
            self.owner = owner
        self.phone_number = phone_number

    @property
    def display_name(self):
        """Gets the display_name of this InlineResponse20074ToMembers.  # noqa: E501

        The participant name.  # noqa: E501

        :return: The display_name of this InlineResponse20074ToMembers.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InlineResponse20074ToMembers.

        The participant name.  # noqa: E501

        :param display_name: The display_name of this InlineResponse20074ToMembers.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def owner(self):
        """Gets the owner of this InlineResponse20074ToMembers.  # noqa: E501


        :return: The owner of this InlineResponse20074ToMembers.  # noqa: E501
        :rtype: InlineResponse20074Owner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this InlineResponse20074ToMembers.


        :param owner: The owner of this InlineResponse20074ToMembers.  # noqa: E501
        :type: InlineResponse20074Owner
        """

        self._owner = owner

    @property
    def phone_number(self):
        """Gets the phone_number of this InlineResponse20074ToMembers.  # noqa: E501

        Receiver's phone number.  # noqa: E501

        :return: The phone_number of this InlineResponse20074ToMembers.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this InlineResponse20074ToMembers.

        Receiver's phone number.  # noqa: E501

        :param phone_number: The phone_number of this InlineResponse20074ToMembers.  # noqa: E501
        :type: str
        """
        if phone_number is None:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

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
        if issubclass(InlineResponse20074ToMembers, dict):
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
        if not isinstance(other, InlineResponse20074ToMembers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other