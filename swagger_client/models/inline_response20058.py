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

class InlineResponse20058(object):
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
        'routing_path': 'PhoneroutingRulesRoutingPath',
        'routing_rule_id': 'str',
        'site_id': 'str',
        'translation': 'str'
    }

    attribute_map = {
        'name': 'name',
        'number_pattern': 'number_pattern',
        'order': 'order',
        'routing_path': 'routing_path',
        'routing_rule_id': 'routing_rule_id',
        'site_id': 'site_id',
        'translation': 'translation'
    }

    def __init__(self, name=None, number_pattern=None, order=None, routing_path=None, routing_rule_id=None, site_id=None, translation=None):  # noqa: E501
        """InlineResponse20058 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._number_pattern = None
        self._order = None
        self._routing_path = None
        self._routing_rule_id = None
        self._site_id = None
        self._translation = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if number_pattern is not None:
            self.number_pattern = number_pattern
        if order is not None:
            self.order = order
        if routing_path is not None:
            self.routing_path = routing_path
        if routing_rule_id is not None:
            self.routing_rule_id = routing_rule_id
        if site_id is not None:
            self.site_id = site_id
        if translation is not None:
            self.translation = translation

    @property
    def name(self):
        """Gets the name of this InlineResponse20058.  # noqa: E501

        Routing rule name.  # noqa: E501

        :return: The name of this InlineResponse20058.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20058.

        Routing rule name.  # noqa: E501

        :param name: The name of this InlineResponse20058.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number_pattern(self):
        """Gets the number_pattern of this InlineResponse20058.  # noqa: E501

        Perl-compatible number_pattern expression.  # noqa: E501

        :return: The number_pattern of this InlineResponse20058.  # noqa: E501
        :rtype: str
        """
        return self._number_pattern

    @number_pattern.setter
    def number_pattern(self, number_pattern):
        """Sets the number_pattern of this InlineResponse20058.

        Perl-compatible number_pattern expression.  # noqa: E501

        :param number_pattern: The number_pattern of this InlineResponse20058.  # noqa: E501
        :type: str
        """

        self._number_pattern = number_pattern

    @property
    def order(self):
        """Gets the order of this InlineResponse20058.  # noqa: E501

        Rule order to be applied, '1' being the highest.  # noqa: E501

        :return: The order of this InlineResponse20058.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this InlineResponse20058.

        Rule order to be applied, '1' being the highest.  # noqa: E501

        :param order: The order of this InlineResponse20058.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def routing_path(self):
        """Gets the routing_path of this InlineResponse20058.  # noqa: E501


        :return: The routing_path of this InlineResponse20058.  # noqa: E501
        :rtype: PhoneroutingRulesRoutingPath
        """
        return self._routing_path

    @routing_path.setter
    def routing_path(self, routing_path):
        """Sets the routing_path of this InlineResponse20058.


        :param routing_path: The routing_path of this InlineResponse20058.  # noqa: E501
        :type: PhoneroutingRulesRoutingPath
        """

        self._routing_path = routing_path

    @property
    def routing_rule_id(self):
        """Gets the routing_rule_id of this InlineResponse20058.  # noqa: E501

        Unique identifier of the routing rule.  # noqa: E501

        :return: The routing_rule_id of this InlineResponse20058.  # noqa: E501
        :rtype: str
        """
        return self._routing_rule_id

    @routing_rule_id.setter
    def routing_rule_id(self, routing_rule_id):
        """Sets the routing_rule_id of this InlineResponse20058.

        Unique identifier of the routing rule.  # noqa: E501

        :param routing_rule_id: The routing_rule_id of this InlineResponse20058.  # noqa: E501
        :type: str
        """

        self._routing_rule_id = routing_rule_id

    @property
    def site_id(self):
        """Gets the site_id of this InlineResponse20058.  # noqa: E501

        Unique identifier of the site: nullable if the routing rule is at an account level.  # noqa: E501

        :return: The site_id of this InlineResponse20058.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this InlineResponse20058.

        Unique identifier of the site: nullable if the routing rule is at an account level.  # noqa: E501

        :param site_id: The site_id of this InlineResponse20058.  # noqa: E501
        :type: str
        """

        self._site_id = site_id

    @property
    def translation(self):
        """Gets the translation of this InlineResponse20058.  # noqa: E501

        Optional replacement pattern: must be in E.164 format.  # noqa: E501

        :return: The translation of this InlineResponse20058.  # noqa: E501
        :rtype: str
        """
        return self._translation

    @translation.setter
    def translation(self, translation):
        """Sets the translation of this InlineResponse20058.

        Optional replacement pattern: must be in E.164 format.  # noqa: E501

        :param translation: The translation of this InlineResponse20058.  # noqa: E501
        :type: str
        """

        self._translation = translation

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
        if issubclass(InlineResponse20058, dict):
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
        if not isinstance(other, InlineResponse20058):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other