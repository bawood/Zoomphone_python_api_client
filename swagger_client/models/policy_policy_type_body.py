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

class PolicyPolicyTypeBody(object):
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
        'voicemail_access_members': 'list[PhonesharedLineGroupssharedLineGroupIdpolicypolicyTypeVoicemailAccessMembers]'
    }

    attribute_map = {
        'voicemail_access_members': 'voicemail_access_members'
    }

    def __init__(self, voicemail_access_members=None):  # noqa: E501
        """PolicyPolicyTypeBody - a model defined in Swagger"""  # noqa: E501
        self._voicemail_access_members = None
        self.discriminator = None
        if voicemail_access_members is not None:
            self.voicemail_access_members = voicemail_access_members

    @property
    def voicemail_access_members(self):
        """Gets the voicemail_access_members of this PolicyPolicyTypeBody.  # noqa: E501

        The shared voicemail access member list.  # noqa: E501

        :return: The voicemail_access_members of this PolicyPolicyTypeBody.  # noqa: E501
        :rtype: list[PhonesharedLineGroupssharedLineGroupIdpolicypolicyTypeVoicemailAccessMembers]
        """
        return self._voicemail_access_members

    @voicemail_access_members.setter
    def voicemail_access_members(self, voicemail_access_members):
        """Sets the voicemail_access_members of this PolicyPolicyTypeBody.

        The shared voicemail access member list.  # noqa: E501

        :param voicemail_access_members: The voicemail_access_members of this PolicyPolicyTypeBody.  # noqa: E501
        :type: list[PhonesharedLineGroupssharedLineGroupIdpolicypolicyTypeVoicemailAccessMembers]
        """

        self._voicemail_access_members = voicemail_access_members

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
        if issubclass(PolicyPolicyTypeBody, dict):
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
        if not isinstance(other, PolicyPolicyTypeBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
