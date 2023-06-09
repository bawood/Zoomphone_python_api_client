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

class PhoneSitesBody(object):
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
        'auto_receptionist_name': 'str',
        'default_emergency_address': 'PhonesitesDefaultEmergencyAddress',
        'name': 'str',
        'short_extension': 'PhonesitesShortExtension',
        'site_code': 'int',
        'sip_zone': 'PhonesitesSipZone'
    }

    attribute_map = {
        'auto_receptionist_name': 'auto_receptionist_name',
        'default_emergency_address': 'default_emergency_address',
        'name': 'name',
        'short_extension': 'short_extension',
        'site_code': 'site_code',
        'sip_zone': 'sip_zone'
    }

    def __init__(self, auto_receptionist_name=None, default_emergency_address=None, name=None, short_extension=None, site_code=None, sip_zone=None):  # noqa: E501
        """PhoneSitesBody - a model defined in Swagger"""  # noqa: E501
        self._auto_receptionist_name = None
        self._default_emergency_address = None
        self._name = None
        self._short_extension = None
        self._site_code = None
        self._sip_zone = None
        self.discriminator = None
        self.auto_receptionist_name = auto_receptionist_name
        self.default_emergency_address = default_emergency_address
        self.name = name
        if short_extension is not None:
            self.short_extension = short_extension
        if site_code is not None:
            self.site_code = site_code
        if sip_zone is not None:
            self.sip_zone = sip_zone

    @property
    def auto_receptionist_name(self):
        """Gets the auto_receptionist_name of this PhoneSitesBody.  # noqa: E501

        The display name of the [auto-receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Integrated-Voice-Response-IVR-) for the site.  # noqa: E501

        :return: The auto_receptionist_name of this PhoneSitesBody.  # noqa: E501
        :rtype: str
        """
        return self._auto_receptionist_name

    @auto_receptionist_name.setter
    def auto_receptionist_name(self, auto_receptionist_name):
        """Sets the auto_receptionist_name of this PhoneSitesBody.

        The display name of the [auto-receptionist](https://support.zoom.us/hc/en-us/articles/360021121312-Managing-Auto-Receptionists-and-Integrated-Voice-Response-IVR-) for the site.  # noqa: E501

        :param auto_receptionist_name: The auto_receptionist_name of this PhoneSitesBody.  # noqa: E501
        :type: str
        """
        if auto_receptionist_name is None:
            raise ValueError("Invalid value for `auto_receptionist_name`, must not be `None`")  # noqa: E501

        self._auto_receptionist_name = auto_receptionist_name

    @property
    def default_emergency_address(self):
        """Gets the default_emergency_address of this PhoneSitesBody.  # noqa: E501


        :return: The default_emergency_address of this PhoneSitesBody.  # noqa: E501
        :rtype: PhonesitesDefaultEmergencyAddress
        """
        return self._default_emergency_address

    @default_emergency_address.setter
    def default_emergency_address(self, default_emergency_address):
        """Sets the default_emergency_address of this PhoneSitesBody.


        :param default_emergency_address: The default_emergency_address of this PhoneSitesBody.  # noqa: E501
        :type: PhonesitesDefaultEmergencyAddress
        """
        if default_emergency_address is None:
            raise ValueError("Invalid value for `default_emergency_address`, must not be `None`")  # noqa: E501

        self._default_emergency_address = default_emergency_address

    @property
    def name(self):
        """Gets the name of this PhoneSitesBody.  # noqa: E501

        The name of the site.  # noqa: E501

        :return: The name of this PhoneSitesBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PhoneSitesBody.

        The name of the site.  # noqa: E501

        :param name: The name of this PhoneSitesBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def short_extension(self):
        """Gets the short_extension of this PhoneSitesBody.  # noqa: E501


        :return: The short_extension of this PhoneSitesBody.  # noqa: E501
        :rtype: PhonesitesShortExtension
        """
        return self._short_extension

    @short_extension.setter
    def short_extension(self, short_extension):
        """Sets the short_extension of this PhoneSitesBody.


        :param short_extension: The short_extension of this PhoneSitesBody.  # noqa: E501
        :type: PhonesitesShortExtension
        """

        self._short_extension = short_extension

    @property
    def site_code(self):
        """Gets the site_code of this PhoneSitesBody.  # noqa: E501

        The identifier for a site. If the site code is enabled, this field is required.    # noqa: E501

        :return: The site_code of this PhoneSitesBody.  # noqa: E501
        :rtype: int
        """
        return self._site_code

    @site_code.setter
    def site_code(self, site_code):
        """Sets the site_code of this PhoneSitesBody.

        The identifier for a site. If the site code is enabled, this field is required.    # noqa: E501

        :param site_code: The site_code of this PhoneSitesBody.  # noqa: E501
        :type: int
        """

        self._site_code = site_code

    @property
    def sip_zone(self):
        """Gets the sip_zone of this PhoneSitesBody.  # noqa: E501


        :return: The sip_zone of this PhoneSitesBody.  # noqa: E501
        :rtype: PhonesitesSipZone
        """
        return self._sip_zone

    @sip_zone.setter
    def sip_zone(self, sip_zone):
        """Sets the sip_zone of this PhoneSitesBody.


        :param sip_zone: The sip_zone of this PhoneSitesBody.  # noqa: E501
        :type: PhonesitesSipZone
        """

        self._sip_zone = sip_zone

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
        if issubclass(PhoneSitesBody, dict):
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
        if not isinstance(other, PhoneSitesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
