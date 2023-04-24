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

class InlineResponse20069PolicySms(object):
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
        'international_sms': 'bool',
        'international_sms_countries': 'list[str]',
        'locked': 'bool',
        'locked_by': 'str',
        'modified': 'bool'
    }

    attribute_map = {
        'enable': 'enable',
        'international_sms': 'international_sms',
        'international_sms_countries': 'international_sms_countries',
        'locked': 'locked',
        'locked_by': 'locked_by',
        'modified': 'modified'
    }

    def __init__(self, enable=None, international_sms=None, international_sms_countries=None, locked=None, locked_by=None, modified=None):  # noqa: E501
        """InlineResponse20069PolicySms - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._international_sms = None
        self._international_sms_countries = None
        self._locked = None
        self._locked_by = None
        self._modified = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if international_sms is not None:
            self.international_sms = international_sms
        if international_sms_countries is not None:
            self.international_sms_countries = international_sms_countries
        if locked is not None:
            self.locked = locked
        if locked_by is not None:
            self.locked_by = locked_by
        if modified is not None:
            self.modified = modified

    @property
    def enable(self):
        """Gets the enable of this InlineResponse20069PolicySms.  # noqa: E501

        Whether to allow users, call queues, and auto receptionists to send and receive messages. You will still need to assign a valid calling plan and phone number to each user for them to send and receive messages.  # noqa: E501

        :return: The enable of this InlineResponse20069PolicySms.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this InlineResponse20069PolicySms.

        Whether to allow users, call queues, and auto receptionists to send and receive messages. You will still need to assign a valid calling plan and phone number to each user for them to send and receive messages.  # noqa: E501

        :param enable: The enable of this InlineResponse20069PolicySms.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def international_sms(self):
        """Gets the international_sms of this InlineResponse20069PolicySms.  # noqa: E501

        Whether the user can send and receive international messages.  # noqa: E501

        :return: The international_sms of this InlineResponse20069PolicySms.  # noqa: E501
        :rtype: bool
        """
        return self._international_sms

    @international_sms.setter
    def international_sms(self, international_sms):
        """Sets the international_sms of this InlineResponse20069PolicySms.

        Whether the user can send and receive international messages.  # noqa: E501

        :param international_sms: The international_sms of this InlineResponse20069PolicySms.  # noqa: E501
        :type: bool
        """

        self._international_sms = international_sms

    @property
    def international_sms_countries(self):
        """Gets the international_sms_countries of this InlineResponse20069PolicySms.  # noqa: E501

        The country to which users can send and receive international messages. The [country ISO code](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries).  # noqa: E501

        :return: The international_sms_countries of this InlineResponse20069PolicySms.  # noqa: E501
        :rtype: list[str]
        """
        return self._international_sms_countries

    @international_sms_countries.setter
    def international_sms_countries(self, international_sms_countries):
        """Sets the international_sms_countries of this InlineResponse20069PolicySms.

        The country to which users can send and receive international messages. The [country ISO code](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries).  # noqa: E501

        :param international_sms_countries: The international_sms_countries of this InlineResponse20069PolicySms.  # noqa: E501
        :type: list[str]
        """

        self._international_sms_countries = international_sms_countries

    @property
    def locked(self):
        """Gets the locked of this InlineResponse20069PolicySms.  # noqa: E501

        Whether the senior administrator allows users to modify the current settings.  # noqa: E501

        :return: The locked of this InlineResponse20069PolicySms.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this InlineResponse20069PolicySms.

        Whether the senior administrator allows users to modify the current settings.  # noqa: E501

        :param locked: The locked of this InlineResponse20069PolicySms.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def locked_by(self):
        """Gets the locked_by of this InlineResponse20069PolicySms.  # noqa: E501

        Which level of administrator prohibits modifying the current settings.  # noqa: E501

        :return: The locked_by of this InlineResponse20069PolicySms.  # noqa: E501
        :rtype: str
        """
        return self._locked_by

    @locked_by.setter
    def locked_by(self, locked_by):
        """Sets the locked_by of this InlineResponse20069PolicySms.

        Which level of administrator prohibits modifying the current settings.  # noqa: E501

        :param locked_by: The locked_by of this InlineResponse20069PolicySms.  # noqa: E501
        :type: str
        """
        allowed_values = ["invalid", "account", "site"]  # noqa: E501
        if locked_by not in allowed_values:
            raise ValueError(
                "Invalid value for `locked_by` ({0}), must be one of {1}"  # noqa: E501
                .format(locked_by, allowed_values)
            )

        self._locked_by = locked_by

    @property
    def modified(self):
        """Gets the modified of this InlineResponse20069PolicySms.  # noqa: E501

        Whether the current settings have been modified. If modified, they can be reset (displayed when using the new policy framework).  # noqa: E501

        :return: The modified of this InlineResponse20069PolicySms.  # noqa: E501
        :rtype: bool
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this InlineResponse20069PolicySms.

        Whether the current settings have been modified. If modified, they can be reset (displayed when using the new policy framework).  # noqa: E501

        :param modified: The modified of this InlineResponse20069PolicySms.  # noqa: E501
        :type: bool
        """

        self._modified = modified

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
        if issubclass(InlineResponse20069PolicySms, dict):
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
        if not isinstance(other, InlineResponse20069PolicySms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
