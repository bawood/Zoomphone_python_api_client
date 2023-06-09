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

class InlineResponse20044RestrictedCallHours(object):
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
        'enable': 'bool',
        'locked': 'bool',
        'locked_by': 'str',
        'time_zone': 'InlineResponse20044RestrictedCallHoursTimeZone',
        'restricted_hours_applied': 'bool',
        'restricted_holiday_hours_applied': 'bool',
        'allow_internal_calls': 'bool'
    }

    attribute_map = {
        'enable': 'enable',
        'locked': 'locked',
        'locked_by': 'locked_by',
        'time_zone': 'time_zone',
        'restricted_hours_applied': 'restricted_hours_applied',
        'restricted_holiday_hours_applied': 'restricted_holiday_hours_applied',
        'allow_internal_calls': 'allow_internal_calls'
    }

    def __init__(self, enable=None, locked=None, locked_by=None, time_zone=None, restricted_hours_applied=None, restricted_holiday_hours_applied=None, allow_internal_calls=None):  # noqa: E501
        """InlineResponse20044RestrictedCallHours - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._locked = None
        self._locked_by = None
        self._time_zone = None
        self._restricted_hours_applied = None
        self._restricted_holiday_hours_applied = None
        self._allow_internal_calls = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if locked is not None:
            self.locked = locked
        if locked_by is not None:
            self.locked_by = locked_by
        if time_zone is not None:
            self.time_zone = time_zone
        if restricted_hours_applied is not None:
            self.restricted_hours_applied = restricted_hours_applied
        if restricted_holiday_hours_applied is not None:
            self.restricted_holiday_hours_applied = restricted_holiday_hours_applied
        if allow_internal_calls is not None:
            self.allow_internal_calls = allow_internal_calls

    @property
    def enable(self):
        """Gets the enable of this InlineResponse20044RestrictedCallHours.  # noqa: E501


        :return: The enable of this InlineResponse20044RestrictedCallHours.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this InlineResponse20044RestrictedCallHours.


        :param enable: The enable of this InlineResponse20044RestrictedCallHours.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def locked(self):
        """Gets the locked of this InlineResponse20044RestrictedCallHours.  # noqa: E501

        Whether the senior administrator allows users to modify the current settings.  # noqa: E501

        :return: The locked of this InlineResponse20044RestrictedCallHours.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this InlineResponse20044RestrictedCallHours.

        Whether the senior administrator allows users to modify the current settings.  # noqa: E501

        :param locked: The locked of this InlineResponse20044RestrictedCallHours.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def locked_by(self):
        """Gets the locked_by of this InlineResponse20044RestrictedCallHours.  # noqa: E501

        Which level of administrator prohibits the modification of the current settings.  # noqa: E501

        :return: The locked_by of this InlineResponse20044RestrictedCallHours.  # noqa: E501
        :rtype: str
        """
        return self._locked_by

    @locked_by.setter
    def locked_by(self, locked_by):
        """Sets the locked_by of this InlineResponse20044RestrictedCallHours.

        Which level of administrator prohibits the modification of the current settings.  # noqa: E501

        :param locked_by: The locked_by of this InlineResponse20044RestrictedCallHours.  # noqa: E501
        :type: str
        """
        allowed_values = ["invalid", "account"]  # noqa: E501
        if locked_by not in allowed_values:
            raise ValueError(
                "Invalid value for `locked_by` ({0}), must be one of {1}"  # noqa: E501
                .format(locked_by, allowed_values)
            )

        self._locked_by = locked_by

    @property
    def time_zone(self):
        """Gets the time_zone of this InlineResponse20044RestrictedCallHours.  # noqa: E501


        :return: The time_zone of this InlineResponse20044RestrictedCallHours.  # noqa: E501
        :rtype: InlineResponse20044RestrictedCallHoursTimeZone
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this InlineResponse20044RestrictedCallHours.


        :param time_zone: The time_zone of this InlineResponse20044RestrictedCallHours.  # noqa: E501
        :type: InlineResponse20044RestrictedCallHoursTimeZone
        """

        self._time_zone = time_zone

    @property
    def restricted_hours_applied(self):
        """Gets the restricted_hours_applied of this InlineResponse20044RestrictedCallHours.  # noqa: E501

        Whether restricted hours has been applied.  # noqa: E501

        :return: The restricted_hours_applied of this InlineResponse20044RestrictedCallHours.  # noqa: E501
        :rtype: bool
        """
        return self._restricted_hours_applied

    @restricted_hours_applied.setter
    def restricted_hours_applied(self, restricted_hours_applied):
        """Sets the restricted_hours_applied of this InlineResponse20044RestrictedCallHours.

        Whether restricted hours has been applied.  # noqa: E501

        :param restricted_hours_applied: The restricted_hours_applied of this InlineResponse20044RestrictedCallHours.  # noqa: E501
        :type: bool
        """

        self._restricted_hours_applied = restricted_hours_applied

    @property
    def restricted_holiday_hours_applied(self):
        """Gets the restricted_holiday_hours_applied of this InlineResponse20044RestrictedCallHours.  # noqa: E501

        Whether restricted holiday hours has been applied.  # noqa: E501

        :return: The restricted_holiday_hours_applied of this InlineResponse20044RestrictedCallHours.  # noqa: E501
        :rtype: bool
        """
        return self._restricted_holiday_hours_applied

    @restricted_holiday_hours_applied.setter
    def restricted_holiday_hours_applied(self, restricted_holiday_hours_applied):
        """Sets the restricted_holiday_hours_applied of this InlineResponse20044RestrictedCallHours.

        Whether restricted holiday hours has been applied.  # noqa: E501

        :param restricted_holiday_hours_applied: The restricted_holiday_hours_applied of this InlineResponse20044RestrictedCallHours.  # noqa: E501
        :type: bool
        """

        self._restricted_holiday_hours_applied = restricted_holiday_hours_applied

    @property
    def allow_internal_calls(self):
        """Gets the allow_internal_calls of this InlineResponse20044RestrictedCallHours.  # noqa: E501

        Whether to allow internal calls/SMS during restricted hours.  # noqa: E501

        :return: The allow_internal_calls of this InlineResponse20044RestrictedCallHours.  # noqa: E501
        :rtype: bool
        """
        return self._allow_internal_calls

    @allow_internal_calls.setter
    def allow_internal_calls(self, allow_internal_calls):
        """Sets the allow_internal_calls of this InlineResponse20044RestrictedCallHours.

        Whether to allow internal calls/SMS during restricted hours.  # noqa: E501

        :param allow_internal_calls: The allow_internal_calls of this InlineResponse20044RestrictedCallHours.  # noqa: E501
        :type: bool
        """

        self._allow_internal_calls = allow_internal_calls

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
        if issubclass(InlineResponse20044RestrictedCallHours, dict):
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
        if not isinstance(other, InlineResponse20044RestrictedCallHours):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
