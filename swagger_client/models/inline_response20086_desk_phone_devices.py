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

class InlineResponse20086DeskPhoneDevices(object):
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
        'device_type': 'str',
        'display_name': 'str',
        'id': 'str',
        'policy': 'InlineResponse20086DeskPhonePolicy',
        'status': 'str'
    }

    attribute_map = {
        'device_type': 'device_type',
        'display_name': 'display_name',
        'id': 'id',
        'policy': 'policy',
        'status': 'status'
    }

    def __init__(self, device_type=None, display_name=None, id=None, policy=None, status=None):  # noqa: E501
        """InlineResponse20086DeskPhoneDevices - a model defined in Swagger"""  # noqa: E501
        self._device_type = None
        self._display_name = None
        self._id = None
        self._policy = None
        self._status = None
        self.discriminator = None
        if device_type is not None:
            self.device_type = device_type
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if policy is not None:
            self.policy = policy
        if status is not None:
            self.status = status

    @property
    def device_type(self):
        """Gets the device_type of this InlineResponse20086DeskPhoneDevices.  # noqa: E501

        The device type, including the manufacturer and the model name.  # noqa: E501

        :return: The device_type of this InlineResponse20086DeskPhoneDevices.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this InlineResponse20086DeskPhoneDevices.

        The device type, including the manufacturer and the model name.  # noqa: E501

        :param device_type: The device_type of this InlineResponse20086DeskPhoneDevices.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def display_name(self):
        """Gets the display_name of this InlineResponse20086DeskPhoneDevices.  # noqa: E501

        The display name of the device.  # noqa: E501

        :return: The display_name of this InlineResponse20086DeskPhoneDevices.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InlineResponse20086DeskPhoneDevices.

        The display name of the device.  # noqa: E501

        :param display_name: The display_name of this InlineResponse20086DeskPhoneDevices.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this InlineResponse20086DeskPhoneDevices.  # noqa: E501

        The device ID.  # noqa: E501

        :return: The id of this InlineResponse20086DeskPhoneDevices.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20086DeskPhoneDevices.

        The device ID.  # noqa: E501

        :param id: The id of this InlineResponse20086DeskPhoneDevices.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def policy(self):
        """Gets the policy of this InlineResponse20086DeskPhoneDevices.  # noqa: E501


        :return: The policy of this InlineResponse20086DeskPhoneDevices.  # noqa: E501
        :rtype: InlineResponse20086DeskPhonePolicy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this InlineResponse20086DeskPhoneDevices.


        :param policy: The policy of this InlineResponse20086DeskPhoneDevices.  # noqa: E501
        :type: InlineResponse20086DeskPhonePolicy
        """

        self._policy = policy

    @property
    def status(self):
        """Gets the status of this InlineResponse20086DeskPhoneDevices.  # noqa: E501

        The status of the device: `online` or `offline`.  # noqa: E501

        :return: The status of this InlineResponse20086DeskPhoneDevices.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20086DeskPhoneDevices.

        The status of the device: `online` or `offline`.  # noqa: E501

        :param status: The status of this InlineResponse20086DeskPhoneDevices.  # noqa: E501
        :type: str
        """
        allowed_values = ["online", "offline"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(InlineResponse20086DeskPhoneDevices, dict):
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
        if not isinstance(other, InlineResponse20086DeskPhoneDevices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
