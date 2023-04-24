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

class InlineResponse20071RestrictedCallHours(object):
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
        'modified': 'bool',
        'time_zone': 'InlineResponse20022RestrictedCallHoursTimeZone',
        'allow_internal_calls': 'bool',
        'restricted_hours': 'InlineResponse20071RestrictedCallHoursRestrictedHours',
        'restricted_holiday_hours': 'InlineResponse20071RestrictedCallHoursRestrictedHolidayHours'
    }

    attribute_map = {
        'enable': 'enable',
        'locked': 'locked',
        'locked_by': 'locked_by',
        'modified': 'modified',
        'time_zone': 'time_zone',
        'allow_internal_calls': 'allow_internal_calls',
        'restricted_hours': 'restricted_hours',
        'restricted_holiday_hours': 'restricted_holiday_hours'
    }

    def __init__(self, enable=None, locked=None, locked_by=None, modified=None, time_zone=None, allow_internal_calls=None, restricted_hours=None, restricted_holiday_hours=None):  # noqa: E501
        """InlineResponse20071RestrictedCallHours - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._locked = None
        self._locked_by = None
        self._modified = None
        self._time_zone = None
        self._allow_internal_calls = None
        self._restricted_hours = None
        self._restricted_holiday_hours = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if locked is not None:
            self.locked = locked
        if locked_by is not None:
            self.locked_by = locked_by
        if modified is not None:
            self.modified = modified
        if time_zone is not None:
            self.time_zone = time_zone
        if allow_internal_calls is not None:
            self.allow_internal_calls = allow_internal_calls
        if restricted_hours is not None:
            self.restricted_hours = restricted_hours
        if restricted_holiday_hours is not None:
            self.restricted_holiday_hours = restricted_holiday_hours

    @property
    def enable(self):
        """Gets the enable of this InlineResponse20071RestrictedCallHours.  # noqa: E501

        Whether to define when the user cannot make or accept calls and send SMS. In the restricted hours, calls will follow \"When a call is not answered\" settings. Outbound and inbound emergency calls will still be allowed.  # noqa: E501

        :return: The enable of this InlineResponse20071RestrictedCallHours.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this InlineResponse20071RestrictedCallHours.

        Whether to define when the user cannot make or accept calls and send SMS. In the restricted hours, calls will follow \"When a call is not answered\" settings. Outbound and inbound emergency calls will still be allowed.  # noqa: E501

        :param enable: The enable of this InlineResponse20071RestrictedCallHours.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def locked(self):
        """Gets the locked of this InlineResponse20071RestrictedCallHours.  # noqa: E501

        Whether the senior administrator allows users to modify the current settings.  # noqa: E501

        :return: The locked of this InlineResponse20071RestrictedCallHours.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this InlineResponse20071RestrictedCallHours.

        Whether the senior administrator allows users to modify the current settings.  # noqa: E501

        :param locked: The locked of this InlineResponse20071RestrictedCallHours.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def locked_by(self):
        """Gets the locked_by of this InlineResponse20071RestrictedCallHours.  # noqa: E501

        Which level of administrator prohibits modifying the current settings.  # noqa: E501

        :return: The locked_by of this InlineResponse20071RestrictedCallHours.  # noqa: E501
        :rtype: str
        """
        return self._locked_by

    @locked_by.setter
    def locked_by(self, locked_by):
        """Sets the locked_by of this InlineResponse20071RestrictedCallHours.

        Which level of administrator prohibits modifying the current settings.  # noqa: E501

        :param locked_by: The locked_by of this InlineResponse20071RestrictedCallHours.  # noqa: E501
        :type: str
        """
        allowed_values = ["invalid", "account", "site"]  # noqa: E501
        if locked_by not in allowed_values:
            raise ValueError(
                "Invalid value for `locked_by` ({0}), must be one of {1}"  # noqa: E501
                .format(locked_by, allowed_values)
            )

        self._locked_by = locked_by

    @property
    def modified(self):
        """Gets the modified of this InlineResponse20071RestrictedCallHours.  # noqa: E501

        Whether the current settings have been modified. If modified, they can be reset (displayed when using the new policy framework).  # noqa: E501

        :return: The modified of this InlineResponse20071RestrictedCallHours.  # noqa: E501
        :rtype: bool
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this InlineResponse20071RestrictedCallHours.

        Whether the current settings have been modified. If modified, they can be reset (displayed when using the new policy framework).  # noqa: E501

        :param modified: The modified of this InlineResponse20071RestrictedCallHours.  # noqa: E501
        :type: bool
        """

        self._modified = modified

    @property
    def time_zone(self):
        """Gets the time_zone of this InlineResponse20071RestrictedCallHours.  # noqa: E501


        :return: The time_zone of this InlineResponse20071RestrictedCallHours.  # noqa: E501
        :rtype: InlineResponse20022RestrictedCallHoursTimeZone
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this InlineResponse20071RestrictedCallHours.


        :param time_zone: The time_zone of this InlineResponse20071RestrictedCallHours.  # noqa: E501
        :type: InlineResponse20022RestrictedCallHoursTimeZone
        """

        self._time_zone = time_zone

    @property
    def allow_internal_calls(self):
        """Gets the allow_internal_calls of this InlineResponse20071RestrictedCallHours.  # noqa: E501

        Whether to allow internal calls/SMS during restricted hours.  # noqa: E501

        :return: The allow_internal_calls of this InlineResponse20071RestrictedCallHours.  # noqa: E501
        :rtype: bool
        """
        return self._allow_internal_calls

    @allow_internal_calls.setter
    def allow_internal_calls(self, allow_internal_calls):
        """Sets the allow_internal_calls of this InlineResponse20071RestrictedCallHours.

        Whether to allow internal calls/SMS during restricted hours.  # noqa: E501

        :param allow_internal_calls: The allow_internal_calls of this InlineResponse20071RestrictedCallHours.  # noqa: E501
        :type: bool
        """

        self._allow_internal_calls = allow_internal_calls

    @property
    def restricted_hours(self):
        """Gets the restricted_hours of this InlineResponse20071RestrictedCallHours.  # noqa: E501


        :return: The restricted_hours of this InlineResponse20071RestrictedCallHours.  # noqa: E501
        :rtype: InlineResponse20071RestrictedCallHoursRestrictedHours
        """
        return self._restricted_hours

    @restricted_hours.setter
    def restricted_hours(self, restricted_hours):
        """Sets the restricted_hours of this InlineResponse20071RestrictedCallHours.


        :param restricted_hours: The restricted_hours of this InlineResponse20071RestrictedCallHours.  # noqa: E501
        :type: InlineResponse20071RestrictedCallHoursRestrictedHours
        """

        self._restricted_hours = restricted_hours

    @property
    def restricted_holiday_hours(self):
        """Gets the restricted_holiday_hours of this InlineResponse20071RestrictedCallHours.  # noqa: E501


        :return: The restricted_holiday_hours of this InlineResponse20071RestrictedCallHours.  # noqa: E501
        :rtype: InlineResponse20071RestrictedCallHoursRestrictedHolidayHours
        """
        return self._restricted_holiday_hours

    @restricted_holiday_hours.setter
    def restricted_holiday_hours(self, restricted_holiday_hours):
        """Sets the restricted_holiday_hours of this InlineResponse20071RestrictedCallHours.


        :param restricted_holiday_hours: The restricted_holiday_hours of this InlineResponse20071RestrictedCallHours.  # noqa: E501
        :type: InlineResponse20071RestrictedCallHoursRestrictedHolidayHours
        """

        self._restricted_holiday_hours = restricted_holiday_hours

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
        if issubclass(InlineResponse20071RestrictedCallHours, dict):
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
        if not isinstance(other, InlineResponse20071RestrictedCallHours):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other