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

class PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution(object):
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
        'handle_multiple_calls': 'bool',
        'ring_duration': 'int',
        'ring_mode': 'str',
        'skip_offline_device_phone_number': 'bool'
    }

    attribute_map = {
        'handle_multiple_calls': 'handle_multiple_calls',
        'ring_duration': 'ring_duration',
        'ring_mode': 'ring_mode',
        'skip_offline_device_phone_number': 'skip_offline_device_phone_number'
    }

    def __init__(self, handle_multiple_calls=None, ring_duration=None, ring_mode=None, skip_offline_device_phone_number=None):  # noqa: E501
        """PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution - a model defined in Swagger"""  # noqa: E501
        self._handle_multiple_calls = None
        self._ring_duration = None
        self._ring_mode = None
        self._skip_offline_device_phone_number = None
        self.discriminator = None
        if handle_multiple_calls is not None:
            self.handle_multiple_calls = handle_multiple_calls
        if ring_duration is not None:
            self.ring_duration = ring_duration
        if ring_mode is not None:
            self.ring_mode = ring_mode
        if skip_offline_device_phone_number is not None:
            self.skip_offline_device_phone_number = skip_offline_device_phone_number

    @property
    def handle_multiple_calls(self):
        """Gets the handle_multiple_calls of this PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution.  # noqa: E501

        The maximum number of calls that can be handled simultaneously is less than half of the total amount of available call queue members. Note that the first incoming call may not be answered first.  Required except for `simultaneous` ring mode.  # noqa: E501

        :return: The handle_multiple_calls of this PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution.  # noqa: E501
        :rtype: bool
        """
        return self._handle_multiple_calls

    @handle_multiple_calls.setter
    def handle_multiple_calls(self, handle_multiple_calls):
        """Sets the handle_multiple_calls of this PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution.

        The maximum number of calls that can be handled simultaneously is less than half of the total amount of available call queue members. Note that the first incoming call may not be answered first.  Required except for `simultaneous` ring mode.  # noqa: E501

        :param handle_multiple_calls: The handle_multiple_calls of this PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution.  # noqa: E501
        :type: bool
        """

        self._handle_multiple_calls = handle_multiple_calls

    @property
    def ring_duration(self):
        """Gets the ring_duration of this PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution.  # noqa: E501

        Ringing duration for each member: * `10`  * `15`  * `20`  * `25`  * `30`  * `35`  * `40`  * `45`  * `50`  * `55`  * `60`   Required except for `simultaneous` ring mode.  # noqa: E501

        :return: The ring_duration of this PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution.  # noqa: E501
        :rtype: int
        """
        return self._ring_duration

    @ring_duration.setter
    def ring_duration(self, ring_duration):
        """Sets the ring_duration of this PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution.

        Ringing duration for each member: * `10`  * `15`  * `20`  * `25`  * `30`  * `35`  * `40`  * `45`  * `50`  * `55`  * `60`   Required except for `simultaneous` ring mode.  # noqa: E501

        :param ring_duration: The ring_duration of this PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution.  # noqa: E501
        :type: int
        """
        allowed_values = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]  # noqa: E501
        if ring_duration not in allowed_values:
            raise ValueError(
                "Invalid value for `ring_duration` ({0}), must be one of {1}"  # noqa: E501
                .format(ring_duration, allowed_values)
            )

        self._ring_duration = ring_duration

    @property
    def ring_mode(self):
        """Gets the ring_mode of this PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution.  # noqa: E501

        The call distribution ring mode:  * `simultaneous`  * `sequential`  * `rotating`  * `longest_idle`.  # noqa: E501

        :return: The ring_mode of this PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution.  # noqa: E501
        :rtype: str
        """
        return self._ring_mode

    @ring_mode.setter
    def ring_mode(self, ring_mode):
        """Sets the ring_mode of this PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution.

        The call distribution ring mode:  * `simultaneous`  * `sequential`  * `rotating`  * `longest_idle`.  # noqa: E501

        :param ring_mode: The ring_mode of this PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution.  # noqa: E501
        :type: str
        """
        allowed_values = ["simultaneous", "sequential", "rotating", "longest_idle"]  # noqa: E501
        if ring_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `ring_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(ring_mode, allowed_values)
            )

        self._ring_mode = ring_mode

    @property
    def skip_offline_device_phone_number(self):
        """Gets the skip_offline_device_phone_number of this PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution.  # noqa: E501

        1. Devices with Zoom app or client not launched and mobile phone with screen locked will be skipped.   2. Phone numbers added to user's call handling settings will be skipped.  Required except for `simultaneous` ring mode.  # noqa: E501

        :return: The skip_offline_device_phone_number of this PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution.  # noqa: E501
        :rtype: bool
        """
        return self._skip_offline_device_phone_number

    @skip_offline_device_phone_number.setter
    def skip_offline_device_phone_number(self, skip_offline_device_phone_number):
        """Sets the skip_offline_device_phone_number of this PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution.

        1. Devices with Zoom app or client not launched and mobile phone with screen locked will be skipped.   2. Phone numbers added to user's call handling settings will be skipped.  Required except for `simultaneous` ring mode.  # noqa: E501

        :param skip_offline_device_phone_number: The skip_offline_device_phone_number of this PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution.  # noqa: E501
        :type: bool
        """

        self._skip_offline_device_phone_number = skip_offline_device_phone_number

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
        if issubclass(PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution, dict):
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
        if not isinstance(other, PhoneextensionextensionIdcallHandlingsettingssettingTypeSettings1CallDistribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
