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

class PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers(object):
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
        'call_forwarding_type': 'int',
        'reset': 'bool'
    }

    attribute_map = {
        'enable': 'enable',
        'call_forwarding_type': 'call_forwarding_type',
        'reset': 'reset'
    }

    def __init__(self, enable=None, call_forwarding_type=None, reset=None):  # noqa: E501
        """PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._call_forwarding_type = None
        self._reset = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if call_forwarding_type is not None:
            self.call_forwarding_type = call_forwarding_type
        if reset is not None:
            self.reset = reset

    @property
    def enable(self):
        """Gets the enable of this PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers.  # noqa: E501


        :return: The enable of this PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers.


        :param enable: The enable of this PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def call_forwarding_type(self):
        """Gets the call_forwarding_type of this PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers.  # noqa: E501

        `1` - Low restriction (external numbers not allowed) `2` - Medium restriction (external numbers and external contacts not allowed)  `3` - High restriction (external numbers, external contacts and internal extensions without inbound automatic call recording not allowed) `4` - No restriction  # noqa: E501

        :return: The call_forwarding_type of this PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers.  # noqa: E501
        :rtype: int
        """
        return self._call_forwarding_type

    @call_forwarding_type.setter
    def call_forwarding_type(self, call_forwarding_type):
        """Sets the call_forwarding_type of this PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers.

        `1` - Low restriction (external numbers not allowed) `2` - Medium restriction (external numbers and external contacts not allowed)  `3` - High restriction (external numbers, external contacts and internal extensions without inbound automatic call recording not allowed) `4` - No restriction  # noqa: E501

        :param call_forwarding_type: The call_forwarding_type of this PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3, 4]  # noqa: E501
        if call_forwarding_type not in allowed_values:
            raise ValueError(
                "Invalid value for `call_forwarding_type` ({0}), must be one of {1}"  # noqa: E501
                .format(call_forwarding_type, allowed_values)
            )

        self._call_forwarding_type = call_forwarding_type

    @property
    def reset(self):
        """Gets the reset of this PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers.  # noqa: E501

        Whether the current settings will use the phone site's settings (applicable if the current settings are using the new policy framework).  # noqa: E501

        :return: The reset of this PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers.  # noqa: E501
        :rtype: bool
        """
        return self._reset

    @reset.setter
    def reset(self, reset):
        """Sets the reset of this PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers.

        Whether the current settings will use the phone site's settings (applicable if the current settings are using the new policy framework).  # noqa: E501

        :param reset: The reset of this PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers.  # noqa: E501
        :type: bool
        """

        self._reset = reset

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
        if issubclass(PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers, dict):
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
        if not isinstance(other, PhoneusersuserIdPolicyCallHandlingForwardingToOtherUsers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
