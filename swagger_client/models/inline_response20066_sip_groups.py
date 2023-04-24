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

class InlineResponse20066SipGroups(object):
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
        'description': 'str',
        'display_name': 'str',
        'id': 'str',
        'send_sip_group_name': 'bool',
        'sip_trunk': 'InlineResponse20066SipTrunk'
    }

    attribute_map = {
        'description': 'description',
        'display_name': 'display_name',
        'id': 'id',
        'send_sip_group_name': 'send_sip_group_name',
        'sip_trunk': 'sip_trunk'
    }

    def __init__(self, description=None, display_name=None, id=None, send_sip_group_name=None, sip_trunk=None):  # noqa: E501
        """InlineResponse20066SipGroups - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._display_name = None
        self._id = None
        self._send_sip_group_name = None
        self._sip_trunk = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if send_sip_group_name is not None:
            self.send_sip_group_name = send_sip_group_name
        if sip_trunk is not None:
            self.sip_trunk = sip_trunk

    @property
    def description(self):
        """Gets the description of this InlineResponse20066SipGroups.  # noqa: E501

        The SIP group's description.  # noqa: E501

        :return: The description of this InlineResponse20066SipGroups.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse20066SipGroups.

        The SIP group's description.  # noqa: E501

        :param description: The description of this InlineResponse20066SipGroups.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this InlineResponse20066SipGroups.  # noqa: E501

        The SIP group's display name.  # noqa: E501

        :return: The display_name of this InlineResponse20066SipGroups.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InlineResponse20066SipGroups.

        The SIP group's display name.  # noqa: E501

        :param display_name: The display_name of this InlineResponse20066SipGroups.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this InlineResponse20066SipGroups.  # noqa: E501

        The SIP group's ID.  # noqa: E501

        :return: The id of this InlineResponse20066SipGroups.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20066SipGroups.

        The SIP group's ID.  # noqa: E501

        :param id: The id of this InlineResponse20066SipGroups.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def send_sip_group_name(self):
        """Gets the send_sip_group_name of this InlineResponse20066SipGroups.  # noqa: E501

        Whether the SIP group's name is sent in the SIP header.  # noqa: E501

        :return: The send_sip_group_name of this InlineResponse20066SipGroups.  # noqa: E501
        :rtype: bool
        """
        return self._send_sip_group_name

    @send_sip_group_name.setter
    def send_sip_group_name(self, send_sip_group_name):
        """Sets the send_sip_group_name of this InlineResponse20066SipGroups.

        Whether the SIP group's name is sent in the SIP header.  # noqa: E501

        :param send_sip_group_name: The send_sip_group_name of this InlineResponse20066SipGroups.  # noqa: E501
        :type: bool
        """

        self._send_sip_group_name = send_sip_group_name

    @property
    def sip_trunk(self):
        """Gets the sip_trunk of this InlineResponse20066SipGroups.  # noqa: E501


        :return: The sip_trunk of this InlineResponse20066SipGroups.  # noqa: E501
        :rtype: InlineResponse20066SipTrunk
        """
        return self._sip_trunk

    @sip_trunk.setter
    def sip_trunk(self, sip_trunk):
        """Sets the sip_trunk of this InlineResponse20066SipGroups.


        :param sip_trunk: The sip_trunk of this InlineResponse20066SipGroups.  # noqa: E501
        :type: InlineResponse20066SipTrunk
        """

        self._sip_trunk = sip_trunk

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
        if issubclass(InlineResponse20066SipGroups, dict):
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
        if not isinstance(other, InlineResponse20066SipGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
