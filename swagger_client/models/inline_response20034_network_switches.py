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

class InlineResponse20034NetworkSwitches(object):
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
        'mac_address': 'str',
        'port': 'str',
        'port_prefix': 'str',
        'port_range_from': 'str',
        'port_range_to': 'str'
    }

    attribute_map = {
        'mac_address': 'mac_address',
        'port': 'port',
        'port_prefix': 'port_prefix',
        'port_range_from': 'port_range_from',
        'port_range_to': 'port_range_to'
    }

    def __init__(self, mac_address=None, port=None, port_prefix=None, port_range_from=None, port_range_to=None):  # noqa: E501
        """InlineResponse20034NetworkSwitches - a model defined in Swagger"""  # noqa: E501
        self._mac_address = None
        self._port = None
        self._port_prefix = None
        self._port_range_from = None
        self._port_range_to = None
        self.discriminator = None
        if mac_address is not None:
            self.mac_address = mac_address
        if port is not None:
            self.port = port
        if port_prefix is not None:
            self.port_prefix = port_prefix
        if port_range_from is not None:
            self.port_range_from = port_range_from
        if port_range_to is not None:
            self.port_range_to = port_range_to

    @property
    def mac_address(self):
        """Gets the mac_address of this InlineResponse20034NetworkSwitches.  # noqa: E501

        The MAC address.  # noqa: E501

        :return: The mac_address of this InlineResponse20034NetworkSwitches.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this InlineResponse20034NetworkSwitches.

        The MAC address.  # noqa: E501

        :param mac_address: The mac_address of this InlineResponse20034NetworkSwitches.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def port(self):
        """Gets the port of this InlineResponse20034NetworkSwitches.  # noqa: E501

        The port's label.  # noqa: E501

        :return: The port of this InlineResponse20034NetworkSwitches.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this InlineResponse20034NetworkSwitches.

        The port's label.  # noqa: E501

        :param port: The port of this InlineResponse20034NetworkSwitches.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def port_prefix(self):
        """Gets the port_prefix of this InlineResponse20034NetworkSwitches.  # noqa: E501

        The port's prefix.  # noqa: E501

        :return: The port_prefix of this InlineResponse20034NetworkSwitches.  # noqa: E501
        :rtype: str
        """
        return self._port_prefix

    @port_prefix.setter
    def port_prefix(self, port_prefix):
        """Sets the port_prefix of this InlineResponse20034NetworkSwitches.

        The port's prefix.  # noqa: E501

        :param port_prefix: The port_prefix of this InlineResponse20034NetworkSwitches.  # noqa: E501
        :type: str
        """

        self._port_prefix = port_prefix

    @property
    def port_range_from(self):
        """Gets the port_range_from of this InlineResponse20034NetworkSwitches.  # noqa: E501

        The port's range from value.  # noqa: E501

        :return: The port_range_from of this InlineResponse20034NetworkSwitches.  # noqa: E501
        :rtype: str
        """
        return self._port_range_from

    @port_range_from.setter
    def port_range_from(self, port_range_from):
        """Sets the port_range_from of this InlineResponse20034NetworkSwitches.

        The port's range from value.  # noqa: E501

        :param port_range_from: The port_range_from of this InlineResponse20034NetworkSwitches.  # noqa: E501
        :type: str
        """

        self._port_range_from = port_range_from

    @property
    def port_range_to(self):
        """Gets the port_range_to of this InlineResponse20034NetworkSwitches.  # noqa: E501

        The port's range to value.  # noqa: E501

        :return: The port_range_to of this InlineResponse20034NetworkSwitches.  # noqa: E501
        :rtype: str
        """
        return self._port_range_to

    @port_range_to.setter
    def port_range_to(self, port_range_to):
        """Sets the port_range_to of this InlineResponse20034NetworkSwitches.

        The port's range to value.  # noqa: E501

        :param port_range_to: The port_range_to of this InlineResponse20034NetworkSwitches.  # noqa: E501
        :type: str
        """

        self._port_range_to = port_range_to

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
        if issubclass(InlineResponse20034NetworkSwitches, dict):
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
        if not isinstance(other, InlineResponse20034NetworkSwitches):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
