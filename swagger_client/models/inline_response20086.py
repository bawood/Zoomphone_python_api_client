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

class InlineResponse20086(object):
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
        'area_code': 'str',
        'audio_prompt_language': 'str',
        'company_number': 'str',
        'country': 'InlineResponse20086Country',
        'delegation': 'InlineResponse20086Delegation',
        'desk_phone': 'InlineResponse20086DeskPhone',
        'extension_number': 'int',
        'music_on_hold_id': 'str',
        'outbound_caller': 'InlineResponse20086OutboundCaller',
        'outbound_caller_ids': 'list[InlineResponse20086OutboundCallerIds]',
        'status': 'str',
        'voice_mail': 'list[InlineResponse20086VoiceMail]',
        'intercom': 'InlineResponse20086Intercom',
        'auto_call_recording_access_members': 'list[PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1]',
        'ad_hoc_call_recording_access_members': 'list[PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1]'
    }

    attribute_map = {
        'area_code': 'area_code',
        'audio_prompt_language': 'audio_prompt_language',
        'company_number': 'company_number',
        'country': 'country',
        'delegation': 'delegation',
        'desk_phone': 'desk_phone',
        'extension_number': 'extension_number',
        'music_on_hold_id': 'music_on_hold_id',
        'outbound_caller': 'outbound_caller',
        'outbound_caller_ids': 'outbound_caller_ids',
        'status': 'status',
        'voice_mail': 'voice_mail',
        'intercom': 'intercom',
        'auto_call_recording_access_members': 'auto_call_recording_access_members',
        'ad_hoc_call_recording_access_members': 'ad_hoc_call_recording_access_members'
    }

    def __init__(self, area_code=None, audio_prompt_language=None, company_number=None, country=None, delegation=None, desk_phone=None, extension_number=None, music_on_hold_id=None, outbound_caller=None, outbound_caller_ids=None, status=None, voice_mail=None, intercom=None, auto_call_recording_access_members=None, ad_hoc_call_recording_access_members=None):  # noqa: E501
        """InlineResponse20086 - a model defined in Swagger"""  # noqa: E501
        self._area_code = None
        self._audio_prompt_language = None
        self._company_number = None
        self._country = None
        self._delegation = None
        self._desk_phone = None
        self._extension_number = None
        self._music_on_hold_id = None
        self._outbound_caller = None
        self._outbound_caller_ids = None
        self._status = None
        self._voice_mail = None
        self._intercom = None
        self._auto_call_recording_access_members = None
        self._ad_hoc_call_recording_access_members = None
        self.discriminator = None
        if area_code is not None:
            self.area_code = area_code
        if audio_prompt_language is not None:
            self.audio_prompt_language = audio_prompt_language
        if company_number is not None:
            self.company_number = company_number
        if country is not None:
            self.country = country
        if delegation is not None:
            self.delegation = delegation
        if desk_phone is not None:
            self.desk_phone = desk_phone
        if extension_number is not None:
            self.extension_number = extension_number
        if music_on_hold_id is not None:
            self.music_on_hold_id = music_on_hold_id
        if outbound_caller is not None:
            self.outbound_caller = outbound_caller
        if outbound_caller_ids is not None:
            self.outbound_caller_ids = outbound_caller_ids
        if status is not None:
            self.status = status
        if voice_mail is not None:
            self.voice_mail = voice_mail
        if intercom is not None:
            self.intercom = intercom
        if auto_call_recording_access_members is not None:
            self.auto_call_recording_access_members = auto_call_recording_access_members
        if ad_hoc_call_recording_access_members is not None:
            self.ad_hoc_call_recording_access_members = ad_hoc_call_recording_access_members

    @property
    def area_code(self):
        """Gets the area_code of this InlineResponse20086.  # noqa: E501

        The area code of user.  # noqa: E501

        :return: The area_code of this InlineResponse20086.  # noqa: E501
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this InlineResponse20086.

        The area code of user.  # noqa: E501

        :param area_code: The area_code of this InlineResponse20086.  # noqa: E501
        :type: str
        """

        self._area_code = area_code

    @property
    def audio_prompt_language(self):
        """Gets the audio_prompt_language of this InlineResponse20086.  # noqa: E501

        The audio prompt language code.<br> American English: `en-US`<br> British English: `en-GB`<br> Español americano: `es-US`<br> Français canadien: `fr-CA`<br> Dansk: `da-DK`<br> Deutsch: `de-DE`<br> Español: `es-ES`<br> Français: `fr-FR`<br> Italiano: `it-IT`<br> Nederlands: `nl-NL`<br> Portugues portugal: `pt-PT`<br> Japanese: `ja-JP`<br> Korean: `ko-KO`<br> Portugues brasil: `pt-BR`<br> Chinese: `zh-CN`<br> Taiwanese: `zh-TW`<br>  # noqa: E501

        :return: The audio_prompt_language of this InlineResponse20086.  # noqa: E501
        :rtype: str
        """
        return self._audio_prompt_language

    @audio_prompt_language.setter
    def audio_prompt_language(self, audio_prompt_language):
        """Sets the audio_prompt_language of this InlineResponse20086.

        The audio prompt language code.<br> American English: `en-US`<br> British English: `en-GB`<br> Español americano: `es-US`<br> Français canadien: `fr-CA`<br> Dansk: `da-DK`<br> Deutsch: `de-DE`<br> Español: `es-ES`<br> Français: `fr-FR`<br> Italiano: `it-IT`<br> Nederlands: `nl-NL`<br> Portugues portugal: `pt-PT`<br> Japanese: `ja-JP`<br> Korean: `ko-KO`<br> Portugues brasil: `pt-BR`<br> Chinese: `zh-CN`<br> Taiwanese: `zh-TW`<br>  # noqa: E501

        :param audio_prompt_language: The audio_prompt_language of this InlineResponse20086.  # noqa: E501
        :type: str
        """

        self._audio_prompt_language = audio_prompt_language

    @property
    def company_number(self):
        """Gets the company_number of this InlineResponse20086.  # noqa: E501

        The [company number](https://support.zoom.us/hc/en-us/articles/360028553691) can be used by external callers to reach your phone users (by dialing the main company number and the user's extension). It can also be used by phone users as their caller ID when making calls.  # noqa: E501

        :return: The company_number of this InlineResponse20086.  # noqa: E501
        :rtype: str
        """
        return self._company_number

    @company_number.setter
    def company_number(self, company_number):
        """Sets the company_number of this InlineResponse20086.

        The [company number](https://support.zoom.us/hc/en-us/articles/360028553691) can be used by external callers to reach your phone users (by dialing the main company number and the user's extension). It can also be used by phone users as their caller ID when making calls.  # noqa: E501

        :param company_number: The company_number of this InlineResponse20086.  # noqa: E501
        :type: str
        """

        self._company_number = company_number

    @property
    def country(self):
        """Gets the country of this InlineResponse20086.  # noqa: E501


        :return: The country of this InlineResponse20086.  # noqa: E501
        :rtype: InlineResponse20086Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this InlineResponse20086.


        :param country: The country of this InlineResponse20086.  # noqa: E501
        :type: InlineResponse20086Country
        """

        self._country = country

    @property
    def delegation(self):
        """Gets the delegation of this InlineResponse20086.  # noqa: E501


        :return: The delegation of this InlineResponse20086.  # noqa: E501
        :rtype: InlineResponse20086Delegation
        """
        return self._delegation

    @delegation.setter
    def delegation(self, delegation):
        """Sets the delegation of this InlineResponse20086.


        :param delegation: The delegation of this InlineResponse20086.  # noqa: E501
        :type: InlineResponse20086Delegation
        """

        self._delegation = delegation

    @property
    def desk_phone(self):
        """Gets the desk_phone of this InlineResponse20086.  # noqa: E501


        :return: The desk_phone of this InlineResponse20086.  # noqa: E501
        :rtype: InlineResponse20086DeskPhone
        """
        return self._desk_phone

    @desk_phone.setter
    def desk_phone(self, desk_phone):
        """Sets the desk_phone of this InlineResponse20086.


        :param desk_phone: The desk_phone of this InlineResponse20086.  # noqa: E501
        :type: InlineResponse20086DeskPhone
        """

        self._desk_phone = desk_phone

    @property
    def extension_number(self):
        """Gets the extension_number of this InlineResponse20086.  # noqa: E501

        The owner's extension number.  # noqa: E501

        :return: The extension_number of this InlineResponse20086.  # noqa: E501
        :rtype: int
        """
        return self._extension_number

    @extension_number.setter
    def extension_number(self, extension_number):
        """Sets the extension_number of this InlineResponse20086.

        The owner's extension number.  # noqa: E501

        :param extension_number: The extension_number of this InlineResponse20086.  # noqa: E501
        :type: int
        """

        self._extension_number = extension_number

    @property
    def music_on_hold_id(self):
        """Gets the music_on_hold_id of this InlineResponse20086.  # noqa: E501

        The music on hold ID.   Options: empty char - default and `0` - disable  # noqa: E501

        :return: The music_on_hold_id of this InlineResponse20086.  # noqa: E501
        :rtype: str
        """
        return self._music_on_hold_id

    @music_on_hold_id.setter
    def music_on_hold_id(self, music_on_hold_id):
        """Sets the music_on_hold_id of this InlineResponse20086.

        The music on hold ID.   Options: empty char - default and `0` - disable  # noqa: E501

        :param music_on_hold_id: The music_on_hold_id of this InlineResponse20086.  # noqa: E501
        :type: str
        """

        self._music_on_hold_id = music_on_hold_id

    @property
    def outbound_caller(self):
        """Gets the outbound_caller of this InlineResponse20086.  # noqa: E501


        :return: The outbound_caller of this InlineResponse20086.  # noqa: E501
        :rtype: InlineResponse20086OutboundCaller
        """
        return self._outbound_caller

    @outbound_caller.setter
    def outbound_caller(self, outbound_caller):
        """Sets the outbound_caller of this InlineResponse20086.


        :param outbound_caller: The outbound_caller of this InlineResponse20086.  # noqa: E501
        :type: InlineResponse20086OutboundCaller
        """

        self._outbound_caller = outbound_caller

    @property
    def outbound_caller_ids(self):
        """Gets the outbound_caller_ids of this InlineResponse20086.  # noqa: E501


        :return: The outbound_caller_ids of this InlineResponse20086.  # noqa: E501
        :rtype: list[InlineResponse20086OutboundCallerIds]
        """
        return self._outbound_caller_ids

    @outbound_caller_ids.setter
    def outbound_caller_ids(self, outbound_caller_ids):
        """Sets the outbound_caller_ids of this InlineResponse20086.


        :param outbound_caller_ids: The outbound_caller_ids of this InlineResponse20086.  # noqa: E501
        :type: list[InlineResponse20086OutboundCallerIds]
        """

        self._outbound_caller_ids = outbound_caller_ids

    @property
    def status(self):
        """Gets the status of this InlineResponse20086.  # noqa: E501

        The status of the user.  # noqa: E501

        :return: The status of this InlineResponse20086.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20086.

        The status of the user.  # noqa: E501

        :param status: The status of this InlineResponse20086.  # noqa: E501
        :type: str
        """
        allowed_values = ["Active", "Inactive"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def voice_mail(self):
        """Gets the voice_mail of this InlineResponse20086.  # noqa: E501

        The shared voicemail access member list. <b>Deprecated</b>, we will completely deprecate this property in a future release. Instead use policy.voicemail_access_members property from 'Get a user's profile' API.  # noqa: E501

        :return: The voice_mail of this InlineResponse20086.  # noqa: E501
        :rtype: list[InlineResponse20086VoiceMail]
        """
        return self._voice_mail

    @voice_mail.setter
    def voice_mail(self, voice_mail):
        """Sets the voice_mail of this InlineResponse20086.

        The shared voicemail access member list. <b>Deprecated</b>, we will completely deprecate this property in a future release. Instead use policy.voicemail_access_members property from 'Get a user's profile' API.  # noqa: E501

        :param voice_mail: The voice_mail of this InlineResponse20086.  # noqa: E501
        :type: list[InlineResponse20086VoiceMail]
        """

        self._voice_mail = voice_mail

    @property
    def intercom(self):
        """Gets the intercom of this InlineResponse20086.  # noqa: E501


        :return: The intercom of this InlineResponse20086.  # noqa: E501
        :rtype: InlineResponse20086Intercom
        """
        return self._intercom

    @intercom.setter
    def intercom(self, intercom):
        """Sets the intercom of this InlineResponse20086.


        :param intercom: The intercom of this InlineResponse20086.  # noqa: E501
        :type: InlineResponse20086Intercom
        """

        self._intercom = intercom

    @property
    def auto_call_recording_access_members(self):
        """Gets the auto_call_recording_access_members of this InlineResponse20086.  # noqa: E501

        The shared automatic call recording access member list. <b>Deprecated</b>, we will completely deprecate this property in a future release. Instead use policy.auto_call_recording_access_members property from 'Get a user's profile' API.  # noqa: E501

        :return: The auto_call_recording_access_members of this InlineResponse20086.  # noqa: E501
        :rtype: list[PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1]
        """
        return self._auto_call_recording_access_members

    @auto_call_recording_access_members.setter
    def auto_call_recording_access_members(self, auto_call_recording_access_members):
        """Sets the auto_call_recording_access_members of this InlineResponse20086.

        The shared automatic call recording access member list. <b>Deprecated</b>, we will completely deprecate this property in a future release. Instead use policy.auto_call_recording_access_members property from 'Get a user's profile' API.  # noqa: E501

        :param auto_call_recording_access_members: The auto_call_recording_access_members of this InlineResponse20086.  # noqa: E501
        :type: list[PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1]
        """

        self._auto_call_recording_access_members = auto_call_recording_access_members

    @property
    def ad_hoc_call_recording_access_members(self):
        """Gets the ad_hoc_call_recording_access_members of this InlineResponse20086.  # noqa: E501

        The shared ad hoc call recording access member list. <b>Deprecated</b>, we will completely deprecate this property in a future release. Instead use policy.ad_hoc_call_recording_access_members property from 'Get a user's profile' API.  # noqa: E501

        :return: The ad_hoc_call_recording_access_members of this InlineResponse20086.  # noqa: E501
        :rtype: list[PhoneusersuserIdsettingssettingTypeAutoCallRecordingAccessMembers1]
        """
        return self._ad_hoc_call_recording_access_members

    @ad_hoc_call_recording_access_members.setter
    def ad_hoc_call_recording_access_members(self, ad_hoc_call_recording_access_members):
        """Sets the ad_hoc_call_recording_access_members of this InlineResponse20086.

        The shared ad hoc call recording access member list. <b>Deprecated</b>, we will completely deprecate this property in a future release. Instead use policy.ad_hoc_call_recording_access_members property from 'Get a user's profile' API.  # noqa: E501

        :param ad_hoc_call_recording_access_members: The ad_hoc_call_recording_access_members of this InlineResponse20086.  # noqa: E501
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
        if issubclass(InlineResponse20086, dict):
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
        if not isinstance(other, InlineResponse20086):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
