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

class InlineResponse20037CalleeQos(object):
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
        'device_private_ip': 'str',
        'device_public_ip': 'str',
        'receiving': 'list[InlineResponse20037CalleeQosReceiving]',
        'sending': 'list[InlineResponse20037CalleeQosSending]'
    }

    attribute_map = {
        'device_private_ip': 'device_private_ip',
        'device_public_ip': 'device_public_ip',
        'receiving': 'receiving',
        'sending': 'sending'
    }

    def __init__(self, device_private_ip=None, device_public_ip=None, receiving=None, sending=None):  # noqa: E501
        """InlineResponse20037CalleeQos - a model defined in Swagger"""  # noqa: E501
        self._device_private_ip = None
        self._device_public_ip = None
        self._receiving = None
        self._sending = None
        self.discriminator = None
        if device_private_ip is not None:
            self.device_private_ip = device_private_ip
        if device_public_ip is not None:
            self.device_public_ip = device_public_ip
        if receiving is not None:
            self.receiving = receiving
        if sending is not None:
            self.sending = sending

    @property
    def device_private_ip(self):
        """Gets the device_private_ip of this InlineResponse20037CalleeQos.  # noqa: E501

        This setting displays the device's private IP address if the account has the `show_device_ip_for_call_log` parameter set to `enabled`.  # noqa: E501

        :return: The device_private_ip of this InlineResponse20037CalleeQos.  # noqa: E501
        :rtype: str
        """
        return self._device_private_ip

    @device_private_ip.setter
    def device_private_ip(self, device_private_ip):
        """Sets the device_private_ip of this InlineResponse20037CalleeQos.

        This setting displays the device's private IP address if the account has the `show_device_ip_for_call_log` parameter set to `enabled`.  # noqa: E501

        :param device_private_ip: The device_private_ip of this InlineResponse20037CalleeQos.  # noqa: E501
        :type: str
        """

        self._device_private_ip = device_private_ip

    @property
    def device_public_ip(self):
        """Gets the device_public_ip of this InlineResponse20037CalleeQos.  # noqa: E501

        This setting displays the device's public IP address if the account has the `show_device_ip_for_call_log` parameter set to `enabled`.  # noqa: E501

        :return: The device_public_ip of this InlineResponse20037CalleeQos.  # noqa: E501
        :rtype: str
        """
        return self._device_public_ip

    @device_public_ip.setter
    def device_public_ip(self, device_public_ip):
        """Sets the device_public_ip of this InlineResponse20037CalleeQos.

        This setting displays the device's public IP address if the account has the `show_device_ip_for_call_log` parameter set to `enabled`.  # noqa: E501

        :param device_public_ip: The device_public_ip of this InlineResponse20037CalleeQos.  # noqa: E501
        :type: str
        """

        self._device_public_ip = device_public_ip

    @property
    def receiving(self):
        """Gets the receiving of this InlineResponse20037CalleeQos.  # noqa: E501

        The QoS that the callee receives.  # noqa: E501

        :return: The receiving of this InlineResponse20037CalleeQos.  # noqa: E501
        :rtype: list[InlineResponse20037CalleeQosReceiving]
        """
        return self._receiving

    @receiving.setter
    def receiving(self, receiving):
        """Sets the receiving of this InlineResponse20037CalleeQos.

        The QoS that the callee receives.  # noqa: E501

        :param receiving: The receiving of this InlineResponse20037CalleeQos.  # noqa: E501
        :type: list[InlineResponse20037CalleeQosReceiving]
        """

        self._receiving = receiving

    @property
    def sending(self):
        """Gets the sending of this InlineResponse20037CalleeQos.  # noqa: E501

        The QoS that the callee sends.  # noqa: E501

        :return: The sending of this InlineResponse20037CalleeQos.  # noqa: E501
        :rtype: list[InlineResponse20037CalleeQosSending]
        """
        return self._sending

    @sending.setter
    def sending(self, sending):
        """Sets the sending of this InlineResponse20037CalleeQos.

        The QoS that the callee sends.  # noqa: E501

        :param sending: The sending of this InlineResponse20037CalleeQos.  # noqa: E501
        :type: list[InlineResponse20037CalleeQosSending]
        """

        self._sending = sending

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
        if issubclass(InlineResponse20037CalleeQos, dict):
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
        if not isinstance(other, InlineResponse20037CalleeQos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
