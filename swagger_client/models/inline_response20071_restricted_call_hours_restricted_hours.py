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

class InlineResponse20071RestrictedCallHoursRestrictedHours(object):
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
        'twenty_four_seven': 'bool',
        'time_windows': 'list[PhonesitessiteIdpoliciespolicyTypeRestrictedCallHoursRestrictedHoursTimeWindows]'
    }

    attribute_map = {
        'twenty_four_seven': 'twenty_four_seven',
        'time_windows': 'time_windows'
    }

    def __init__(self, twenty_four_seven=None, time_windows=None):  # noqa: E501
        """InlineResponse20071RestrictedCallHoursRestrictedHours - a model defined in Swagger"""  # noqa: E501
        self._twenty_four_seven = None
        self._time_windows = None
        self.discriminator = None
        if twenty_four_seven is not None:
            self.twenty_four_seven = twenty_four_seven
        if time_windows is not None:
            self.time_windows = time_windows

    @property
    def twenty_four_seven(self):
        """Gets the twenty_four_seven of this InlineResponse20071RestrictedCallHoursRestrictedHours.  # noqa: E501

        * `true` — 24 hours, 7 days a week.  * `false` — Custom hours.  # noqa: E501

        :return: The twenty_four_seven of this InlineResponse20071RestrictedCallHoursRestrictedHours.  # noqa: E501
        :rtype: bool
        """
        return self._twenty_four_seven

    @twenty_four_seven.setter
    def twenty_four_seven(self, twenty_four_seven):
        """Sets the twenty_four_seven of this InlineResponse20071RestrictedCallHoursRestrictedHours.

        * `true` — 24 hours, 7 days a week.  * `false` — Custom hours.  # noqa: E501

        :param twenty_four_seven: The twenty_four_seven of this InlineResponse20071RestrictedCallHoursRestrictedHours.  # noqa: E501
        :type: bool
        """

        self._twenty_four_seven = twenty_four_seven

    @property
    def time_windows(self):
        """Gets the time_windows of this InlineResponse20071RestrictedCallHoursRestrictedHours.  # noqa: E501

        The settings for custom hours.  # noqa: E501

        :return: The time_windows of this InlineResponse20071RestrictedCallHoursRestrictedHours.  # noqa: E501
        :rtype: list[PhonesitessiteIdpoliciespolicyTypeRestrictedCallHoursRestrictedHoursTimeWindows]
        """
        return self._time_windows

    @time_windows.setter
    def time_windows(self, time_windows):
        """Sets the time_windows of this InlineResponse20071RestrictedCallHoursRestrictedHours.

        The settings for custom hours.  # noqa: E501

        :param time_windows: The time_windows of this InlineResponse20071RestrictedCallHoursRestrictedHours.  # noqa: E501
        :type: list[PhonesitessiteIdpoliciespolicyTypeRestrictedCallHoursRestrictedHoursTimeWindows]
        """

        self._time_windows = time_windows

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
        if issubclass(InlineResponse20071RestrictedCallHoursRestrictedHours, dict):
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
        if not isinstance(other, InlineResponse20071RestrictedCallHoursRestrictedHours):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
