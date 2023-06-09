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

class InlineResponse20017CommonAreaPhones(object):
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
        'calling_plans': 'list[InlineResponse20017CallingPlans]',
        'device_type': 'str',
        'display_name': 'str',
        'id': 'str',
        'mac_address': 'str',
        'phone_numbers': 'list[InlineResponse20017PhoneNumbers]',
        'site': 'InlineResponse20017Site',
        'status': 'str'
    }

    attribute_map = {
        'calling_plans': 'calling_plans',
        'device_type': 'device_type',
        'display_name': 'display_name',
        'id': 'id',
        'mac_address': 'mac_address',
        'phone_numbers': 'phone_numbers',
        'site': 'site',
        'status': 'status'
    }

    def __init__(self, calling_plans=None, device_type=None, display_name=None, id=None, mac_address=None, phone_numbers=None, site=None, status=None):  # noqa: E501
        """InlineResponse20017CommonAreaPhones - a model defined in Swagger"""  # noqa: E501
        self._calling_plans = None
        self._device_type = None
        self._display_name = None
        self._id = None
        self._mac_address = None
        self._phone_numbers = None
        self._site = None
        self._status = None
        self.discriminator = None
        if calling_plans is not None:
            self.calling_plans = calling_plans
        if device_type is not None:
            self.device_type = device_type
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if mac_address is not None:
            self.mac_address = mac_address
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if site is not None:
            self.site = site
        if status is not None:
            self.status = status

    @property
    def calling_plans(self):
        """Gets the calling_plans of this InlineResponse20017CommonAreaPhones.  # noqa: E501


        :return: The calling_plans of this InlineResponse20017CommonAreaPhones.  # noqa: E501
        :rtype: list[InlineResponse20017CallingPlans]
        """
        return self._calling_plans

    @calling_plans.setter
    def calling_plans(self, calling_plans):
        """Sets the calling_plans of this InlineResponse20017CommonAreaPhones.


        :param calling_plans: The calling_plans of this InlineResponse20017CommonAreaPhones.  # noqa: E501
        :type: list[InlineResponse20017CallingPlans]
        """

        self._calling_plans = calling_plans

    @property
    def device_type(self):
        """Gets the device_type of this InlineResponse20017CommonAreaPhones.  # noqa: E501

        Type of device (manufacturer name + model name). Refer to the table here for a list of [supported devices](https://marketplace.zoom.us/docs/api-reference/other-references/zoomphone-supporteddevice).  # noqa: E501

        :return: The device_type of this InlineResponse20017CommonAreaPhones.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this InlineResponse20017CommonAreaPhones.

        Type of device (manufacturer name + model name). Refer to the table here for a list of [supported devices](https://marketplace.zoom.us/docs/api-reference/other-references/zoomphone-supporteddevice).  # noqa: E501

        :param device_type: The device_type of this InlineResponse20017CommonAreaPhones.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def display_name(self):
        """Gets the display_name of this InlineResponse20017CommonAreaPhones.  # noqa: E501

        Display name of the common area phone.  # noqa: E501

        :return: The display_name of this InlineResponse20017CommonAreaPhones.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InlineResponse20017CommonAreaPhones.

        Display name of the common area phone.  # noqa: E501

        :param display_name: The display_name of this InlineResponse20017CommonAreaPhones.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this InlineResponse20017CommonAreaPhones.  # noqa: E501

        Unique identifier of the common area phone.  # noqa: E501

        :return: The id of this InlineResponse20017CommonAreaPhones.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20017CommonAreaPhones.

        Unique identifier of the common area phone.  # noqa: E501

        :param id: The id of this InlineResponse20017CommonAreaPhones.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def mac_address(self):
        """Gets the mac_address of this InlineResponse20017CommonAreaPhones.  # noqa: E501

         Mac address or serial number.  # noqa: E501

        :return: The mac_address of this InlineResponse20017CommonAreaPhones.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this InlineResponse20017CommonAreaPhones.

         Mac address or serial number.  # noqa: E501

        :param mac_address: The mac_address of this InlineResponse20017CommonAreaPhones.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this InlineResponse20017CommonAreaPhones.  # noqa: E501


        :return: The phone_numbers of this InlineResponse20017CommonAreaPhones.  # noqa: E501
        :rtype: list[InlineResponse20017PhoneNumbers]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this InlineResponse20017CommonAreaPhones.


        :param phone_numbers: The phone_numbers of this InlineResponse20017CommonAreaPhones.  # noqa: E501
        :type: list[InlineResponse20017PhoneNumbers]
        """

        self._phone_numbers = phone_numbers

    @property
    def site(self):
        """Gets the site of this InlineResponse20017CommonAreaPhones.  # noqa: E501


        :return: The site of this InlineResponse20017CommonAreaPhones.  # noqa: E501
        :rtype: InlineResponse20017Site
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this InlineResponse20017CommonAreaPhones.


        :param site: The site of this InlineResponse20017CommonAreaPhones.  # noqa: E501
        :type: InlineResponse20017Site
        """

        self._site = site

    @property
    def status(self):
        """Gets the status of this InlineResponse20017CommonAreaPhones.  # noqa: E501

        Status of the common area phone. It can be either `online` or `offline`.  # noqa: E501

        :return: The status of this InlineResponse20017CommonAreaPhones.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20017CommonAreaPhones.

        Status of the common area phone. It can be either `online` or `offline`.  # noqa: E501

        :param status: The status of this InlineResponse20017CommonAreaPhones.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(InlineResponse20017CommonAreaPhones, dict):
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
        if not isinstance(other, InlineResponse20017CommonAreaPhones):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
