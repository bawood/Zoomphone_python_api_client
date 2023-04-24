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

class InlineResponse20055CallingPlans(object):
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
        'name': 'str',
        'type': 'int',
        'billing_account_id': 'str',
        'billing_account_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'billing_account_id': 'billing_account_id',
        'billing_account_name': 'billing_account_name'
    }

    def __init__(self, name=None, type=None, billing_account_id=None, billing_account_name=None):  # noqa: E501
        """InlineResponse20055CallingPlans - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._billing_account_id = None
        self._billing_account_name = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if billing_account_id is not None:
            self.billing_account_id = billing_account_id
        if billing_account_name is not None:
            self.billing_account_name = billing_account_name

    @property
    def name(self):
        """Gets the name of this InlineResponse20055CallingPlans.  # noqa: E501

        Name of the calling plan that Zoom Room is enrolled in.  # noqa: E501

        :return: The name of this InlineResponse20055CallingPlans.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20055CallingPlans.

        Name of the calling plan that Zoom Room is enrolled in.  # noqa: E501

        :param name: The name of this InlineResponse20055CallingPlans.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this InlineResponse20055CallingPlans.  # noqa: E501

        Type of calling plan that Zoom Room is enrolled in.  # noqa: E501

        :return: The type of this InlineResponse20055CallingPlans.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20055CallingPlans.

        Type of calling plan that Zoom Room is enrolled in.  # noqa: E501

        :param type: The type of this InlineResponse20055CallingPlans.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def billing_account_id(self):
        """Gets the billing_account_id of this InlineResponse20055CallingPlans.  # noqa: E501

        Billing account ID. Displayed when the zoom room is located in India.  # noqa: E501

        :return: The billing_account_id of this InlineResponse20055CallingPlans.  # noqa: E501
        :rtype: str
        """
        return self._billing_account_id

    @billing_account_id.setter
    def billing_account_id(self, billing_account_id):
        """Sets the billing_account_id of this InlineResponse20055CallingPlans.

        Billing account ID. Displayed when the zoom room is located in India.  # noqa: E501

        :param billing_account_id: The billing_account_id of this InlineResponse20055CallingPlans.  # noqa: E501
        :type: str
        """

        self._billing_account_id = billing_account_id

    @property
    def billing_account_name(self):
        """Gets the billing_account_name of this InlineResponse20055CallingPlans.  # noqa: E501

        Billing account name. Displayed when the zoom room is located in India.  # noqa: E501

        :return: The billing_account_name of this InlineResponse20055CallingPlans.  # noqa: E501
        :rtype: str
        """
        return self._billing_account_name

    @billing_account_name.setter
    def billing_account_name(self, billing_account_name):
        """Sets the billing_account_name of this InlineResponse20055CallingPlans.

        Billing account name. Displayed when the zoom room is located in India.  # noqa: E501

        :param billing_account_name: The billing_account_name of this InlineResponse20055CallingPlans.  # noqa: E501
        :type: str
        """

        self._billing_account_name = billing_account_name

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
        if issubclass(InlineResponse20055CallingPlans, dict):
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
        if not isinstance(other, InlineResponse20055CallingPlans):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
