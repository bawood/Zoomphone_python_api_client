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

class InlineResponse20039Assignees(object):
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
        'extension_number': 'int',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'extension_number': 'extension_number',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, extension_number=None, id=None, name=None):  # noqa: E501
        """InlineResponse20039Assignees - a model defined in Swagger"""  # noqa: E501
        self._extension_number = None
        self._id = None
        self._name = None
        self.discriminator = None
        if extension_number is not None:
            self.extension_number = extension_number
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def extension_number(self):
        """Gets the extension_number of this InlineResponse20039Assignees.  # noqa: E501

        The extension number of the user's Zoom Phone.  # noqa: E501

        :return: The extension_number of this InlineResponse20039Assignees.  # noqa: E501
        :rtype: int
        """
        return self._extension_number

    @extension_number.setter
    def extension_number(self, extension_number):
        """Sets the extension_number of this InlineResponse20039Assignees.

        The extension number of the user's Zoom Phone.  # noqa: E501

        :param extension_number: The extension_number of this InlineResponse20039Assignees.  # noqa: E501
        :type: int
        """

        self._extension_number = extension_number

    @property
    def id(self):
        """Gets the id of this InlineResponse20039Assignees.  # noqa: E501

        The user ID of the user with the assigned device.  # noqa: E501

        :return: The id of this InlineResponse20039Assignees.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20039Assignees.

        The user ID of the user with the assigned device.  # noqa: E501

        :param id: The id of this InlineResponse20039Assignees.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20039Assignees.  # noqa: E501

        The name of the user.  # noqa: E501

        :return: The name of this InlineResponse20039Assignees.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20039Assignees.

        The name of the user.  # noqa: E501

        :param name: The name of this InlineResponse20039Assignees.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(InlineResponse20039Assignees, dict):
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
        if not isinstance(other, InlineResponse20039Assignees):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
