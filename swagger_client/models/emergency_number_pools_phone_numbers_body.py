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

class EmergencyNumberPoolsPhoneNumbersBody(object):
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
        'phone_numbers': 'list[PhoneemergencyNumberPoolsphoneNumbersPhoneNumbers]',
        'site_id': 'str'
    }

    attribute_map = {
        'phone_numbers': 'phone_numbers',
        'site_id': 'site_id'
    }

    def __init__(self, phone_numbers=None, site_id=None):  # noqa: E501
        """EmergencyNumberPoolsPhoneNumbersBody - a model defined in Swagger"""  # noqa: E501
        self._phone_numbers = None
        self._site_id = None
        self.discriminator = None
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if site_id is not None:
            self.site_id = site_id

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this EmergencyNumberPoolsPhoneNumbersBody.  # noqa: E501


        :return: The phone_numbers of this EmergencyNumberPoolsPhoneNumbersBody.  # noqa: E501
        :rtype: list[PhoneemergencyNumberPoolsphoneNumbersPhoneNumbers]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this EmergencyNumberPoolsPhoneNumbersBody.


        :param phone_numbers: The phone_numbers of this EmergencyNumberPoolsPhoneNumbersBody.  # noqa: E501
        :type: list[PhoneemergencyNumberPoolsphoneNumbersPhoneNumbers]
        """

        self._phone_numbers = phone_numbers

    @property
    def site_id(self):
        """Gets the site_id of this EmergencyNumberPoolsPhoneNumbersBody.  # noqa: E501

        Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672). This can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. Required if multiple sites are enabled.  # noqa: E501

        :return: The site_id of this EmergencyNumberPoolsPhoneNumbersBody.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this EmergencyNumberPoolsPhoneNumbersBody.

        Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672). This can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API. Required if multiple sites are enabled.  # noqa: E501

        :param site_id: The site_id of this EmergencyNumberPoolsPhoneNumbersBody.  # noqa: E501
        :type: str
        """

        self._site_id = site_id

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
        if issubclass(EmergencyNumberPoolsPhoneNumbersBody, dict):
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
        if not isinstance(other, EmergencyNumberPoolsPhoneNumbersBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
