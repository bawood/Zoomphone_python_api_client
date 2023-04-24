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

class InlineResponse20037CallerQosQos(object):
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
        'avg_loss': 'str',
        'bitrate': 'str',
        'jitter': 'str',
        'max_loss': 'str',
        'mos': 'str',
        'network_delay': 'str'
    }

    attribute_map = {
        'avg_loss': 'avg_loss',
        'bitrate': 'bitrate',
        'jitter': 'jitter',
        'max_loss': 'max_loss',
        'mos': 'mos',
        'network_delay': 'network_delay'
    }

    def __init__(self, avg_loss=None, bitrate=None, jitter=None, max_loss=None, mos=None, network_delay=None):  # noqa: E501
        """InlineResponse20037CallerQosQos - a model defined in Swagger"""  # noqa: E501
        self._avg_loss = None
        self._bitrate = None
        self._jitter = None
        self._max_loss = None
        self._mos = None
        self._network_delay = None
        self.discriminator = None
        if avg_loss is not None:
            self.avg_loss = avg_loss
        if bitrate is not None:
            self.bitrate = bitrate
        if jitter is not None:
            self.jitter = jitter
        if max_loss is not None:
            self.max_loss = max_loss
        if mos is not None:
            self.mos = mos
        if network_delay is not None:
            self.network_delay = network_delay

    @property
    def avg_loss(self):
        """Gets the avg_loss of this InlineResponse20037CallerQosQos.  # noqa: E501

        The average amount of packet loss. For example, the percentage of packets that fail to arrive at their destination.  # noqa: E501

        :return: The avg_loss of this InlineResponse20037CallerQosQos.  # noqa: E501
        :rtype: str
        """
        return self._avg_loss

    @avg_loss.setter
    def avg_loss(self, avg_loss):
        """Sets the avg_loss of this InlineResponse20037CallerQosQos.

        The average amount of packet loss. For example, the percentage of packets that fail to arrive at their destination.  # noqa: E501

        :param avg_loss: The avg_loss of this InlineResponse20037CallerQosQos.  # noqa: E501
        :type: str
        """

        self._avg_loss = avg_loss

    @property
    def bitrate(self):
        """Gets the bitrate of this InlineResponse20037CallerQosQos.  # noqa: E501

        The number of bits per second, in kbps, that can be transmitted along a digital network.  # noqa: E501

        :return: The bitrate of this InlineResponse20037CallerQosQos.  # noqa: E501
        :rtype: str
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this InlineResponse20037CallerQosQos.

        The number of bits per second, in kbps, that can be transmitted along a digital network.  # noqa: E501

        :param bitrate: The bitrate of this InlineResponse20037CallerQosQos.  # noqa: E501
        :type: str
        """

        self._bitrate = bitrate

    @property
    def jitter(self):
        """Gets the jitter of this InlineResponse20037CallerQosQos.  # noqa: E501

        The variation in the delay of received packets in milliseconds.  # noqa: E501

        :return: The jitter of this InlineResponse20037CallerQosQos.  # noqa: E501
        :rtype: str
        """
        return self._jitter

    @jitter.setter
    def jitter(self, jitter):
        """Sets the jitter of this InlineResponse20037CallerQosQos.

        The variation in the delay of received packets in milliseconds.  # noqa: E501

        :param jitter: The jitter of this InlineResponse20037CallerQosQos.  # noqa: E501
        :type: str
        """

        self._jitter = jitter

    @property
    def max_loss(self):
        """Gets the max_loss of this InlineResponse20037CallerQosQos.  # noqa: E501

        The maximum amount of packet loss. For example, the maximum percentage of packets that fail to arrive at their destination.  # noqa: E501

        :return: The max_loss of this InlineResponse20037CallerQosQos.  # noqa: E501
        :rtype: str
        """
        return self._max_loss

    @max_loss.setter
    def max_loss(self, max_loss):
        """Sets the max_loss of this InlineResponse20037CallerQosQos.

        The maximum amount of packet loss. For example, the maximum percentage of packets that fail to arrive at their destination.  # noqa: E501

        :param max_loss: The max_loss of this InlineResponse20037CallerQosQos.  # noqa: E501
        :type: str
        """

        self._max_loss = max_loss

    @property
    def mos(self):
        """Gets the mos of this InlineResponse20037CallerQosQos.  # noqa: E501

        The MOS (Mean Opinion Score).  MOS measures voice quality on a scale of 1 to 5. A score than or equal to 3.5 means good quality, while below 3.5 means poor quality.  # noqa: E501

        :return: The mos of this InlineResponse20037CallerQosQos.  # noqa: E501
        :rtype: str
        """
        return self._mos

    @mos.setter
    def mos(self, mos):
        """Sets the mos of this InlineResponse20037CallerQosQos.

        The MOS (Mean Opinion Score).  MOS measures voice quality on a scale of 1 to 5. A score than or equal to 3.5 means good quality, while below 3.5 means poor quality.  # noqa: E501

        :param mos: The mos of this InlineResponse20037CallerQosQos.  # noqa: E501
        :type: str
        """

        self._mos = mos

    @property
    def network_delay(self):
        """Gets the network_delay of this InlineResponse20037CallerQosQos.  # noqa: E501

        The amount of time, in milliseconds, it takes for a VoIP (Voice Over IP) packet to travel from one point to another.  # noqa: E501

        :return: The network_delay of this InlineResponse20037CallerQosQos.  # noqa: E501
        :rtype: str
        """
        return self._network_delay

    @network_delay.setter
    def network_delay(self, network_delay):
        """Sets the network_delay of this InlineResponse20037CallerQosQos.

        The amount of time, in milliseconds, it takes for a VoIP (Voice Over IP) packet to travel from one point to another.  # noqa: E501

        :param network_delay: The network_delay of this InlineResponse20037CallerQosQos.  # noqa: E501
        :type: str
        """

        self._network_delay = network_delay

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
        if issubclass(InlineResponse20037CallerQosQos, dict):
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
        if not isinstance(other, InlineResponse20037CallerQosQos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
