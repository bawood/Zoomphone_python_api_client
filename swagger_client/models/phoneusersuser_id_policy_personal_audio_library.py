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

class PhoneusersuserIdPolicyPersonalAudioLibrary(object):
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
        'allow_music_on_hold_customization': 'bool',
        'allow_voicemail_and_message_greeting_customization': 'bool',
        'enable': 'bool',
        'reset': 'bool'
    }

    attribute_map = {
        'allow_music_on_hold_customization': 'allow_music_on_hold_customization',
        'allow_voicemail_and_message_greeting_customization': 'allow_voicemail_and_message_greeting_customization',
        'enable': 'enable',
        'reset': 'reset'
    }

    def __init__(self, allow_music_on_hold_customization=None, allow_voicemail_and_message_greeting_customization=None, enable=None, reset=None):  # noqa: E501
        """PhoneusersuserIdPolicyPersonalAudioLibrary - a model defined in Swagger"""  # noqa: E501
        self._allow_music_on_hold_customization = None
        self._allow_voicemail_and_message_greeting_customization = None
        self._enable = None
        self._reset = None
        self.discriminator = None
        if allow_music_on_hold_customization is not None:
            self.allow_music_on_hold_customization = allow_music_on_hold_customization
        if allow_voicemail_and_message_greeting_customization is not None:
            self.allow_voicemail_and_message_greeting_customization = allow_voicemail_and_message_greeting_customization
        if enable is not None:
            self.enable = enable
        if reset is not None:
            self.reset = reset

    @property
    def allow_music_on_hold_customization(self):
        """Gets the allow_music_on_hold_customization of this PhoneusersuserIdPolicyPersonalAudioLibrary.  # noqa: E501

        Whether to allow the user to customize allow music on hold.  # noqa: E501

        :return: The allow_music_on_hold_customization of this PhoneusersuserIdPolicyPersonalAudioLibrary.  # noqa: E501
        :rtype: bool
        """
        return self._allow_music_on_hold_customization

    @allow_music_on_hold_customization.setter
    def allow_music_on_hold_customization(self, allow_music_on_hold_customization):
        """Sets the allow_music_on_hold_customization of this PhoneusersuserIdPolicyPersonalAudioLibrary.

        Whether to allow the user to customize allow music on hold.  # noqa: E501

        :param allow_music_on_hold_customization: The allow_music_on_hold_customization of this PhoneusersuserIdPolicyPersonalAudioLibrary.  # noqa: E501
        :type: bool
        """

        self._allow_music_on_hold_customization = allow_music_on_hold_customization

    @property
    def allow_voicemail_and_message_greeting_customization(self):
        """Gets the allow_voicemail_and_message_greeting_customization of this PhoneusersuserIdPolicyPersonalAudioLibrary.  # noqa: E501

        Whether to allow the user to customize voicemail and message greeting.  # noqa: E501

        :return: The allow_voicemail_and_message_greeting_customization of this PhoneusersuserIdPolicyPersonalAudioLibrary.  # noqa: E501
        :rtype: bool
        """
        return self._allow_voicemail_and_message_greeting_customization

    @allow_voicemail_and_message_greeting_customization.setter
    def allow_voicemail_and_message_greeting_customization(self, allow_voicemail_and_message_greeting_customization):
        """Sets the allow_voicemail_and_message_greeting_customization of this PhoneusersuserIdPolicyPersonalAudioLibrary.

        Whether to allow the user to customize voicemail and message greeting.  # noqa: E501

        :param allow_voicemail_and_message_greeting_customization: The allow_voicemail_and_message_greeting_customization of this PhoneusersuserIdPolicyPersonalAudioLibrary.  # noqa: E501
        :type: bool
        """

        self._allow_voicemail_and_message_greeting_customization = allow_voicemail_and_message_greeting_customization

    @property
    def enable(self):
        """Gets the enable of this PhoneusersuserIdPolicyPersonalAudioLibrary.  # noqa: E501

        Whether to allow users to change their own audio library.  # noqa: E501

        :return: The enable of this PhoneusersuserIdPolicyPersonalAudioLibrary.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this PhoneusersuserIdPolicyPersonalAudioLibrary.

        Whether to allow users to change their own audio library.  # noqa: E501

        :param enable: The enable of this PhoneusersuserIdPolicyPersonalAudioLibrary.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def reset(self):
        """Gets the reset of this PhoneusersuserIdPolicyPersonalAudioLibrary.  # noqa: E501

        Whether the user's personal audio library reset option will use the phone site's settings.  # noqa: E501

        :return: The reset of this PhoneusersuserIdPolicyPersonalAudioLibrary.  # noqa: E501
        :rtype: bool
        """
        return self._reset

    @reset.setter
    def reset(self, reset):
        """Sets the reset of this PhoneusersuserIdPolicyPersonalAudioLibrary.

        Whether the user's personal audio library reset option will use the phone site's settings.  # noqa: E501

        :param reset: The reset of this PhoneusersuserIdPolicyPersonalAudioLibrary.  # noqa: E501
        :type: bool
        """

        self._reset = reset

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
        if issubclass(PhoneusersuserIdPolicyPersonalAudioLibrary, dict):
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
        if not isinstance(other, PhoneusersuserIdPolicyPersonalAudioLibrary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
