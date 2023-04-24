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

class InlineResponse20078PolicyZoomPhoneOnMobile(object):
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
        'allow_calling_sms_mms': 'bool',
        'enable': 'bool',
        'locked': 'bool',
        'locked_by': 'str'
    }

    attribute_map = {
        'allow_calling_sms_mms': 'allow_calling_sms_mms',
        'enable': 'enable',
        'locked': 'locked',
        'locked_by': 'locked_by'
    }

    def __init__(self, allow_calling_sms_mms=None, enable=None, locked=None, locked_by=None):  # noqa: E501
        """InlineResponse20078PolicyZoomPhoneOnMobile - a model defined in Swagger"""  # noqa: E501
        self._allow_calling_sms_mms = None
        self._enable = None
        self._locked = None
        self._locked_by = None
        self.discriminator = None
        if allow_calling_sms_mms is not None:
            self.allow_calling_sms_mms = allow_calling_sms_mms
        if enable is not None:
            self.enable = enable
        if locked is not None:
            self.locked = locked
        if locked_by is not None:
            self.locked_by = locked_by

    @property
    def allow_calling_sms_mms(self):
        """Gets the allow_calling_sms_mms of this InlineResponse20078PolicyZoomPhoneOnMobile.  # noqa: E501

        Whether to allow Calling and SMS/MMS functions on Mobile.  # noqa: E501

        :return: The allow_calling_sms_mms of this InlineResponse20078PolicyZoomPhoneOnMobile.  # noqa: E501
        :rtype: bool
        """
        return self._allow_calling_sms_mms

    @allow_calling_sms_mms.setter
    def allow_calling_sms_mms(self, allow_calling_sms_mms):
        """Sets the allow_calling_sms_mms of this InlineResponse20078PolicyZoomPhoneOnMobile.

        Whether to allow Calling and SMS/MMS functions on Mobile.  # noqa: E501

        :param allow_calling_sms_mms: The allow_calling_sms_mms of this InlineResponse20078PolicyZoomPhoneOnMobile.  # noqa: E501
        :type: bool
        """

        self._allow_calling_sms_mms = allow_calling_sms_mms

    @property
    def enable(self):
        """Gets the enable of this InlineResponse20078PolicyZoomPhoneOnMobile.  # noqa: E501

        Whether to allow user to use Zoom Phone on mobile clients (iOS, iPad OS and Android).  # noqa: E501

        :return: The enable of this InlineResponse20078PolicyZoomPhoneOnMobile.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this InlineResponse20078PolicyZoomPhoneOnMobile.

        Whether to allow user to use Zoom Phone on mobile clients (iOS, iPad OS and Android).  # noqa: E501

        :param enable: The enable of this InlineResponse20078PolicyZoomPhoneOnMobile.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def locked(self):
        """Gets the locked of this InlineResponse20078PolicyZoomPhoneOnMobile.  # noqa: E501

        Whether the senior administrator allows users to modify the current settings.  # noqa: E501

        :return: The locked of this InlineResponse20078PolicyZoomPhoneOnMobile.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this InlineResponse20078PolicyZoomPhoneOnMobile.

        Whether the senior administrator allows users to modify the current settings.  # noqa: E501

        :param locked: The locked of this InlineResponse20078PolicyZoomPhoneOnMobile.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def locked_by(self):
        """Gets the locked_by of this InlineResponse20078PolicyZoomPhoneOnMobile.  # noqa: E501

        Which level of administrator prohibits modifying the current settings.  # noqa: E501

        :return: The locked_by of this InlineResponse20078PolicyZoomPhoneOnMobile.  # noqa: E501
        :rtype: str
        """
        return self._locked_by

    @locked_by.setter
    def locked_by(self, locked_by):
        """Sets the locked_by of this InlineResponse20078PolicyZoomPhoneOnMobile.

        Which level of administrator prohibits modifying the current settings.  # noqa: E501

        :param locked_by: The locked_by of this InlineResponse20078PolicyZoomPhoneOnMobile.  # noqa: E501
        :type: str
        """
        allowed_values = ["invalid", "account", "user_group", "site", "extension"]  # noqa: E501
        if locked_by not in allowed_values:
            raise ValueError(
                "Invalid value for `locked_by` ({0}), must be one of {1}"  # noqa: E501
                .format(locked_by, allowed_values)
            )

        self._locked_by = locked_by

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
        if issubclass(InlineResponse20078PolicyZoomPhoneOnMobile, dict):
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
        if not isinstance(other, InlineResponse20078PolicyZoomPhoneOnMobile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
