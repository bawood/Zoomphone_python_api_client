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

class InlineResponse20044CallPark(object):
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
        'expiration_period': 'int',
        'call_not_picked_up_action': 'int',
        'forward_to': 'InlineResponse20044CallParkForwardTo',
        'sequence': 'int'
    }

    attribute_map = {
        'enable': 'enable',
        'locked': 'locked',
        'locked_by': 'locked_by',
        'expiration_period': 'expiration_period',
        'call_not_picked_up_action': 'call_not_picked_up_action',
        'forward_to': 'forward_to',
        'sequence': 'sequence'
    }

    def __init__(self, enable=None, locked=None, locked_by=None, expiration_period=None, call_not_picked_up_action=None, forward_to=None, sequence=None):  # noqa: E501
        """InlineResponse20044CallPark - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._locked = None
        self._locked_by = None
        self._expiration_period = None
        self._call_not_picked_up_action = None
        self._forward_to = None
        self._sequence = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if locked is not None:
            self.locked = locked
        if locked_by is not None:
            self.locked_by = locked_by
        if expiration_period is not None:
            self.expiration_period = expiration_period
        if call_not_picked_up_action is not None:
            self.call_not_picked_up_action = call_not_picked_up_action
        if forward_to is not None:
            self.forward_to = forward_to
        if sequence is not None:
            self.sequence = sequence

    @property
    def enable(self):
        """Gets the enable of this InlineResponse20044CallPark.  # noqa: E501


        :return: The enable of this InlineResponse20044CallPark.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this InlineResponse20044CallPark.


        :param enable: The enable of this InlineResponse20044CallPark.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def locked(self):
        """Gets the locked of this InlineResponse20044CallPark.  # noqa: E501

        Whether the senior administrator allows users to modify the current settings.  # noqa: E501

        :return: The locked of this InlineResponse20044CallPark.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this InlineResponse20044CallPark.

        Whether the senior administrator allows users to modify the current settings.  # noqa: E501

        :param locked: The locked of this InlineResponse20044CallPark.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def locked_by(self):
        """Gets the locked_by of this InlineResponse20044CallPark.  # noqa: E501

        Which level of administrator prohibits the modification of the current settings.  # noqa: E501

        :return: The locked_by of this InlineResponse20044CallPark.  # noqa: E501
        :rtype: str
        """
        return self._locked_by

    @locked_by.setter
    def locked_by(self, locked_by):
        """Sets the locked_by of this InlineResponse20044CallPark.

        Which level of administrator prohibits the modification of the current settings.  # noqa: E501

        :param locked_by: The locked_by of this InlineResponse20044CallPark.  # noqa: E501
        :type: str
        """
        allowed_values = ["invalid", "account"]  # noqa: E501
        if locked_by not in allowed_values:
            raise ValueError(
                "Invalid value for `locked_by` ({0}), must be one of {1}"  # noqa: E501
                .format(locked_by, allowed_values)
            )

        self._locked_by = locked_by

    @property
    def expiration_period(self):
        """Gets the expiration_period of this InlineResponse20044CallPark.  # noqa: E501

        A time limit for parked calls in minutes. After the expiration period ends, the retrieval code is no longer valid and a new code will be generated.  # noqa: E501

        :return: The expiration_period of this InlineResponse20044CallPark.  # noqa: E501
        :rtype: int
        """
        return self._expiration_period

    @expiration_period.setter
    def expiration_period(self, expiration_period):
        """Sets the expiration_period of this InlineResponse20044CallPark.

        A time limit for parked calls in minutes. After the expiration period ends, the retrieval code is no longer valid and a new code will be generated.  # noqa: E501

        :param expiration_period: The expiration_period of this InlineResponse20044CallPark.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]  # noqa: E501
        if expiration_period not in allowed_values:
            raise ValueError(
                "Invalid value for `expiration_period` ({0}), must be one of {1}"  # noqa: E501
                .format(expiration_period, allowed_values)
            )

        self._expiration_period = expiration_period

    @property
    def call_not_picked_up_action(self):
        """Gets the call_not_picked_up_action of this InlineResponse20044CallPark.  # noqa: E501

        The action when a parked call is not picked up.   `100` - Ring back to parker  `0` - Forward to voicemail of the parker  `9` - Disconnect   `50` - Forward to another extension  # noqa: E501

        :return: The call_not_picked_up_action of this InlineResponse20044CallPark.  # noqa: E501
        :rtype: int
        """
        return self._call_not_picked_up_action

    @call_not_picked_up_action.setter
    def call_not_picked_up_action(self, call_not_picked_up_action):
        """Sets the call_not_picked_up_action of this InlineResponse20044CallPark.

        The action when a parked call is not picked up.   `100` - Ring back to parker  `0` - Forward to voicemail of the parker  `9` - Disconnect   `50` - Forward to another extension  # noqa: E501

        :param call_not_picked_up_action: The call_not_picked_up_action of this InlineResponse20044CallPark.  # noqa: E501
        :type: int
        """

        self._call_not_picked_up_action = call_not_picked_up_action

    @property
    def forward_to(self):
        """Gets the forward_to of this InlineResponse20044CallPark.  # noqa: E501


        :return: The forward_to of this InlineResponse20044CallPark.  # noqa: E501
        :rtype: InlineResponse20044CallParkForwardTo
        """
        return self._forward_to

    @forward_to.setter
    def forward_to(self, forward_to):
        """Sets the forward_to of this InlineResponse20044CallPark.


        :param forward_to: The forward_to of this InlineResponse20044CallPark.  # noqa: E501
        :type: InlineResponse20044CallParkForwardTo
        """

        self._forward_to = forward_to

    @property
    def sequence(self):
        """Gets the sequence of this InlineResponse20044CallPark.  # noqa: E501

        This field is only used in the new policy framework. Choose how parked calls are assigned to a BLF (Busy Lamp Field) key. Sequential assignment will park the call at the next available BLF key. Random assignment will park the call at a randomly selected BLF key.  `0` - Random  `1` - Sequential  # noqa: E501

        :return: The sequence of this InlineResponse20044CallPark.  # noqa: E501
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this InlineResponse20044CallPark.

        This field is only used in the new policy framework. Choose how parked calls are assigned to a BLF (Busy Lamp Field) key. Sequential assignment will park the call at the next available BLF key. Random assignment will park the call at a randomly selected BLF key.  `0` - Random  `1` - Sequential  # noqa: E501

        :param sequence: The sequence of this InlineResponse20044CallPark.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if sequence not in allowed_values:
            raise ValueError(
                "Invalid value for `sequence` ({0}), must be one of {1}"  # noqa: E501
                .format(sequence, allowed_values)
            )

        self._sequence = sequence

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
        if issubclass(InlineResponse20044CallPark, dict):
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
        if not isinstance(other, InlineResponse20044CallPark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
