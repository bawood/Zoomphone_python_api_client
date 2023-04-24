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

class InlineResponse20036Caller(object):
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
        'codec': 'str',
        'device_private_ip': 'str',
        'device_public_ip': 'str',
        'device_type': 'str',
        'extension_number': 'str',
        'headset': 'str',
        'isp': 'str',
        'microphone': 'str',
        'phone_number': 'str',
        'site_id': 'str'
    }

    attribute_map = {
        'codec': 'codec',
        'device_private_ip': 'device_private_ip',
        'device_public_ip': 'device_public_ip',
        'device_type': 'device_type',
        'extension_number': 'extension_number',
        'headset': 'headset',
        'isp': 'isp',
        'microphone': 'microphone',
        'phone_number': 'phone_number',
        'site_id': 'site_id'
    }

    def __init__(self, codec=None, device_private_ip=None, device_public_ip=None, device_type=None, extension_number=None, headset=None, isp=None, microphone=None, phone_number=None, site_id=None):  # noqa: E501
        """InlineResponse20036Caller - a model defined in Swagger"""  # noqa: E501
        self._codec = None
        self._device_private_ip = None
        self._device_public_ip = None
        self._device_type = None
        self._extension_number = None
        self._headset = None
        self._isp = None
        self._microphone = None
        self._phone_number = None
        self._site_id = None
        self.discriminator = None
        if codec is not None:
            self.codec = codec
        if device_private_ip is not None:
            self.device_private_ip = device_private_ip
        if device_public_ip is not None:
            self.device_public_ip = device_public_ip
        if device_type is not None:
            self.device_type = device_type
        if extension_number is not None:
            self.extension_number = extension_number
        if headset is not None:
            self.headset = headset
        if isp is not None:
            self.isp = isp
        if microphone is not None:
            self.microphone = microphone
        if phone_number is not None:
            self.phone_number = phone_number
        if site_id is not None:
            self.site_id = site_id

    @property
    def codec(self):
        """Gets the codec of this InlineResponse20036Caller.  # noqa: E501

        Audio codec.  # noqa: E501

        :return: The codec of this InlineResponse20036Caller.  # noqa: E501
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this InlineResponse20036Caller.

        Audio codec.  # noqa: E501

        :param codec: The codec of this InlineResponse20036Caller.  # noqa: E501
        :type: str
        """

        self._codec = codec

    @property
    def device_private_ip(self):
        """Gets the device_private_ip of this InlineResponse20036Caller.  # noqa: E501

        This setting displays the device's private IP address if the account has the `show_device_ip_for_call_log` parameter set to `enabled`.  # noqa: E501

        :return: The device_private_ip of this InlineResponse20036Caller.  # noqa: E501
        :rtype: str
        """
        return self._device_private_ip

    @device_private_ip.setter
    def device_private_ip(self, device_private_ip):
        """Sets the device_private_ip of this InlineResponse20036Caller.

        This setting displays the device's private IP address if the account has the `show_device_ip_for_call_log` parameter set to `enabled`.  # noqa: E501

        :param device_private_ip: The device_private_ip of this InlineResponse20036Caller.  # noqa: E501
        :type: str
        """

        self._device_private_ip = device_private_ip

    @property
    def device_public_ip(self):
        """Gets the device_public_ip of this InlineResponse20036Caller.  # noqa: E501

        This setting display sthe device's public IP address if the account has the `show_device_ip_for_call_log` parameter set to `enabled`.  # noqa: E501

        :return: The device_public_ip of this InlineResponse20036Caller.  # noqa: E501
        :rtype: str
        """
        return self._device_public_ip

    @device_public_ip.setter
    def device_public_ip(self, device_public_ip):
        """Sets the device_public_ip of this InlineResponse20036Caller.

        This setting display sthe device's public IP address if the account has the `show_device_ip_for_call_log` parameter set to `enabled`.  # noqa: E501

        :param device_public_ip: The device_public_ip of this InlineResponse20036Caller.  # noqa: E501
        :type: str
        """

        self._device_public_ip = device_public_ip

    @property
    def device_type(self):
        """Gets the device_type of this InlineResponse20036Caller.  # noqa: E501

        The device type, and if applicable, its version number. Acceptable device types:  * `Windows_Client`  * `MAC_Client`  * `Linux_Client`   * `Android_Phone`  * `IOS_Phone`  * `Android_Pad`  * `IOS_Pad`  * [Zoom Phone Appliance](https://support.zoom.us/hc/en-us/articles/360001299063#h_cc0dac0d-44aa-4fb6-8e39-359166c38715)  * `Windows_VDI_Client`  * `MAC_VDI_Client`  * `Linux_VDI_Client`   # noqa: E501

        :return: The device_type of this InlineResponse20036Caller.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this InlineResponse20036Caller.

        The device type, and if applicable, its version number. Acceptable device types:  * `Windows_Client`  * `MAC_Client`  * `Linux_Client`   * `Android_Phone`  * `IOS_Phone`  * `Android_Pad`  * `IOS_Pad`  * [Zoom Phone Appliance](https://support.zoom.us/hc/en-us/articles/360001299063#h_cc0dac0d-44aa-4fb6-8e39-359166c38715)  * `Windows_VDI_Client`  * `MAC_VDI_Client`  * `Linux_VDI_Client`   # noqa: E501

        :param device_type: The device_type of this InlineResponse20036Caller.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def extension_number(self):
        """Gets the extension_number of this InlineResponse20036Caller.  # noqa: E501

        The full extension number of the caller.  # noqa: E501

        :return: The extension_number of this InlineResponse20036Caller.  # noqa: E501
        :rtype: str
        """
        return self._extension_number

    @extension_number.setter
    def extension_number(self, extension_number):
        """Sets the extension_number of this InlineResponse20036Caller.

        The full extension number of the caller.  # noqa: E501

        :param extension_number: The extension_number of this InlineResponse20036Caller.  # noqa: E501
        :type: str
        """

        self._extension_number = extension_number

    @property
    def headset(self):
        """Gets the headset of this InlineResponse20036Caller.  # noqa: E501

        The headset the caller uses for the call.  # noqa: E501

        :return: The headset of this InlineResponse20036Caller.  # noqa: E501
        :rtype: str
        """
        return self._headset

    @headset.setter
    def headset(self, headset):
        """Sets the headset of this InlineResponse20036Caller.

        The headset the caller uses for the call.  # noqa: E501

        :param headset: The headset of this InlineResponse20036Caller.  # noqa: E501
        :type: str
        """

        self._headset = headset

    @property
    def isp(self):
        """Gets the isp of this InlineResponse20036Caller.  # noqa: E501

        ISP.  # noqa: E501

        :return: The isp of this InlineResponse20036Caller.  # noqa: E501
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this InlineResponse20036Caller.

        ISP.  # noqa: E501

        :param isp: The isp of this InlineResponse20036Caller.  # noqa: E501
        :type: str
        """

        self._isp = isp

    @property
    def microphone(self):
        """Gets the microphone of this InlineResponse20036Caller.  # noqa: E501

        The microphone the caller uses for the call.  # noqa: E501

        :return: The microphone of this InlineResponse20036Caller.  # noqa: E501
        :rtype: str
        """
        return self._microphone

    @microphone.setter
    def microphone(self, microphone):
        """Sets the microphone of this InlineResponse20036Caller.

        The microphone the caller uses for the call.  # noqa: E501

        :param microphone: The microphone of this InlineResponse20036Caller.  # noqa: E501
        :type: str
        """

        self._microphone = microphone

    @property
    def phone_number(self):
        """Gets the phone_number of this InlineResponse20036Caller.  # noqa: E501

        The phone number of the caller in E164 format.  # noqa: E501

        :return: The phone_number of this InlineResponse20036Caller.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this InlineResponse20036Caller.

        The phone number of the caller in E164 format.  # noqa: E501

        :param phone_number: The phone_number of this InlineResponse20036Caller.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def site_id(self):
        """Gets the site_id of this InlineResponse20036Caller.  # noqa: E501

        The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites).  # noqa: E501

        :return: The site_id of this InlineResponse20036Caller.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this InlineResponse20036Caller.

        The unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites).  # noqa: E501

        :param site_id: The site_id of this InlineResponse20036Caller.  # noqa: E501
        :type: str
        """

        self._site_id = site_id

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
        if issubclass(InlineResponse20036Caller, dict):
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
        if not isinstance(other, InlineResponse20036Caller):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
