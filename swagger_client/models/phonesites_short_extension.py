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

class PhonesitesShortExtension(object):
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
        'length': 'int'
    }

    attribute_map = {
        'length': 'length'
    }

    def __init__(self, length=3):  # noqa: E501
        """PhonesitesShortExtension - a model defined in Swagger"""  # noqa: E501
        self._length = None
        self.discriminator = None
        if length is not None:
            self.length = length

    @property
    def length(self):
        """Gets the length of this PhonesitesShortExtension.  # noqa: E501

        The length of short extension numbers for the site.  Since there is a default 6-digit limit on extensions, the short extension can be two to five digits and the length of site code added to the length of short extension can not exceed a value of `6` (i.e., length of `site_code`+ length of `short_extension` should always be less than or equal to 6).  # noqa: E501

        :return: The length of this PhonesitesShortExtension.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this PhonesitesShortExtension.

        The length of short extension numbers for the site.  Since there is a default 6-digit limit on extensions, the short extension can be two to five digits and the length of site code added to the length of short extension can not exceed a value of `6` (i.e., length of `site_code`+ length of `short_extension` should always be less than or equal to 6).  # noqa: E501

        :param length: The length of this PhonesitesShortExtension.  # noqa: E501
        :type: int
        """

        self._length = length

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
        if issubclass(PhonesitesShortExtension, dict):
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
        if not isinstance(other, PhonesitesShortExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other