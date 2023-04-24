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

class PhonesettingTemplatestemplateIdPolicyAutoCallRecording(object):
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
        'recording_calls': 'str',
        'recording_start_prompt': 'bool',
        'recording_transcription': 'bool'
    }

    attribute_map = {
        'enable': 'enable',
        'recording_calls': 'recording_calls',
        'recording_start_prompt': 'recording_start_prompt',
        'recording_transcription': 'recording_transcription'
    }

    def __init__(self, enable=None, recording_calls=None, recording_start_prompt=None, recording_transcription=None):  # noqa: E501
        """PhonesettingTemplatestemplateIdPolicyAutoCallRecording - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._recording_calls = None
        self._recording_start_prompt = None
        self._recording_transcription = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if recording_calls is not None:
            self.recording_calls = recording_calls
        if recording_start_prompt is not None:
            self.recording_start_prompt = recording_start_prompt
        if recording_transcription is not None:
            self.recording_transcription = recording_transcription

    @property
    def enable(self):
        """Gets the enable of this PhonesettingTemplatestemplateIdPolicyAutoCallRecording.  # noqa: E501

        The automatic call recording.  # noqa: E501

        :return: The enable of this PhonesettingTemplatestemplateIdPolicyAutoCallRecording.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this PhonesettingTemplatestemplateIdPolicyAutoCallRecording.

        The automatic call recording.  # noqa: E501

        :param enable: The enable of this PhonesettingTemplatestemplateIdPolicyAutoCallRecording.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def recording_calls(self):
        """Gets the recording_calls of this PhonesettingTemplatestemplateIdPolicyAutoCallRecording.  # noqa: E501

        Values: inbound, outbound, both.  # noqa: E501

        :return: The recording_calls of this PhonesettingTemplatestemplateIdPolicyAutoCallRecording.  # noqa: E501
        :rtype: str
        """
        return self._recording_calls

    @recording_calls.setter
    def recording_calls(self, recording_calls):
        """Sets the recording_calls of this PhonesettingTemplatestemplateIdPolicyAutoCallRecording.

        Values: inbound, outbound, both.  # noqa: E501

        :param recording_calls: The recording_calls of this PhonesettingTemplatestemplateIdPolicyAutoCallRecording.  # noqa: E501
        :type: str
        """
        allowed_values = ["inbound", "outbound", "both"]  # noqa: E501
        if recording_calls not in allowed_values:
            raise ValueError(
                "Invalid value for `recording_calls` ({0}), must be one of {1}"  # noqa: E501
                .format(recording_calls, allowed_values)
            )

        self._recording_calls = recording_calls

    @property
    def recording_start_prompt(self):
        """Gets the recording_start_prompt of this PhonesettingTemplatestemplateIdPolicyAutoCallRecording.  # noqa: E501

        Whether to play a prompt to call participants when the recording has started.  # noqa: E501

        :return: The recording_start_prompt of this PhonesettingTemplatestemplateIdPolicyAutoCallRecording.  # noqa: E501
        :rtype: bool
        """
        return self._recording_start_prompt

    @recording_start_prompt.setter
    def recording_start_prompt(self, recording_start_prompt):
        """Sets the recording_start_prompt of this PhonesettingTemplatestemplateIdPolicyAutoCallRecording.

        Whether to play a prompt to call participants when the recording has started.  # noqa: E501

        :param recording_start_prompt: The recording_start_prompt of this PhonesettingTemplatestemplateIdPolicyAutoCallRecording.  # noqa: E501
        :type: bool
        """

        self._recording_start_prompt = recording_start_prompt

    @property
    def recording_transcription(self):
        """Gets the recording_transcription of this PhonesettingTemplatestemplateIdPolicyAutoCallRecording.  # noqa: E501

        Whether to allow call recording transcription.  # noqa: E501

        :return: The recording_transcription of this PhonesettingTemplatestemplateIdPolicyAutoCallRecording.  # noqa: E501
        :rtype: bool
        """
        return self._recording_transcription

    @recording_transcription.setter
    def recording_transcription(self, recording_transcription):
        """Sets the recording_transcription of this PhonesettingTemplatestemplateIdPolicyAutoCallRecording.

        Whether to allow call recording transcription.  # noqa: E501

        :param recording_transcription: The recording_transcription of this PhonesettingTemplatestemplateIdPolicyAutoCallRecording.  # noqa: E501
        :type: bool
        """

        self._recording_transcription = recording_transcription

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
        if issubclass(PhonesettingTemplatestemplateIdPolicyAutoCallRecording, dict):
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
        if not isinstance(other, PhonesettingTemplatestemplateIdPolicyAutoCallRecording):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
