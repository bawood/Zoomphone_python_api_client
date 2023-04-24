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

class InlineResponse20099Roles(object):
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
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'total_members': 'int',
        'is_default': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'total_members': 'total_members',
        'is_default': 'is_default'
    }

    def __init__(self, id=None, name=None, description=None, total_members=None, is_default=None):  # noqa: E501
        """InlineResponse20099Roles - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._total_members = None
        self._is_default = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if total_members is not None:
            self.total_members = total_members
        if is_default is not None:
            self.is_default = is_default

    @property
    def id(self):
        """Gets the id of this InlineResponse20099Roles.  # noqa: E501

        Unique identifier of the [role](https://support.zoom.us/hc/en-us/articles/360042099012-Using-Zoom-Phone-role-management) assigned to the user.  # noqa: E501

        :return: The id of this InlineResponse20099Roles.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20099Roles.

        Unique identifier of the [role](https://support.zoom.us/hc/en-us/articles/360042099012-Using-Zoom-Phone-role-management) assigned to the user.  # noqa: E501

        :param id: The id of this InlineResponse20099Roles.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20099Roles.  # noqa: E501

        User's [role](https://support.zoom.us/hc/en-us/articles/115001078646-Role-Based-Access-Control) name.  # noqa: E501

        :return: The name of this InlineResponse20099Roles.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20099Roles.

        User's [role](https://support.zoom.us/hc/en-us/articles/115001078646-Role-Based-Access-Control) name.  # noqa: E501

        :param name: The name of this InlineResponse20099Roles.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this InlineResponse20099Roles.  # noqa: E501

        Role description.  # noqa: E501

        :return: The description of this InlineResponse20099Roles.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse20099Roles.

        Role description.  # noqa: E501

        :param description: The description of this InlineResponse20099Roles.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def total_members(self):
        """Gets the total_members of this InlineResponse20099Roles.  # noqa: E501

        Total members assigned to the role.  # noqa: E501

        :return: The total_members of this InlineResponse20099Roles.  # noqa: E501
        :rtype: int
        """
        return self._total_members

    @total_members.setter
    def total_members(self, total_members):
        """Sets the total_members of this InlineResponse20099Roles.

        Total members assigned to the role.  # noqa: E501

        :param total_members: The total_members of this InlineResponse20099Roles.  # noqa: E501
        :type: int
        """

        self._total_members = total_members

    @property
    def is_default(self):
        """Gets the is_default of this InlineResponse20099Roles.  # noqa: E501

        Indicates whether the role is default or not.  # noqa: E501

        :return: The is_default of this InlineResponse20099Roles.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this InlineResponse20099Roles.

        Indicates whether the role is default or not.  # noqa: E501

        :param is_default: The is_default of this InlineResponse20099Roles.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

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
        if issubclass(InlineResponse20099Roles, dict):
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
        if not isinstance(other, InlineResponse20099Roles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other