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

class InlineResponse20046AssigneeGreeting(object):
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
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, id=None, name=None):  # noqa: E501
        """InlineResponse20046AssigneeGreeting - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this InlineResponse20046AssigneeGreeting.  # noqa: E501

        The audio prompt file ID. If the audio was removed from the user's audio library, it will be marked with a prefix, `removed_vWby3OZaQlS1nAdmEAqgwA` for example. You can still use this audio ID to get the audio information in [Get an audio item](https://marketplace.zoom.us/docs/api-reference/phone/methods#tag/Audio-Library/operation/GetAudioItem) API.  # noqa: E501

        :return: The id of this InlineResponse20046AssigneeGreeting.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20046AssigneeGreeting.

        The audio prompt file ID. If the audio was removed from the user's audio library, it will be marked with a prefix, `removed_vWby3OZaQlS1nAdmEAqgwA` for example. You can still use this audio ID to get the audio information in [Get an audio item](https://marketplace.zoom.us/docs/api-reference/phone/methods#tag/Audio-Library/operation/GetAudioItem) API.  # noqa: E501

        :param id: The id of this InlineResponse20046AssigneeGreeting.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20046AssigneeGreeting.  # noqa: E501

        Audio prompt file name.  # noqa: E501

        :return: The name of this InlineResponse20046AssigneeGreeting.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20046AssigneeGreeting.

        Audio prompt file name.  # noqa: E501

        :param name: The name of this InlineResponse20046AssigneeGreeting.  # noqa: E501
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
        if issubclass(InlineResponse20046AssigneeGreeting, dict):
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
        if not isinstance(other, InlineResponse20046AssigneeGreeting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
