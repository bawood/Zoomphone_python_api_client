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

class InlineResponse20037CallerQosSending(object):
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
        'date_time': 'datetime',
        'qos': 'InlineResponse20037CallerQosQos1'
    }

    attribute_map = {
        'date_time': 'date_time',
        'qos': 'qos'
    }

    def __init__(self, date_time=None, qos=None):  # noqa: E501
        """InlineResponse20037CallerQosSending - a model defined in Swagger"""  # noqa: E501
        self._date_time = None
        self._qos = None
        self.discriminator = None
        if date_time is not None:
            self.date_time = date_time
        if qos is not None:
            self.qos = qos

    @property
    def date_time(self):
        """Gets the date_time of this InlineResponse20037CallerQosSending.  # noqa: E501

        The date and time when the QoS was delivered.  # noqa: E501

        :return: The date_time of this InlineResponse20037CallerQosSending.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this InlineResponse20037CallerQosSending.

        The date and time when the QoS was delivered.  # noqa: E501

        :param date_time: The date_time of this InlineResponse20037CallerQosSending.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def qos(self):
        """Gets the qos of this InlineResponse20037CallerQosSending.  # noqa: E501


        :return: The qos of this InlineResponse20037CallerQosSending.  # noqa: E501
        :rtype: InlineResponse20037CallerQosQos1
        """
        return self._qos

    @qos.setter
    def qos(self, qos):
        """Sets the qos of this InlineResponse20037CallerQosSending.


        :param qos: The qos of this InlineResponse20037CallerQosSending.  # noqa: E501
        :type: InlineResponse20037CallerQosQos1
        """

        self._qos = qos

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
        if issubclass(InlineResponse20037CallerQosSending, dict):
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
        if not isinstance(other, InlineResponse20037CallerQosSending):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
