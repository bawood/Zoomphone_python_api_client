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

class InlineResponse20127Delegation(object):
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
        'assistants': 'list[InlineResponse20127DelegationAssistants]',
        'privacy': 'bool',
        'privileges': 'list[int]'
    }

    attribute_map = {
        'assistants': 'assistants',
        'privacy': 'privacy',
        'privileges': 'privileges'
    }

    def __init__(self, assistants=None, privacy=None, privileges=None):  # noqa: E501
        """InlineResponse20127Delegation - a model defined in Swagger"""  # noqa: E501
        self._assistants = None
        self._privacy = None
        self._privileges = None
        self.discriminator = None
        if assistants is not None:
            self.assistants = assistants
        if privacy is not None:
            self.privacy = privacy
        if privileges is not None:
            self.privileges = privileges

    @property
    def assistants(self):
        """Gets the assistants of this InlineResponse20127Delegation.  # noqa: E501

        The delegation assistants.  # noqa: E501

        :return: The assistants of this InlineResponse20127Delegation.  # noqa: E501
        :rtype: list[InlineResponse20127DelegationAssistants]
        """
        return self._assistants

    @assistants.setter
    def assistants(self, assistants):
        """Sets the assistants of this InlineResponse20127Delegation.

        The delegation assistants.  # noqa: E501

        :param assistants: The assistants of this InlineResponse20127Delegation.  # noqa: E501
        :type: list[InlineResponse20127DelegationAssistants]
        """

        self._assistants = assistants

    @property
    def privacy(self):
        """Gets the privacy of this InlineResponse20127Delegation.  # noqa: E501

        Whether to allow members to prevent others from picking up a held call, and listening, whispering, barging, or taking over a call if it's configured.  # noqa: E501

        :return: The privacy of this InlineResponse20127Delegation.  # noqa: E501
        :rtype: bool
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """Sets the privacy of this InlineResponse20127Delegation.

        Whether to allow members to prevent others from picking up a held call, and listening, whispering, barging, or taking over a call if it's configured.  # noqa: E501

        :param privacy: The privacy of this InlineResponse20127Delegation.  # noqa: E501
        :type: bool
        """

        self._privacy = privacy

    @property
    def privileges(self):
        """Gets the privileges of this InlineResponse20127Delegation.  # noqa: E501

        The delegation privileges. 1-Place Calls, 2-Answer Calls, 3- Pick Up Hold Calls.  # noqa: E501

        :return: The privileges of this InlineResponse20127Delegation.  # noqa: E501
        :rtype: list[int]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this InlineResponse20127Delegation.

        The delegation privileges. 1-Place Calls, 2-Answer Calls, 3- Pick Up Hold Calls.  # noqa: E501

        :param privileges: The privileges of this InlineResponse20127Delegation.  # noqa: E501
        :type: list[int]
        """

        self._privileges = privileges

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
        if issubclass(InlineResponse20127Delegation, dict):
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
        if not isinstance(other, InlineResponse20127Delegation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
