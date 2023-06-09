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

class InlineResponse20031KeyAssignment(object):
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
        'display_name': 'str',
        'extension_id': 'str',
        'extension_number': 'str',
        'phone_number': 'str',
        'retrieval_code': 'str',
        'speed_dial_number': 'str'
    }

    attribute_map = {
        'display_name': 'display_name',
        'extension_id': 'extension_id',
        'extension_number': 'extension_number',
        'phone_number': 'phone_number',
        'retrieval_code': 'retrieval_code',
        'speed_dial_number': 'speed_dial_number'
    }

    def __init__(self, display_name=None, extension_id=None, extension_number=None, phone_number=None, retrieval_code=None, speed_dial_number=None):  # noqa: E501
        """InlineResponse20031KeyAssignment - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._extension_id = None
        self._extension_number = None
        self._phone_number = None
        self._retrieval_code = None
        self._speed_dial_number = None
        self.discriminator = None
        if display_name is not None:
            self.display_name = display_name
        if extension_id is not None:
            self.extension_id = extension_id
        if extension_number is not None:
            self.extension_number = extension_number
        if phone_number is not None:
            self.phone_number = phone_number
        if retrieval_code is not None:
            self.retrieval_code = retrieval_code
        if speed_dial_number is not None:
            self.speed_dial_number = speed_dial_number

    @property
    def display_name(self):
        """Gets the display_name of this InlineResponse20031KeyAssignment.  # noqa: E501

        The display name of the line assigned to the line key.  # noqa: E501

        :return: The display_name of this InlineResponse20031KeyAssignment.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InlineResponse20031KeyAssignment.

        The display name of the line assigned to the line key.  # noqa: E501

        :param display_name: The display_name of this InlineResponse20031KeyAssignment.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def extension_id(self):
        """Gets the extension_id of this InlineResponse20031KeyAssignment.  # noqa: E501

        The extension ID of the line assigned to the line key.  # noqa: E501

        :return: The extension_id of this InlineResponse20031KeyAssignment.  # noqa: E501
        :rtype: str
        """
        return self._extension_id

    @extension_id.setter
    def extension_id(self, extension_id):
        """Sets the extension_id of this InlineResponse20031KeyAssignment.

        The extension ID of the line assigned to the line key.  # noqa: E501

        :param extension_id: The extension_id of this InlineResponse20031KeyAssignment.  # noqa: E501
        :type: str
        """

        self._extension_id = extension_id

    @property
    def extension_number(self):
        """Gets the extension_number of this InlineResponse20031KeyAssignment.  # noqa: E501

        The extension number of the line assigned to the line key.  # noqa: E501

        :return: The extension_number of this InlineResponse20031KeyAssignment.  # noqa: E501
        :rtype: str
        """
        return self._extension_number

    @extension_number.setter
    def extension_number(self, extension_number):
        """Sets the extension_number of this InlineResponse20031KeyAssignment.

        The extension number of the line assigned to the line key.  # noqa: E501

        :param extension_number: The extension_number of this InlineResponse20031KeyAssignment.  # noqa: E501
        :type: str
        """

        self._extension_number = extension_number

    @property
    def phone_number(self):
        """Gets the phone_number of this InlineResponse20031KeyAssignment.  # noqa: E501

        The phone number of the line assigned to the line key.  # noqa: E501

        :return: The phone_number of this InlineResponse20031KeyAssignment.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this InlineResponse20031KeyAssignment.

        The phone number of the line assigned to the line key.  # noqa: E501

        :param phone_number: The phone_number of this InlineResponse20031KeyAssignment.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def retrieval_code(self):
        """Gets the retrieval_code of this InlineResponse20031KeyAssignment.  # noqa: E501

        The call park retrieval code for `call_park` line key type.  # noqa: E501

        :return: The retrieval_code of this InlineResponse20031KeyAssignment.  # noqa: E501
        :rtype: str
        """
        return self._retrieval_code

    @retrieval_code.setter
    def retrieval_code(self, retrieval_code):
        """Sets the retrieval_code of this InlineResponse20031KeyAssignment.

        The call park retrieval code for `call_park` line key type.  # noqa: E501

        :param retrieval_code: The retrieval_code of this InlineResponse20031KeyAssignment.  # noqa: E501
        :type: str
        """

        self._retrieval_code = retrieval_code

    @property
    def speed_dial_number(self):
        """Gets the speed_dial_number of this InlineResponse20031KeyAssignment.  # noqa: E501

        The speed dial number used for `speed_dial_number` line key type.  # noqa: E501

        :return: The speed_dial_number of this InlineResponse20031KeyAssignment.  # noqa: E501
        :rtype: str
        """
        return self._speed_dial_number

    @speed_dial_number.setter
    def speed_dial_number(self, speed_dial_number):
        """Sets the speed_dial_number of this InlineResponse20031KeyAssignment.

        The speed dial number used for `speed_dial_number` line key type.  # noqa: E501

        :param speed_dial_number: The speed_dial_number of this InlineResponse20031KeyAssignment.  # noqa: E501
        :type: str
        """

        self._speed_dial_number = speed_dial_number

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
        if issubclass(InlineResponse20031KeyAssignment, dict):
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
        if not isinstance(other, InlineResponse20031KeyAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
