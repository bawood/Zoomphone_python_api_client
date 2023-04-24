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

class InlineResponse20052OriginalBillingInfo(object):
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
        'account_number': 'str',
        'address': 'InlineResponse20052OriginalBillingInfoAddress',
        'authorizing_person': 'str',
        'billing_telephone_number': 'str',
        'company': 'str',
        'customer_requested_date': 'str',
        'pin': 'str'
    }

    attribute_map = {
        'account_number': 'account_number',
        'address': 'address',
        'authorizing_person': 'authorizing_person',
        'billing_telephone_number': 'billing_telephone_number',
        'company': 'company',
        'customer_requested_date': 'customer_requested_date',
        'pin': 'pin'
    }

    def __init__(self, account_number=None, address=None, authorizing_person=None, billing_telephone_number=None, company=None, customer_requested_date=None, pin=None):  # noqa: E501
        """InlineResponse20052OriginalBillingInfo - a model defined in Swagger"""  # noqa: E501
        self._account_number = None
        self._address = None
        self._authorizing_person = None
        self._billing_telephone_number = None
        self._company = None
        self._customer_requested_date = None
        self._pin = None
        self.discriminator = None
        if account_number is not None:
            self.account_number = account_number
        if address is not None:
            self.address = address
        if authorizing_person is not None:
            self.authorizing_person = authorizing_person
        if billing_telephone_number is not None:
            self.billing_telephone_number = billing_telephone_number
        if company is not None:
            self.company = company
        if customer_requested_date is not None:
            self.customer_requested_date = customer_requested_date
        if pin is not None:
            self.pin = pin

    @property
    def account_number(self):
        """Gets the account_number of this InlineResponse20052OriginalBillingInfo.  # noqa: E501


        :return: The account_number of this InlineResponse20052OriginalBillingInfo.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this InlineResponse20052OriginalBillingInfo.


        :param account_number: The account_number of this InlineResponse20052OriginalBillingInfo.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def address(self):
        """Gets the address of this InlineResponse20052OriginalBillingInfo.  # noqa: E501


        :return: The address of this InlineResponse20052OriginalBillingInfo.  # noqa: E501
        :rtype: InlineResponse20052OriginalBillingInfoAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this InlineResponse20052OriginalBillingInfo.


        :param address: The address of this InlineResponse20052OriginalBillingInfo.  # noqa: E501
        :type: InlineResponse20052OriginalBillingInfoAddress
        """

        self._address = address

    @property
    def authorizing_person(self):
        """Gets the authorizing_person of this InlineResponse20052OriginalBillingInfo.  # noqa: E501


        :return: The authorizing_person of this InlineResponse20052OriginalBillingInfo.  # noqa: E501
        :rtype: str
        """
        return self._authorizing_person

    @authorizing_person.setter
    def authorizing_person(self, authorizing_person):
        """Sets the authorizing_person of this InlineResponse20052OriginalBillingInfo.


        :param authorizing_person: The authorizing_person of this InlineResponse20052OriginalBillingInfo.  # noqa: E501
        :type: str
        """

        self._authorizing_person = authorizing_person

    @property
    def billing_telephone_number(self):
        """Gets the billing_telephone_number of this InlineResponse20052OriginalBillingInfo.  # noqa: E501


        :return: The billing_telephone_number of this InlineResponse20052OriginalBillingInfo.  # noqa: E501
        :rtype: str
        """
        return self._billing_telephone_number

    @billing_telephone_number.setter
    def billing_telephone_number(self, billing_telephone_number):
        """Sets the billing_telephone_number of this InlineResponse20052OriginalBillingInfo.


        :param billing_telephone_number: The billing_telephone_number of this InlineResponse20052OriginalBillingInfo.  # noqa: E501
        :type: str
        """

        self._billing_telephone_number = billing_telephone_number

    @property
    def company(self):
        """Gets the company of this InlineResponse20052OriginalBillingInfo.  # noqa: E501


        :return: The company of this InlineResponse20052OriginalBillingInfo.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this InlineResponse20052OriginalBillingInfo.


        :param company: The company of this InlineResponse20052OriginalBillingInfo.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def customer_requested_date(self):
        """Gets the customer_requested_date of this InlineResponse20052OriginalBillingInfo.  # noqa: E501


        :return: The customer_requested_date of this InlineResponse20052OriginalBillingInfo.  # noqa: E501
        :rtype: str
        """
        return self._customer_requested_date

    @customer_requested_date.setter
    def customer_requested_date(self, customer_requested_date):
        """Sets the customer_requested_date of this InlineResponse20052OriginalBillingInfo.


        :param customer_requested_date: The customer_requested_date of this InlineResponse20052OriginalBillingInfo.  # noqa: E501
        :type: str
        """

        self._customer_requested_date = customer_requested_date

    @property
    def pin(self):
        """Gets the pin of this InlineResponse20052OriginalBillingInfo.  # noqa: E501


        :return: The pin of this InlineResponse20052OriginalBillingInfo.  # noqa: E501
        :rtype: str
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        """Sets the pin of this InlineResponse20052OriginalBillingInfo.


        :param pin: The pin of this InlineResponse20052OriginalBillingInfo.  # noqa: E501
        :type: str
        """

        self._pin = pin

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
        if issubclass(InlineResponse20052OriginalBillingInfo, dict):
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
        if not isinstance(other, InlineResponse20052OriginalBillingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
