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

class InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone(object):
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
        'play_beep_volume': 'int',
        'play_beep_time_interval': 'int',
        'play_beep_member': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'play_beep_volume': 'play_beep_volume',
        'play_beep_time_interval': 'play_beep_time_interval',
        'play_beep_member': 'play_beep_member'
    }

    def __init__(self, enable=None, play_beep_volume=None, play_beep_time_interval=None, play_beep_member=None):  # noqa: E501
        """InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._play_beep_volume = None
        self._play_beep_time_interval = None
        self._play_beep_member = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if play_beep_volume is not None:
            self.play_beep_volume = play_beep_volume
        if play_beep_time_interval is not None:
            self.play_beep_time_interval = play_beep_time_interval
        if play_beep_member is not None:
            self.play_beep_member = play_beep_member

    @property
    def enable(self):
        """Gets the enable of this InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.  # noqa: E501

        Whether to play the side tone beep for recorded users while recording. It displays only when auto call recording policy uses the new framework.  # noqa: E501

        :return: The enable of this InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.

        Whether to play the side tone beep for recorded users while recording. It displays only when auto call recording policy uses the new framework.  # noqa: E501

        :param enable: The enable of this InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def play_beep_volume(self):
        """Gets the play_beep_volume of this InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.  # noqa: E501

        The side tone beep volume. It displays only when `enable` is set to `true`.  # noqa: E501

        :return: The play_beep_volume of this InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.  # noqa: E501
        :rtype: int
        """
        return self._play_beep_volume

    @play_beep_volume.setter
    def play_beep_volume(self, play_beep_volume):
        """Sets the play_beep_volume of this InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.

        The side tone beep volume. It displays only when `enable` is set to `true`.  # noqa: E501

        :param play_beep_volume: The play_beep_volume of this InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 20, 40, 60, 80, 100]  # noqa: E501
        if play_beep_volume not in allowed_values:
            raise ValueError(
                "Invalid value for `play_beep_volume` ({0}), must be one of {1}"  # noqa: E501
                .format(play_beep_volume, allowed_values)
            )

        self._play_beep_volume = play_beep_volume

    @property
    def play_beep_time_interval(self):
        """Gets the play_beep_time_interval of this InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.  # noqa: E501

        The beep time interval in seconds. It displays only when the `enable` is set to true.  # noqa: E501

        :return: The play_beep_time_interval of this InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.  # noqa: E501
        :rtype: int
        """
        return self._play_beep_time_interval

    @play_beep_time_interval.setter
    def play_beep_time_interval(self, play_beep_time_interval):
        """Sets the play_beep_time_interval of this InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.

        The beep time interval in seconds. It displays only when the `enable` is set to true.  # noqa: E501

        :param play_beep_time_interval: The play_beep_time_interval of this InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.  # noqa: E501
        :type: int
        """
        allowed_values = [5, 10, 15, 20, 25, 30, 60, 120]  # noqa: E501
        if play_beep_time_interval not in allowed_values:
            raise ValueError(
                "Invalid value for `play_beep_time_interval` ({0}), must be one of {1}"  # noqa: E501
                .format(play_beep_time_interval, allowed_values)
            )

        self._play_beep_time_interval = play_beep_time_interval

    @property
    def play_beep_member(self):
        """Gets the play_beep_member of this InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.  # noqa: E501

        The beep sides. It displays only when the `enable` is set to true.  # noqa: E501

        :return: The play_beep_member of this InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.  # noqa: E501
        :rtype: str
        """
        return self._play_beep_member

    @play_beep_member.setter
    def play_beep_member(self, play_beep_member):
        """Sets the play_beep_member of this InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.

        The beep sides. It displays only when the `enable` is set to true.  # noqa: E501

        :param play_beep_member: The play_beep_member of this InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone.  # noqa: E501
        :type: str
        """
        allowed_values = ["allMember", "recordingSide"]  # noqa: E501
        if play_beep_member not in allowed_values:
            raise ValueError(
                "Invalid value for `play_beep_member` ({0}), must be one of {1}"  # noqa: E501
                .format(play_beep_member, allowed_values)
            )

        self._play_beep_member = play_beep_member

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
        if issubclass(InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone, dict):
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
        if not isinstance(other, InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
