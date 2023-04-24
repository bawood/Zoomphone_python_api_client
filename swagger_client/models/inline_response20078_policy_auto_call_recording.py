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

class InlineResponse20078PolicyAutoCallRecording(object):
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
        'allow_stop_resume_recording': 'bool',
        'disconnect_on_recording_failure': 'bool',
        'enable': 'bool',
        'locked': 'bool',
        'locked_by': 'str',
        'recording_calls': 'str',
        'recording_explicit_consent': 'bool',
        'recording_start_prompt': 'bool',
        'recording_transcription': 'bool',
        'play_recording_beep_tone': 'InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone'
    }

    attribute_map = {
        'allow_stop_resume_recording': 'allow_stop_resume_recording',
        'disconnect_on_recording_failure': 'disconnect_on_recording_failure',
        'enable': 'enable',
        'locked': 'locked',
        'locked_by': 'locked_by',
        'recording_calls': 'recording_calls',
        'recording_explicit_consent': 'recording_explicit_consent',
        'recording_start_prompt': 'recording_start_prompt',
        'recording_transcription': 'recording_transcription',
        'play_recording_beep_tone': 'play_recording_beep_tone'
    }

    def __init__(self, allow_stop_resume_recording=None, disconnect_on_recording_failure=None, enable=None, locked=None, locked_by=None, recording_calls=None, recording_explicit_consent=None, recording_start_prompt=None, recording_transcription=None, play_recording_beep_tone=None):  # noqa: E501
        """InlineResponse20078PolicyAutoCallRecording - a model defined in Swagger"""  # noqa: E501
        self._allow_stop_resume_recording = None
        self._disconnect_on_recording_failure = None
        self._enable = None
        self._locked = None
        self._locked_by = None
        self._recording_calls = None
        self._recording_explicit_consent = None
        self._recording_start_prompt = None
        self._recording_transcription = None
        self._play_recording_beep_tone = None
        self.discriminator = None
        if allow_stop_resume_recording is not None:
            self.allow_stop_resume_recording = allow_stop_resume_recording
        if disconnect_on_recording_failure is not None:
            self.disconnect_on_recording_failure = disconnect_on_recording_failure
        if enable is not None:
            self.enable = enable
        if locked is not None:
            self.locked = locked
        if locked_by is not None:
            self.locked_by = locked_by
        if recording_calls is not None:
            self.recording_calls = recording_calls
        if recording_explicit_consent is not None:
            self.recording_explicit_consent = recording_explicit_consent
        if recording_start_prompt is not None:
            self.recording_start_prompt = recording_start_prompt
        if recording_transcription is not None:
            self.recording_transcription = recording_transcription
        if play_recording_beep_tone is not None:
            self.play_recording_beep_tone = play_recording_beep_tone

    @property
    def allow_stop_resume_recording(self):
        """Gets the allow_stop_resume_recording of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501

        Whether the stop of and resuming of automatic call recording is enabled.  # noqa: E501

        :return: The allow_stop_resume_recording of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :rtype: bool
        """
        return self._allow_stop_resume_recording

    @allow_stop_resume_recording.setter
    def allow_stop_resume_recording(self, allow_stop_resume_recording):
        """Sets the allow_stop_resume_recording of this InlineResponse20078PolicyAutoCallRecording.

        Whether the stop of and resuming of automatic call recording is enabled.  # noqa: E501

        :param allow_stop_resume_recording: The allow_stop_resume_recording of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :type: bool
        """

        self._allow_stop_resume_recording = allow_stop_resume_recording

    @property
    def disconnect_on_recording_failure(self):
        """Gets the disconnect_on_recording_failure of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501

        Whether a call disconnects when there is an issue with automatic call recording and the call cannot reconnect after five seconds. This does **not** include emergency calls.  # noqa: E501

        :return: The disconnect_on_recording_failure of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :rtype: bool
        """
        return self._disconnect_on_recording_failure

    @disconnect_on_recording_failure.setter
    def disconnect_on_recording_failure(self, disconnect_on_recording_failure):
        """Sets the disconnect_on_recording_failure of this InlineResponse20078PolicyAutoCallRecording.

        Whether a call disconnects when there is an issue with automatic call recording and the call cannot reconnect after five seconds. This does **not** include emergency calls.  # noqa: E501

        :param disconnect_on_recording_failure: The disconnect_on_recording_failure of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :type: bool
        """

        self._disconnect_on_recording_failure = disconnect_on_recording_failure

    @property
    def enable(self):
        """Gets the enable of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501

        Whether automatic call recording is enabled.  # noqa: E501

        :return: The enable of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this InlineResponse20078PolicyAutoCallRecording.

        Whether automatic call recording is enabled.  # noqa: E501

        :param enable: The enable of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def locked(self):
        """Gets the locked of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501

        Whether the senior administrator allow users to modify the current settings.  # noqa: E501

        :return: The locked of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this InlineResponse20078PolicyAutoCallRecording.

        Whether the senior administrator allow users to modify the current settings.  # noqa: E501

        :param locked: The locked of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def locked_by(self):
        """Gets the locked_by of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501

        This field specifies which level of administrator prohibits modifying the current settings.  # noqa: E501

        :return: The locked_by of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :rtype: str
        """
        return self._locked_by

    @locked_by.setter
    def locked_by(self, locked_by):
        """Sets the locked_by of this InlineResponse20078PolicyAutoCallRecording.

        This field specifies which level of administrator prohibits modifying the current settings.  # noqa: E501

        :param locked_by: The locked_by of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
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
    def recording_calls(self):
        """Gets the recording_calls of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501

        The type of calls automatically recorded:  * `inbound`  * `outbound`  * `both`  # noqa: E501

        :return: The recording_calls of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :rtype: str
        """
        return self._recording_calls

    @recording_calls.setter
    def recording_calls(self, recording_calls):
        """Sets the recording_calls of this InlineResponse20078PolicyAutoCallRecording.

        The type of calls automatically recorded:  * `inbound`  * `outbound`  * `both`  # noqa: E501

        :param recording_calls: The recording_calls of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
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
    def recording_explicit_consent(self):
        """Gets the recording_explicit_consent of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501

        Whether press 1 to provide recording consent is enabled.  # noqa: E501

        :return: The recording_explicit_consent of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :rtype: bool
        """
        return self._recording_explicit_consent

    @recording_explicit_consent.setter
    def recording_explicit_consent(self, recording_explicit_consent):
        """Sets the recording_explicit_consent of this InlineResponse20078PolicyAutoCallRecording.

        Whether press 1 to provide recording consent is enabled.  # noqa: E501

        :param recording_explicit_consent: The recording_explicit_consent of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :type: bool
        """

        self._recording_explicit_consent = recording_explicit_consent

    @property
    def recording_start_prompt(self):
        """Gets the recording_start_prompt of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501

        Whether a prompt plays to call participants when the recording has started.  # noqa: E501

        :return: The recording_start_prompt of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :rtype: bool
        """
        return self._recording_start_prompt

    @recording_start_prompt.setter
    def recording_start_prompt(self, recording_start_prompt):
        """Sets the recording_start_prompt of this InlineResponse20078PolicyAutoCallRecording.

        Whether a prompt plays to call participants when the recording has started.  # noqa: E501

        :param recording_start_prompt: The recording_start_prompt of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :type: bool
        """

        self._recording_start_prompt = recording_start_prompt

    @property
    def recording_transcription(self):
        """Gets the recording_transcription of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501

        Whether call recording transcription is enabled.  # noqa: E501

        :return: The recording_transcription of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :rtype: bool
        """
        return self._recording_transcription

    @recording_transcription.setter
    def recording_transcription(self, recording_transcription):
        """Sets the recording_transcription of this InlineResponse20078PolicyAutoCallRecording.

        Whether call recording transcription is enabled.  # noqa: E501

        :param recording_transcription: The recording_transcription of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :type: bool
        """

        self._recording_transcription = recording_transcription

    @property
    def play_recording_beep_tone(self):
        """Gets the play_recording_beep_tone of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501


        :return: The play_recording_beep_tone of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :rtype: InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone
        """
        return self._play_recording_beep_tone

    @play_recording_beep_tone.setter
    def play_recording_beep_tone(self, play_recording_beep_tone):
        """Sets the play_recording_beep_tone of this InlineResponse20078PolicyAutoCallRecording.


        :param play_recording_beep_tone: The play_recording_beep_tone of this InlineResponse20078PolicyAutoCallRecording.  # noqa: E501
        :type: InlineResponse20069PolicyAutoCallRecordingPlayRecordingBeepTone
        """

        self._play_recording_beep_tone = play_recording_beep_tone

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
        if issubclass(InlineResponse20078PolicyAutoCallRecording, dict):
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
        if not isinstance(other, InlineResponse20078PolicyAutoCallRecording):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other