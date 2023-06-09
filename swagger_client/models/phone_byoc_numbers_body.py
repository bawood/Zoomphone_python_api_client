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

class PhoneByocNumbersBody(object):
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
        'carrier': 'str',
        'phone_numbers': 'list[str]',
        'sip_group_id': 'str',
        'site_id': 'str'
    }

    attribute_map = {
        'carrier': 'carrier',
        'phone_numbers': 'phone_numbers',
        'sip_group_id': 'sip_group_id',
        'site_id': 'site_id'
    }

    def __init__(self, carrier=None, phone_numbers=None, sip_group_id=None, site_id=None):  # noqa: E501
        """PhoneByocNumbersBody - a model defined in Swagger"""  # noqa: E501
        self._carrier = None
        self._phone_numbers = None
        self._sip_group_id = None
        self._site_id = None
        self.discriminator = None
        self.carrier = carrier
        self.phone_numbers = phone_numbers
        if sip_group_id is not None:
            self.sip_group_id = sip_group_id
        if site_id is not None:
            self.site_id = site_id

    @property
    def carrier(self):
        """Gets the carrier of this PhoneByocNumbersBody.  # noqa: E501

        Name of the carrier.  # noqa: E501

        :return: The carrier of this PhoneByocNumbersBody.  # noqa: E501
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this PhoneByocNumbersBody.

        Name of the carrier.  # noqa: E501

        :param carrier: The carrier of this PhoneByocNumbersBody.  # noqa: E501
        :type: str
        """
        if carrier is None:
            raise ValueError("Invalid value for `carrier`, must not be `None`")  # noqa: E501

        self._carrier = carrier

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this PhoneByocNumbersBody.  # noqa: E501

        Phone number(s) to be added to Zoom. The value should be in e164 format.  # noqa: E501

        :return: The phone_numbers of this PhoneByocNumbersBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this PhoneByocNumbersBody.

        Phone number(s) to be added to Zoom. The value should be in e164 format.  # noqa: E501

        :param phone_numbers: The phone_numbers of this PhoneByocNumbersBody.  # noqa: E501
        :type: list[str]
        """
        if phone_numbers is None:
            raise ValueError("Invalid value for `phone_numbers`, must not be `None`")  # noqa: E501

        self._phone_numbers = phone_numbers

    @property
    def sip_group_id(self):
        """Gets the sip_group_id of this PhoneByocNumbersBody.  # noqa: E501

        Sip group id.  # noqa: E501

        :return: The sip_group_id of this PhoneByocNumbersBody.  # noqa: E501
        :rtype: str
        """
        return self._sip_group_id

    @sip_group_id.setter
    def sip_group_id(self, sip_group_id):
        """Sets the sip_group_id of this PhoneByocNumbersBody.

        Sip group id.  # noqa: E501

        :param sip_group_id: The sip_group_id of this PhoneByocNumbersBody.  # noqa: E501
        :type: str
        """

        self._sip_group_id = sip_group_id

    @property
    def site_id(self):
        """Gets the site_id of this PhoneByocNumbersBody.  # noqa: E501

        Unique identifier of the site. This field is only required if you have enabled multiple sites in the account. See [Managing multiple sites](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) or [Adding a site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15) for details.  # noqa: E501

        :return: The site_id of this PhoneByocNumbersBody.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this PhoneByocNumbersBody.

        Unique identifier of the site. This field is only required if you have enabled multiple sites in the account. See [Managing multiple sites](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites) or [Adding a site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-multiple-sites#h_05c88e35-1593-491f-b1a8-b7139a75dc15) for details.  # noqa: E501

        :param site_id: The site_id of this PhoneByocNumbersBody.  # noqa: E501
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
        if issubclass(PhoneByocNumbersBody, dict):
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
        if not isinstance(other, PhoneByocNumbersBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
