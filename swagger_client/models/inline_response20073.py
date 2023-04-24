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

class InlineResponse20073(object):
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
        'next_page_token': 'str',
        'page_size': 'int',
        'sms_sessions': 'list[InlineResponse20073SmsSessions]'
    }

    attribute_map = {
        'next_page_token': 'next_page_token',
        'page_size': 'page_size',
        'sms_sessions': 'sms_sessions'
    }

    def __init__(self, next_page_token=None, page_size=None, sms_sessions=None):  # noqa: E501
        """InlineResponse20073 - a model defined in Swagger"""  # noqa: E501
        self._next_page_token = None
        self._page_size = None
        self._sms_sessions = None
        self.discriminator = None
        if next_page_token is not None:
            self.next_page_token = next_page_token
        if page_size is not None:
            self.page_size = page_size
        if sms_sessions is not None:
            self.sms_sessions = sms_sessions

    @property
    def next_page_token(self):
        """Gets the next_page_token of this InlineResponse20073.  # noqa: E501

        The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of the available result list exceeds the page size.  # noqa: E501

        :return: The next_page_token of this InlineResponse20073.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this InlineResponse20073.

        The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of the available result list exceeds the page size.  # noqa: E501

        :param next_page_token: The next_page_token of this InlineResponse20073.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    @property
    def page_size(self):
        """Gets the page_size of this InlineResponse20073.  # noqa: E501

        The size of each page.  # noqa: E501

        :return: The page_size of this InlineResponse20073.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this InlineResponse20073.

        The size of each page.  # noqa: E501

        :param page_size: The page_size of this InlineResponse20073.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def sms_sessions(self):
        """Gets the sms_sessions of this InlineResponse20073.  # noqa: E501


        :return: The sms_sessions of this InlineResponse20073.  # noqa: E501
        :rtype: list[InlineResponse20073SmsSessions]
        """
        return self._sms_sessions

    @sms_sessions.setter
    def sms_sessions(self, sms_sessions):
        """Sets the sms_sessions of this InlineResponse20073.


        :param sms_sessions: The sms_sessions of this InlineResponse20073.  # noqa: E501
        :type: list[InlineResponse20073SmsSessions]
        """

        self._sms_sessions = sms_sessions

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
        if issubclass(InlineResponse20073, dict):
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
        if not isinstance(other, InlineResponse20073):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
