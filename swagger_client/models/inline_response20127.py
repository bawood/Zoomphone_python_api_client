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

class InlineResponse20127(object):
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
        'delegation': 'InlineResponse20127Delegation',
        'voice_mail': 'InlineResponse20127VoiceMail',
        'voicemail_access_members': 'list[PhoneusersuserIdsettingssettingTypeVoicemailAccessMembers]',
        'auto_call_recording_access_members': 'list[PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1]',
        'ad_hoc_call_recording_access_members': 'list[PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1]'
    }

    attribute_map = {
        'delegation': 'delegation',
        'voice_mail': 'voice_mail',
        'voicemail_access_members': 'voicemail_access_members',
        'auto_call_recording_access_members': 'auto_call_recording_access_members',
        'ad_hoc_call_recording_access_members': 'ad_hoc_call_recording_access_members'
    }

    def __init__(self, delegation=None, voice_mail=None, voicemail_access_members=None, auto_call_recording_access_members=None, ad_hoc_call_recording_access_members=None):  # noqa: E501
        """InlineResponse20127 - a model defined in Swagger"""  # noqa: E501
        self._delegation = None
        self._voice_mail = None
        self._voicemail_access_members = None
        self._auto_call_recording_access_members = None
        self._ad_hoc_call_recording_access_members = None
        self.discriminator = None
        if delegation is not None:
            self.delegation = delegation
        if voice_mail is not None:
            self.voice_mail = voice_mail
        if voicemail_access_members is not None:
            self.voicemail_access_members = voicemail_access_members
        if auto_call_recording_access_members is not None:
            self.auto_call_recording_access_members = auto_call_recording_access_members
        if ad_hoc_call_recording_access_members is not None:
            self.ad_hoc_call_recording_access_members = ad_hoc_call_recording_access_members

    @property
    def delegation(self):
        """Gets the delegation of this InlineResponse20127.  # noqa: E501


        :return: The delegation of this InlineResponse20127.  # noqa: E501
        :rtype: InlineResponse20127Delegation
        """
        return self._delegation

    @delegation.setter
    def delegation(self, delegation):
        """Sets the delegation of this InlineResponse20127.


        :param delegation: The delegation of this InlineResponse20127.  # noqa: E501
        :type: InlineResponse20127Delegation
        """

        self._delegation = delegation

    @property
    def voice_mail(self):
        """Gets the voice_mail of this InlineResponse20127.  # noqa: E501


        :return: The voice_mail of this InlineResponse20127.  # noqa: E501
        :rtype: InlineResponse20127VoiceMail
        """
        return self._voice_mail

    @voice_mail.setter
    def voice_mail(self, voice_mail):
        """Sets the voice_mail of this InlineResponse20127.


        :param voice_mail: The voice_mail of this InlineResponse20127.  # noqa: E501
        :type: InlineResponse20127VoiceMail
        """

        self._voice_mail = voice_mail

    @property
    def voicemail_access_members(self):
        """Gets the voicemail_access_members of this InlineResponse20127.  # noqa: E501

        The shared voicemail access member list.  # noqa: E501

        :return: The voicemail_access_members of this InlineResponse20127.  # noqa: E501
        :rtype: list[PhoneusersuserIdsettingssettingTypeVoicemailAccessMembers]
        """
        return self._voicemail_access_members

    @voicemail_access_members.setter
    def voicemail_access_members(self, voicemail_access_members):
        """Sets the voicemail_access_members of this InlineResponse20127.

        The shared voicemail access member list.  # noqa: E501

        :param voicemail_access_members: The voicemail_access_members of this InlineResponse20127.  # noqa: E501
        :type: list[PhoneusersuserIdsettingssettingTypeVoicemailAccessMembers]
        """

        self._voicemail_access_members = voicemail_access_members

    @property
    def auto_call_recording_access_members(self):
        """Gets the auto_call_recording_access_members of this InlineResponse20127.  # noqa: E501

        The shared automatic call recording access member list.  # noqa: E501

        :return: The auto_call_recording_access_members of this InlineResponse20127.  # noqa: E501
        :rtype: list[PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1]
        """
        return self._auto_call_recording_access_members

    @auto_call_recording_access_members.setter
    def auto_call_recording_access_members(self, auto_call_recording_access_members):
        """Sets the auto_call_recording_access_members of this InlineResponse20127.

        The shared automatic call recording access member list.  # noqa: E501

        :param auto_call_recording_access_members: The auto_call_recording_access_members of this InlineResponse20127.  # noqa: E501
        :type: list[PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1]
        """

        self._auto_call_recording_access_members = auto_call_recording_access_members

    @property
    def ad_hoc_call_recording_access_members(self):
        """Gets the ad_hoc_call_recording_access_members of this InlineResponse20127.  # noqa: E501

        The shared ad hoc call recording access member list.  # noqa: E501

        :return: The ad_hoc_call_recording_access_members of this InlineResponse20127.  # noqa: E501
        :rtype: list[PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1]
        """
        return self._ad_hoc_call_recording_access_members

    @ad_hoc_call_recording_access_members.setter
    def ad_hoc_call_recording_access_members(self, ad_hoc_call_recording_access_members):
        """Sets the ad_hoc_call_recording_access_members of this InlineResponse20127.

        The shared ad hoc call recording access member list.  # noqa: E501

        :param ad_hoc_call_recording_access_members: The ad_hoc_call_recording_access_members of this InlineResponse20127.  # noqa: E501
        :type: list[PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1]
        """

        self._ad_hoc_call_recording_access_members = ad_hoc_call_recording_access_members

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
        if issubclass(InlineResponse20127, dict):
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
        if not isinstance(other, InlineResponse20127):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other