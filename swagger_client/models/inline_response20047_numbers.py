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

class InlineResponse20047Numbers(object):
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
        'assigned': 'int',
        'billing_reference_id': 'str',
        'phone_number': 'str',
        'service_info': 'str',
        'sip_trunk_name': 'str',
        'status': 'int'
    }

    attribute_map = {
        'assigned': 'assigned',
        'billing_reference_id': 'billing_reference_id',
        'phone_number': 'phone_number',
        'service_info': 'service_info',
        'sip_trunk_name': 'sip_trunk_name',
        'status': 'status'
    }

    def __init__(self, assigned=None, billing_reference_id=None, phone_number=None, service_info=None, sip_trunk_name=None, status=None):  # noqa: E501
        """InlineResponse20047Numbers - a model defined in Swagger"""  # noqa: E501
        self._assigned = None
        self._billing_reference_id = None
        self._phone_number = None
        self._service_info = None
        self._sip_trunk_name = None
        self._status = None
        self.discriminator = None
        self.assigned = assigned
        if billing_reference_id is not None:
            self.billing_reference_id = billing_reference_id
        self.phone_number = phone_number
        if service_info is not None:
            self.service_info = service_info
        self.sip_trunk_name = sip_trunk_name
        self.status = status

    @property
    def assigned(self):
        """Gets the assigned of this InlineResponse20047Numbers.  # noqa: E501

        Whether the phone number is assigned: * `0` — Unassigned. * `1` — Assigned.  # noqa: E501

        :return: The assigned of this InlineResponse20047Numbers.  # noqa: E501
        :rtype: int
        """
        return self._assigned

    @assigned.setter
    def assigned(self, assigned):
        """Sets the assigned of this InlineResponse20047Numbers.

        Whether the phone number is assigned: * `0` — Unassigned. * `1` — Assigned.  # noqa: E501

        :param assigned: The assigned of this InlineResponse20047Numbers.  # noqa: E501
        :type: int
        """
        if assigned is None:
            raise ValueError("Invalid value for `assigned`, must not be `None`")  # noqa: E501

        self._assigned = assigned

    @property
    def billing_reference_id(self):
        """Gets the billing_reference_id of this InlineResponse20047Numbers.  # noqa: E501

        The carrier's billing reference ID.  # noqa: E501

        :return: The billing_reference_id of this InlineResponse20047Numbers.  # noqa: E501
        :rtype: str
        """
        return self._billing_reference_id

    @billing_reference_id.setter
    def billing_reference_id(self, billing_reference_id):
        """Sets the billing_reference_id of this InlineResponse20047Numbers.

        The carrier's billing reference ID.  # noqa: E501

        :param billing_reference_id: The billing_reference_id of this InlineResponse20047Numbers.  # noqa: E501
        :type: str
        """

        self._billing_reference_id = billing_reference_id

    @property
    def phone_number(self):
        """Gets the phone_number of this InlineResponse20047Numbers.  # noqa: E501

        The phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164).  # noqa: E501

        :return: The phone_number of this InlineResponse20047Numbers.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this InlineResponse20047Numbers.

        The phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164).  # noqa: E501

        :param phone_number: The phone_number of this InlineResponse20047Numbers.  # noqa: E501
        :type: str
        """
        if phone_number is None:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def service_info(self):
        """Gets the service_info of this InlineResponse20047Numbers.  # noqa: E501

        The carrier's service information.  # noqa: E501

        :return: The service_info of this InlineResponse20047Numbers.  # noqa: E501
        :rtype: str
        """
        return self._service_info

    @service_info.setter
    def service_info(self, service_info):
        """Sets the service_info of this InlineResponse20047Numbers.

        The carrier's service information.  # noqa: E501

        :param service_info: The service_info of this InlineResponse20047Numbers.  # noqa: E501
        :type: str
        """

        self._service_info = service_info

    @property
    def sip_trunk_name(self):
        """Gets the sip_trunk_name of this InlineResponse20047Numbers.  # noqa: E501

        The phone number's [SIP trunk](https://en.wikipedia.org/wiki/SIP_trunking).  # noqa: E501

        :return: The sip_trunk_name of this InlineResponse20047Numbers.  # noqa: E501
        :rtype: str
        """
        return self._sip_trunk_name

    @sip_trunk_name.setter
    def sip_trunk_name(self, sip_trunk_name):
        """Sets the sip_trunk_name of this InlineResponse20047Numbers.

        The phone number's [SIP trunk](https://en.wikipedia.org/wiki/SIP_trunking).  # noqa: E501

        :param sip_trunk_name: The sip_trunk_name of this InlineResponse20047Numbers.  # noqa: E501
        :type: str
        """
        if sip_trunk_name is None:
            raise ValueError("Invalid value for `sip_trunk_name`, must not be `None`")  # noqa: E501

        self._sip_trunk_name = sip_trunk_name

    @property
    def status(self):
        """Gets the status of this InlineResponse20047Numbers.  # noqa: E501

        The phone number's status: * `0` — Inactive. * `1` — Active.  # noqa: E501

        :return: The status of this InlineResponse20047Numbers.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20047Numbers.

        The phone number's status: * `0` — Inactive. * `1` — Active.  # noqa: E501

        :param status: The status of this InlineResponse20047Numbers.  # noqa: E501
        :type: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

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
        if issubclass(InlineResponse20047Numbers, dict):
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
        if not isinstance(other, InlineResponse20047Numbers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
