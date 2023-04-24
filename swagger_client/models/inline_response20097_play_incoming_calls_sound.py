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

class InlineResponse20097PlayIncomingCallsSound(object):
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
        'ring_tone': 'str',
        'duration': 'int'
    }

    attribute_map = {
        'enable': 'enable',
        'ring_tone': 'ring_tone',
        'duration': 'duration'
    }

    def __init__(self, enable=None, ring_tone=None, duration=None):  # noqa: E501
        """InlineResponse20097PlayIncomingCallsSound - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._ring_tone = None
        self._duration = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if ring_tone is not None:
            self.ring_tone = ring_tone
        if duration is not None:
            self.duration = duration

    @property
    def enable(self):
        """Gets the enable of this InlineResponse20097PlayIncomingCallsSound.  # noqa: E501

        Whether to play incoming call sound in Zoom clients.  # noqa: E501

        :return: The enable of this InlineResponse20097PlayIncomingCallsSound.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this InlineResponse20097PlayIncomingCallsSound.

        Whether to play incoming call sound in Zoom clients.  # noqa: E501

        :param enable: The enable of this InlineResponse20097PlayIncomingCallsSound.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def ring_tone(self):
        """Gets the ring_tone of this InlineResponse20097PlayIncomingCallsSound.  # noqa: E501

        Incoming call sound in Zoom clients.  # noqa: E501

        :return: The ring_tone of this InlineResponse20097PlayIncomingCallsSound.  # noqa: E501
        :rtype: str
        """
        return self._ring_tone

    @ring_tone.setter
    def ring_tone(self, ring_tone):
        """Sets the ring_tone of this InlineResponse20097PlayIncomingCallsSound.

        Incoming call sound in Zoom clients.  # noqa: E501

        :param ring_tone: The ring_tone of this InlineResponse20097PlayIncomingCallsSound.  # noqa: E501
        :type: str
        """
        allowed_values = ["ringtone_1", "ringtone_2", "ringtone_3"]  # noqa: E501
        if ring_tone not in allowed_values:
            raise ValueError(
                "Invalid value for `ring_tone` ({0}), must be one of {1}"  # noqa: E501
                .format(ring_tone, allowed_values)
            )

        self._ring_tone = ring_tone

    @property
    def duration(self):
        """Gets the duration of this InlineResponse20097PlayIncomingCallsSound.  # noqa: E501

        Duration (in seconds) between ring tones.  # noqa: E501

        :return: The duration of this InlineResponse20097PlayIncomingCallsSound.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InlineResponse20097PlayIncomingCallsSound.

        Duration (in seconds) between ring tones.  # noqa: E501

        :param duration: The duration of this InlineResponse20097PlayIncomingCallsSound.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 3, 5]  # noqa: E501
        if duration not in allowed_values:
            raise ValueError(
                "Invalid value for `duration` ({0}), must be one of {1}"  # noqa: E501
                .format(duration, allowed_values)
            )

        self._duration = duration

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
        if issubclass(InlineResponse20097PlayIncomingCallsSound, dict):
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
        if not isinstance(other, InlineResponse20097PlayIncomingCallsSound):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
