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

class DevicesSyncBody(object):
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
        'level': 'int',
        'site_id': 'str'
    }

    attribute_map = {
        'level': 'level',
        'site_id': 'site_id'
    }

    def __init__(self, level=None, site_id=None):  # noqa: E501
        """DevicesSyncBody - a model defined in Swagger"""  # noqa: E501
        self._level = None
        self._site_id = None
        self.discriminator = None
        self.level = level
        if site_id is not None:
            self.site_id = site_id

    @property
    def level(self):
        """Gets the level of this DevicesSyncBody.  # noqa: E501

        Deskphone sync level: 1 - account level, 2 - site level.  # noqa: E501

        :return: The level of this DevicesSyncBody.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this DevicesSyncBody.

        Deskphone sync level: 1 - account level, 2 - site level.  # noqa: E501

        :param level: The level of this DevicesSyncBody.  # noqa: E501
        :type: int
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

    @property
    def site_id(self):
        """Gets the site_id of this DevicesSyncBody.  # noqa: E501

        Site ID.  # noqa: E501

        :return: The site_id of this DevicesSyncBody.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this DevicesSyncBody.

        Site ID.  # noqa: E501

        :param site_id: The site_id of this DevicesSyncBody.  # noqa: E501
        :type: str
        """

        self._site_id = site_id

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
        if issubclass(DevicesSyncBody, dict):
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
        if not isinstance(other, DevicesSyncBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
