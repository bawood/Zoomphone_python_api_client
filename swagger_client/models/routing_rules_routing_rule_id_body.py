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

class RoutingRulesRoutingRuleIdBody(object):
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
        'number_pattern': 'str',
        'order': 'int',
        'sip_group_id': 'str',
        'translation': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'number_pattern': 'number_pattern',
        'order': 'order',
        'sip_group_id': 'sip_group_id',
        'translation': 'translation',
        'type': 'type'
    }

    def __init__(self, name=None, number_pattern=None, order=None, sip_group_id=None, translation=None, type=None):  # noqa: E501
        """RoutingRulesRoutingRuleIdBody - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._number_pattern = None
        self._order = None
        self._sip_group_id = None
        self._translation = None
        self._type = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if number_pattern is not None:
            self.number_pattern = number_pattern
        if order is not None:
            self.order = order
        if sip_group_id is not None:
            self.sip_group_id = sip_group_id
        if translation is not None:
            self.translation = translation
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this RoutingRulesRoutingRuleIdBody.  # noqa: E501

        Routing rule name.  # noqa: E501

        :return: The name of this RoutingRulesRoutingRuleIdBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoutingRulesRoutingRuleIdBody.

        Routing rule name.  # noqa: E501

        :param name: The name of this RoutingRulesRoutingRuleIdBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number_pattern(self):
        """Gets the number_pattern of this RoutingRulesRoutingRuleIdBody.  # noqa: E501

        Perl-compatible number_pattern expression.  # noqa: E501

        :return: The number_pattern of this RoutingRulesRoutingRuleIdBody.  # noqa: E501
        :rtype: str
        """
        return self._number_pattern

    @number_pattern.setter
    def number_pattern(self, number_pattern):
        """Sets the number_pattern of this RoutingRulesRoutingRuleIdBody.

        Perl-compatible number_pattern expression.  # noqa: E501

        :param number_pattern: The number_pattern of this RoutingRulesRoutingRuleIdBody.  # noqa: E501
        :type: str
        """

        self._number_pattern = number_pattern

    @property
    def order(self):
        """Gets the order of this RoutingRulesRoutingRuleIdBody.  # noqa: E501

        Routing rule order to be applied, '1' being the highest. Order inserting occurs when this field is filled. It will automatically readjust the order of rules between the target order and the current order.  # noqa: E501

        :return: The order of this RoutingRulesRoutingRuleIdBody.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this RoutingRulesRoutingRuleIdBody.

        Routing rule order to be applied, '1' being the highest. Order inserting occurs when this field is filled. It will automatically readjust the order of rules between the target order and the current order.  # noqa: E501

        :param order: The order of this RoutingRulesRoutingRuleIdBody.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def sip_group_id(self):
        """Gets the sip_group_id of this RoutingRulesRoutingRuleIdBody.  # noqa: E501

        Unique identifier of the SIP Group: must not be null when 'type' = 'sip_group'.  # noqa: E501

        :return: The sip_group_id of this RoutingRulesRoutingRuleIdBody.  # noqa: E501
        :rtype: str
        """
        return self._sip_group_id

    @sip_group_id.setter
    def sip_group_id(self, sip_group_id):
        """Sets the sip_group_id of this RoutingRulesRoutingRuleIdBody.

        Unique identifier of the SIP Group: must not be null when 'type' = 'sip_group'.  # noqa: E501

        :param sip_group_id: The sip_group_id of this RoutingRulesRoutingRuleIdBody.  # noqa: E501
        :type: str
        """

        self._sip_group_id = sip_group_id

    @property
    def translation(self):
        """Gets the translation of this RoutingRulesRoutingRuleIdBody.  # noqa: E501

        `nullable` Optional replacement pattern: must be in E.164 format.  # noqa: E501

        :return: The translation of this RoutingRulesRoutingRuleIdBody.  # noqa: E501
        :rtype: str
        """
        return self._translation

    @translation.setter
    def translation(self, translation):
        """Sets the translation of this RoutingRulesRoutingRuleIdBody.

        `nullable` Optional replacement pattern: must be in E.164 format.  # noqa: E501

        :param translation: The translation of this RoutingRulesRoutingRuleIdBody.  # noqa: E501
        :type: str
        """

        self._translation = translation

    @property
    def type(self):
        """Gets the type of this RoutingRulesRoutingRuleIdBody.  # noqa: E501

        Routing path type.  # noqa: E501

        :return: The type of this RoutingRulesRoutingRuleIdBody.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RoutingRulesRoutingRuleIdBody.

        Routing path type.  # noqa: E501

        :param type: The type of this RoutingRulesRoutingRuleIdBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["other_sites", "pstn", "sip_group"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(RoutingRulesRoutingRuleIdBody, dict):
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
        if not isinstance(other, RoutingRulesRoutingRuleIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
