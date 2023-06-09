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

class InlineResponse20086IntercomAudioIntercoms(object):
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
        'extension_id': 'str',
        'extension_number': 'str',
        'extension_type': 'str',
        'display_name': 'str',
        'status': 'str',
        'device_id': 'str',
        'device_status': 'str'
    }

    attribute_map = {
        'extension_id': 'extension_id',
        'extension_number': 'extension_number',
        'extension_type': 'extension_type',
        'display_name': 'display_name',
        'status': 'status',
        'device_id': 'device_id',
        'device_status': 'device_status'
    }

    def __init__(self, extension_id=None, extension_number=None, extension_type=None, display_name=None, status=None, device_id=None, device_status=None):  # noqa: E501
        """InlineResponse20086IntercomAudioIntercoms - a model defined in Swagger"""  # noqa: E501
        self._extension_id = None
        self._extension_number = None
        self._extension_type = None
        self._display_name = None
        self._status = None
        self._device_id = None
        self._device_status = None
        self.discriminator = None
        if extension_id is not None:
            self.extension_id = extension_id
        if extension_number is not None:
            self.extension_number = extension_number
        if extension_type is not None:
            self.extension_type = extension_type
        if display_name is not None:
            self.display_name = display_name
        if status is not None:
            self.status = status
        if device_id is not None:
            self.device_id = device_id
        if device_status is not None:
            self.device_status = device_status

    @property
    def extension_id(self):
        """Gets the extension_id of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501

        The extension ID.  # noqa: E501

        :return: The extension_id of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501
        :rtype: str
        """
        return self._extension_id

    @extension_id.setter
    def extension_id(self, extension_id):
        """Sets the extension_id of this InlineResponse20086IntercomAudioIntercoms.

        The extension ID.  # noqa: E501

        :param extension_id: The extension_id of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501
        :type: str
        """

        self._extension_id = extension_id

    @property
    def extension_number(self):
        """Gets the extension_number of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501

        The extension number.  # noqa: E501

        :return: The extension_number of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501
        :rtype: str
        """
        return self._extension_number

    @extension_number.setter
    def extension_number(self, extension_number):
        """Sets the extension_number of this InlineResponse20086IntercomAudioIntercoms.

        The extension number.  # noqa: E501

        :param extension_number: The extension_number of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501
        :type: str
        """

        self._extension_number = extension_number

    @property
    def extension_type(self):
        """Gets the extension_type of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501

        The extension type: `user` or `commonArea`.  # noqa: E501

        :return: The extension_type of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501
        :rtype: str
        """
        return self._extension_type

    @extension_type.setter
    def extension_type(self, extension_type):
        """Sets the extension_type of this InlineResponse20086IntercomAudioIntercoms.

        The extension type: `user` or `commonArea`.  # noqa: E501

        :param extension_type: The extension_type of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501
        :type: str
        """

        self._extension_type = extension_type

    @property
    def display_name(self):
        """Gets the display_name of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501

        The display name.  # noqa: E501

        :return: The display_name of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InlineResponse20086IntercomAudioIntercoms.

        The display name.  # noqa: E501

        :param display_name: The display_name of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def status(self):
        """Gets the status of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501

        The status of the extension: `active` or `pending`.  # noqa: E501

        :return: The status of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20086IntercomAudioIntercoms.

        The status of the extension: `active` or `pending`.  # noqa: E501

        :param status: The status of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "pending"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def device_id(self):
        """Gets the device_id of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501

        The device ID. Applicable when the extension level is `commonArea`.  # noqa: E501

        :return: The device_id of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this InlineResponse20086IntercomAudioIntercoms.

        The device ID. Applicable when the extension level is `commonArea`.  # noqa: E501

        :param device_id: The device_id of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def device_status(self):
        """Gets the device_status of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501

        The status of the device. Applicable when the extension level is `commonArea`.  # noqa: E501

        :return: The device_status of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501
        :rtype: str
        """
        return self._device_status

    @device_status.setter
    def device_status(self, device_status):
        """Sets the device_status of this InlineResponse20086IntercomAudioIntercoms.

        The status of the device. Applicable when the extension level is `commonArea`.  # noqa: E501

        :param device_status: The device_status of this InlineResponse20086IntercomAudioIntercoms.  # noqa: E501
        :type: str
        """
        allowed_values = ["online", "offline", "no device"]  # noqa: E501
        if device_status not in allowed_values:
            raise ValueError(
                "Invalid value for `device_status` ({0}), must be one of {1}"  # noqa: E501
                .format(device_status, allowed_values)
            )

        self._device_status = device_status

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
        if issubclass(InlineResponse20086IntercomAudioIntercoms, dict):
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
        if not isinstance(other, InlineResponse20086IntercomAudioIntercoms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
