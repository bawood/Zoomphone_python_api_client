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

class InlineResponse20061Policy(object):
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
        'ad_hoc_call_recording': 'InlineResponse20061PolicyAdHocCallRecording',
        'auto_call_recording': 'InlineResponse20061PolicyAutoCallRecording',
        'sms': 'InlineResponse20061PolicySms',
        'voicemail': 'InlineResponse20061PolicyVoicemail',
        'call_forwarding': 'PhonesettingTemplatestemplateIdPolicyCallForwarding',
        'call_overflow': 'PhonesettingTemplatestemplateIdPolicyCallOverflow'
    }

    attribute_map = {
        'ad_hoc_call_recording': 'ad_hoc_call_recording',
        'auto_call_recording': 'auto_call_recording',
        'sms': 'sms',
        'voicemail': 'voicemail',
        'call_forwarding': 'call_forwarding',
        'call_overflow': 'call_overflow'
    }

    def __init__(self, ad_hoc_call_recording=None, auto_call_recording=None, sms=None, voicemail=None, call_forwarding=None, call_overflow=None):  # noqa: E501
        """InlineResponse20061Policy - a model defined in Swagger"""  # noqa: E501
        self._ad_hoc_call_recording = None
        self._auto_call_recording = None
        self._sms = None
        self._voicemail = None
        self._call_forwarding = None
        self._call_overflow = None
        self.discriminator = None
        if ad_hoc_call_recording is not None:
            self.ad_hoc_call_recording = ad_hoc_call_recording
        if auto_call_recording is not None:
            self.auto_call_recording = auto_call_recording
        if sms is not None:
            self.sms = sms
        if voicemail is not None:
            self.voicemail = voicemail
        if call_forwarding is not None:
            self.call_forwarding = call_forwarding
        if call_overflow is not None:
            self.call_overflow = call_overflow

    @property
    def ad_hoc_call_recording(self):
        """Gets the ad_hoc_call_recording of this InlineResponse20061Policy.  # noqa: E501


        :return: The ad_hoc_call_recording of this InlineResponse20061Policy.  # noqa: E501
        :rtype: InlineResponse20061PolicyAdHocCallRecording
        """
        return self._ad_hoc_call_recording

    @ad_hoc_call_recording.setter
    def ad_hoc_call_recording(self, ad_hoc_call_recording):
        """Sets the ad_hoc_call_recording of this InlineResponse20061Policy.


        :param ad_hoc_call_recording: The ad_hoc_call_recording of this InlineResponse20061Policy.  # noqa: E501
        :type: InlineResponse20061PolicyAdHocCallRecording
        """

        self._ad_hoc_call_recording = ad_hoc_call_recording

    @property
    def auto_call_recording(self):
        """Gets the auto_call_recording of this InlineResponse20061Policy.  # noqa: E501


        :return: The auto_call_recording of this InlineResponse20061Policy.  # noqa: E501
        :rtype: InlineResponse20061PolicyAutoCallRecording
        """
        return self._auto_call_recording

    @auto_call_recording.setter
    def auto_call_recording(self, auto_call_recording):
        """Sets the auto_call_recording of this InlineResponse20061Policy.


        :param auto_call_recording: The auto_call_recording of this InlineResponse20061Policy.  # noqa: E501
        :type: InlineResponse20061PolicyAutoCallRecording
        """

        self._auto_call_recording = auto_call_recording

    @property
    def sms(self):
        """Gets the sms of this InlineResponse20061Policy.  # noqa: E501


        :return: The sms of this InlineResponse20061Policy.  # noqa: E501
        :rtype: InlineResponse20061PolicySms
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this InlineResponse20061Policy.


        :param sms: The sms of this InlineResponse20061Policy.  # noqa: E501
        :type: InlineResponse20061PolicySms
        """

        self._sms = sms

    @property
    def voicemail(self):
        """Gets the voicemail of this InlineResponse20061Policy.  # noqa: E501


        :return: The voicemail of this InlineResponse20061Policy.  # noqa: E501
        :rtype: InlineResponse20061PolicyVoicemail
        """
        return self._voicemail

    @voicemail.setter
    def voicemail(self, voicemail):
        """Sets the voicemail of this InlineResponse20061Policy.


        :param voicemail: The voicemail of this InlineResponse20061Policy.  # noqa: E501
        :type: InlineResponse20061PolicyVoicemail
        """

        self._voicemail = voicemail

    @property
    def call_forwarding(self):
        """Gets the call_forwarding of this InlineResponse20061Policy.  # noqa: E501


        :return: The call_forwarding of this InlineResponse20061Policy.  # noqa: E501
        :rtype: PhonesettingTemplatestemplateIdPolicyCallForwarding
        """
        return self._call_forwarding

    @call_forwarding.setter
    def call_forwarding(self, call_forwarding):
        """Sets the call_forwarding of this InlineResponse20061Policy.


        :param call_forwarding: The call_forwarding of this InlineResponse20061Policy.  # noqa: E501
        :type: PhonesettingTemplatestemplateIdPolicyCallForwarding
        """

        self._call_forwarding = call_forwarding

    @property
    def call_overflow(self):
        """Gets the call_overflow of this InlineResponse20061Policy.  # noqa: E501


        :return: The call_overflow of this InlineResponse20061Policy.  # noqa: E501
        :rtype: PhonesettingTemplatestemplateIdPolicyCallOverflow
        """
        return self._call_overflow

    @call_overflow.setter
    def call_overflow(self, call_overflow):
        """Sets the call_overflow of this InlineResponse20061Policy.


        :param call_overflow: The call_overflow of this InlineResponse20061Policy.  # noqa: E501
        :type: PhonesettingTemplatestemplateIdPolicyCallOverflow
        """

        self._call_overflow = call_overflow

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
        if issubclass(InlineResponse20061Policy, dict):
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
        if not isinstance(other, InlineResponse20061Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
