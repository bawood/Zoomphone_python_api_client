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

class InlineResponse200102Firmwares(object):
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
        'device_type': 'str',
        'device_model': 'str',
        'versions': 'list[InlineResponse200102Versions]'
    }

    attribute_map = {
        'device_type': 'device_type',
        'device_model': 'device_model',
        'versions': 'versions'
    }

    def __init__(self, device_type=None, device_model=None, versions=None):  # noqa: E501
        """InlineResponse200102Firmwares - a model defined in Swagger"""  # noqa: E501
        self._device_type = None
        self._device_model = None
        self._versions = None
        self.discriminator = None
        if device_type is not None:
            self.device_type = device_type
        if device_model is not None:
            self.device_model = device_model
        if versions is not None:
            self.versions = versions

    @property
    def device_type(self):
        """Gets the device_type of this InlineResponse200102Firmwares.  # noqa: E501

        Device type.  # noqa: E501

        :return: The device_type of this InlineResponse200102Firmwares.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this InlineResponse200102Firmwares.

        Device type.  # noqa: E501

        :param device_type: The device_type of this InlineResponse200102Firmwares.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def device_model(self):
        """Gets the device_model of this InlineResponse200102Firmwares.  # noqa: E501

        Device model name.  # noqa: E501

        :return: The device_model of this InlineResponse200102Firmwares.  # noqa: E501
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """Sets the device_model of this InlineResponse200102Firmwares.

        Device model name.  # noqa: E501

        :param device_model: The device_model of this InlineResponse200102Firmwares.  # noqa: E501
        :type: str
        """

        self._device_model = device_model

    @property
    def versions(self):
        """Gets the versions of this InlineResponse200102Firmwares.  # noqa: E501

        Firmware versions.  # noqa: E501

        :return: The versions of this InlineResponse200102Firmwares.  # noqa: E501
        :rtype: list[InlineResponse200102Versions]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this InlineResponse200102Firmwares.

        Firmware versions.  # noqa: E501

        :param versions: The versions of this InlineResponse200102Firmwares.  # noqa: E501
        :type: list[InlineResponse200102Versions]
        """

        self._versions = versions

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
        if issubclass(InlineResponse200102Firmwares, dict):
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
        if not isinstance(other, InlineResponse200102Firmwares):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
