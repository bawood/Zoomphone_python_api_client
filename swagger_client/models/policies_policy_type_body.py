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

class PoliciesPolicyTypeBody(object):
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
        'voicemail_access_member': 'PhoneautoReceptionistsautoReceptionistIdpoliciespolicyTypeVoicemailAccessMember'
    }

    attribute_map = {
        'voicemail_access_member': 'voicemail_access_member'
    }

    def __init__(self, voicemail_access_member=None):  # noqa: E501
        """PoliciesPolicyTypeBody - a model defined in Swagger"""  # noqa: E501
        self._voicemail_access_member = None
        self.discriminator = None
        if voicemail_access_member is not None:
            self.voicemail_access_member = voicemail_access_member

    @property
    def voicemail_access_member(self):
        """Gets the voicemail_access_member of this PoliciesPolicyTypeBody.  # noqa: E501


        :return: The voicemail_access_member of this PoliciesPolicyTypeBody.  # noqa: E501
        :rtype: PhoneautoReceptionistsautoReceptionistIdpoliciespolicyTypeVoicemailAccessMember
        """
        return self._voicemail_access_member

    @voicemail_access_member.setter
    def voicemail_access_member(self, voicemail_access_member):
        """Sets the voicemail_access_member of this PoliciesPolicyTypeBody.


        :param voicemail_access_member: The voicemail_access_member of this PoliciesPolicyTypeBody.  # noqa: E501
        :type: PhoneautoReceptionistsautoReceptionistIdpoliciespolicyTypeVoicemailAccessMember
        """

        self._voicemail_access_member = voicemail_access_member

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
        if issubclass(PoliciesPolicyTypeBody, dict):
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
        if not isinstance(other, PoliciesPolicyTypeBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
