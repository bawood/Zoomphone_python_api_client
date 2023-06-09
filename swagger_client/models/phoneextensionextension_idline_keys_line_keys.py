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

class PhoneextensionextensionIdlineKeysLineKeys(object):
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
        'line_key_id': 'str',
        'index': 'int',
        'type': 'str',
        'key_assignment': 'PhoneextensionextensionIdlineKeysKeyAssignment',
        'alias': 'str',
        'outbound_caller_id': 'str'
    }

    attribute_map = {
        'line_key_id': 'line_key_id',
        'index': 'index',
        'type': 'type',
        'key_assignment': 'key_assignment',
        'alias': 'alias',
        'outbound_caller_id': 'outbound_caller_id'
    }

    def __init__(self, line_key_id=None, index=None, type=None, key_assignment=None, alias=None, outbound_caller_id=None):  # noqa: E501
        """PhoneextensionextensionIdlineKeysLineKeys - a model defined in Swagger"""  # noqa: E501
        self._line_key_id = None
        self._index = None
        self._type = None
        self._key_assignment = None
        self._alias = None
        self._outbound_caller_id = None
        self.discriminator = None
        if line_key_id is not None:
            self.line_key_id = line_key_id
        if index is not None:
            self.index = index
        if type is not None:
            self.type = type
        if key_assignment is not None:
            self.key_assignment = key_assignment
        if alias is not None:
            self.alias = alias
        if outbound_caller_id is not None:
            self.outbound_caller_id = outbound_caller_id

    @property
    def line_key_id(self):
        """Gets the line_key_id of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501

        The line key ID.  # noqa: E501

        :return: The line_key_id of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501
        :rtype: str
        """
        return self._line_key_id

    @line_key_id.setter
    def line_key_id(self, line_key_id):
        """Sets the line_key_id of this PhoneextensionextensionIdlineKeysLineKeys.

        The line key ID.  # noqa: E501

        :param line_key_id: The line_key_id of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501
        :type: str
        """

        self._line_key_id = line_key_id

    @property
    def index(self):
        """Gets the index of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501

        The order of the line key on the phone.  # noqa: E501

        :return: The index of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this PhoneextensionextensionIdlineKeysLineKeys.

        The order of the line key on the phone.  # noqa: E501

        :param index: The index of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def type(self):
        """Gets the type of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501

        The line key type.   `line`: Line/Shared line access/Shared line group.  `blf`: Busy lamp field.  `speed_dial`: Speed-dial a phone number.  `zoom_meeting`: Desk phone companion mode.  `call_park`: Call park. Users don't need to dial the retrieval codes with this setting.  `group_call_pickup`: Pick up inbound calls for call pickup groups.  # noqa: E501

        :return: The type of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PhoneextensionextensionIdlineKeysLineKeys.

        The line key type.   `line`: Line/Shared line access/Shared line group.  `blf`: Busy lamp field.  `speed_dial`: Speed-dial a phone number.  `zoom_meeting`: Desk phone companion mode.  `call_park`: Call park. Users don't need to dial the retrieval codes with this setting.  `group_call_pickup`: Pick up inbound calls for call pickup groups.  # noqa: E501

        :param type: The type of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501
        :type: str
        """
        allowed_values = ["line", "blf", "speed_dial", "zoom_meeting", "call_park", "group_call_pickup"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def key_assignment(self):
        """Gets the key_assignment of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501


        :return: The key_assignment of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501
        :rtype: PhoneextensionextensionIdlineKeysKeyAssignment
        """
        return self._key_assignment

    @key_assignment.setter
    def key_assignment(self, key_assignment):
        """Sets the key_assignment of this PhoneextensionextensionIdlineKeysLineKeys.


        :param key_assignment: The key_assignment of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501
        :type: PhoneextensionextensionIdlineKeysKeyAssignment
        """

        self._key_assignment = key_assignment

    @property
    def alias(self):
        """Gets the alias of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501

        The user-defined display name for each line key of the device. The alias can be up to 32 characters in length.  # noqa: E501

        :return: The alias of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this PhoneextensionextensionIdlineKeysLineKeys.

        The user-defined display name for each line key of the device. The alias can be up to 32 characters in length.  # noqa: E501

        :param alias: The alias of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def outbound_caller_id(self):
        """Gets the outbound_caller_id of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501

        The mapping ID of the parameter `outbound_caller_number`. Hides the caller ID if set to `anonymous`.  # noqa: E501

        :return: The outbound_caller_id of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501
        :rtype: str
        """
        return self._outbound_caller_id

    @outbound_caller_id.setter
    def outbound_caller_id(self, outbound_caller_id):
        """Sets the outbound_caller_id of this PhoneextensionextensionIdlineKeysLineKeys.

        The mapping ID of the parameter `outbound_caller_number`. Hides the caller ID if set to `anonymous`.  # noqa: E501

        :param outbound_caller_id: The outbound_caller_id of this PhoneextensionextensionIdlineKeysLineKeys.  # noqa: E501
        :type: str
        """

        self._outbound_caller_id = outbound_caller_id

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
        if issubclass(PhoneextensionextensionIdlineKeysLineKeys, dict):
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
        if not isinstance(other, PhoneextensionextensionIdlineKeysLineKeys):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
