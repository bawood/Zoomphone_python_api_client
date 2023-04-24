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

class PhonesettingTemplatestemplateIdUserSettings(object):
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
        'audio_prompt_language': 'str',
        'block_calls_without_caller_id': 'bool',
        'call_handling': 'PhonesettingTemplatestemplateIdUserSettingsCallHandling',
        'desk_phone': 'PhonesettingTemplatestemplateIdUserSettingsDeskPhone',
        'hold_music': 'str'
    }

    attribute_map = {
        'audio_prompt_language': 'audio_prompt_language',
        'block_calls_without_caller_id': 'block_calls_without_caller_id',
        'call_handling': 'call_handling',
        'desk_phone': 'desk_phone',
        'hold_music': 'hold_music'
    }

    def __init__(self, audio_prompt_language=None, block_calls_without_caller_id=None, call_handling=None, desk_phone=None, hold_music=None):  # noqa: E501
        """PhonesettingTemplatestemplateIdUserSettings - a model defined in Swagger"""  # noqa: E501
        self._audio_prompt_language = None
        self._block_calls_without_caller_id = None
        self._call_handling = None
        self._desk_phone = None
        self._hold_music = None
        self.discriminator = None
        if audio_prompt_language is not None:
            self.audio_prompt_language = audio_prompt_language
        if block_calls_without_caller_id is not None:
            self.block_calls_without_caller_id = block_calls_without_caller_id
        if call_handling is not None:
            self.call_handling = call_handling
        if desk_phone is not None:
            self.desk_phone = desk_phone
        if hold_music is not None:
            self.hold_music = hold_music

    @property
    def audio_prompt_language(self):
        """Gets the audio_prompt_language of this PhonesettingTemplatestemplateIdUserSettings.  # noqa: E501

        Audio prompt language code.  American English: `en-US`  British English: `en-GB`  Español americano: `es-US`  Français canadien: `fr-CA`  Dansk: `da-DK`  Deutsch: `de-DE`  Español: `es-ES`  Français: `fr-FR`  Italiano: `it-IT`  Nederlands: `nl-NL`  Portugues portugal: `pt-PT`  Japanese: `ja-JP`  Korean: `ko-KO`  Portugues brasil: `pt-BR`  Chinese: `zh-CN`  Taiwanese: `zh-TW`   # noqa: E501

        :return: The audio_prompt_language of this PhonesettingTemplatestemplateIdUserSettings.  # noqa: E501
        :rtype: str
        """
        return self._audio_prompt_language

    @audio_prompt_language.setter
    def audio_prompt_language(self, audio_prompt_language):
        """Sets the audio_prompt_language of this PhonesettingTemplatestemplateIdUserSettings.

        Audio prompt language code.  American English: `en-US`  British English: `en-GB`  Español americano: `es-US`  Français canadien: `fr-CA`  Dansk: `da-DK`  Deutsch: `de-DE`  Español: `es-ES`  Français: `fr-FR`  Italiano: `it-IT`  Nederlands: `nl-NL`  Portugues portugal: `pt-PT`  Japanese: `ja-JP`  Korean: `ko-KO`  Portugues brasil: `pt-BR`  Chinese: `zh-CN`  Taiwanese: `zh-TW`   # noqa: E501

        :param audio_prompt_language: The audio_prompt_language of this PhonesettingTemplatestemplateIdUserSettings.  # noqa: E501
        :type: str
        """

        self._audio_prompt_language = audio_prompt_language

    @property
    def block_calls_without_caller_id(self):
        """Gets the block_calls_without_caller_id of this PhonesettingTemplatestemplateIdUserSettings.  # noqa: E501

        The block calls without caller ID.  # noqa: E501

        :return: The block_calls_without_caller_id of this PhonesettingTemplatestemplateIdUserSettings.  # noqa: E501
        :rtype: bool
        """
        return self._block_calls_without_caller_id

    @block_calls_without_caller_id.setter
    def block_calls_without_caller_id(self, block_calls_without_caller_id):
        """Sets the block_calls_without_caller_id of this PhonesettingTemplatestemplateIdUserSettings.

        The block calls without caller ID.  # noqa: E501

        :param block_calls_without_caller_id: The block_calls_without_caller_id of this PhonesettingTemplatestemplateIdUserSettings.  # noqa: E501
        :type: bool
        """

        self._block_calls_without_caller_id = block_calls_without_caller_id

    @property
    def call_handling(self):
        """Gets the call_handling of this PhonesettingTemplatestemplateIdUserSettings.  # noqa: E501


        :return: The call_handling of this PhonesettingTemplatestemplateIdUserSettings.  # noqa: E501
        :rtype: PhonesettingTemplatestemplateIdUserSettingsCallHandling
        """
        return self._call_handling

    @call_handling.setter
    def call_handling(self, call_handling):
        """Sets the call_handling of this PhonesettingTemplatestemplateIdUserSettings.


        :param call_handling: The call_handling of this PhonesettingTemplatestemplateIdUserSettings.  # noqa: E501
        :type: PhonesettingTemplatestemplateIdUserSettingsCallHandling
        """

        self._call_handling = call_handling

    @property
    def desk_phone(self):
        """Gets the desk_phone of this PhonesettingTemplatestemplateIdUserSettings.  # noqa: E501


        :return: The desk_phone of this PhonesettingTemplatestemplateIdUserSettings.  # noqa: E501
        :rtype: PhonesettingTemplatestemplateIdUserSettingsDeskPhone
        """
        return self._desk_phone

    @desk_phone.setter
    def desk_phone(self, desk_phone):
        """Sets the desk_phone of this PhonesettingTemplatestemplateIdUserSettings.


        :param desk_phone: The desk_phone of this PhonesettingTemplatestemplateIdUserSettings.  # noqa: E501
        :type: PhonesettingTemplatestemplateIdUserSettingsDeskPhone
        """

        self._desk_phone = desk_phone

    @property
    def hold_music(self):
        """Gets the hold_music of this PhonesettingTemplatestemplateIdUserSettings.  # noqa: E501

        The value of this field can be either `default` or `disable`.  * `default`: This means that the hold music can be set using the [audio library](https://support.zoom.us/hc/en-us/articles/360028212652-Using-the-audio-library-to-customize-greetings-and-hold-music).  * `disable`: This means that the hold music is disabled.  # noqa: E501

        :return: The hold_music of this PhonesettingTemplatestemplateIdUserSettings.  # noqa: E501
        :rtype: str
        """
        return self._hold_music

    @hold_music.setter
    def hold_music(self, hold_music):
        """Sets the hold_music of this PhonesettingTemplatestemplateIdUserSettings.

        The value of this field can be either `default` or `disable`.  * `default`: This means that the hold music can be set using the [audio library](https://support.zoom.us/hc/en-us/articles/360028212652-Using-the-audio-library-to-customize-greetings-and-hold-music).  * `disable`: This means that the hold music is disabled.  # noqa: E501

        :param hold_music: The hold_music of this PhonesettingTemplatestemplateIdUserSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["default", "disable"]  # noqa: E501
        if hold_music not in allowed_values:
            raise ValueError(
                "Invalid value for `hold_music` ({0}), must be one of {1}"  # noqa: E501
                .format(hold_music, allowed_values)
            )

        self._hold_music = hold_music

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
        if issubclass(PhonesettingTemplatestemplateIdUserSettings, dict):
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
        if not isinstance(other, PhonesettingTemplatestemplateIdUserSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other