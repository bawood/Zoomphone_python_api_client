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

class InlineResponse20077Users(object):
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
        'calling_plans': 'list[InlineResponse20077CallingPlans]',
        'email': 'str',
        'extension_id': 'str',
        'extension_number': 'int',
        'id': 'str',
        'name': 'str',
        'phone_user_id': 'str',
        'site': 'InlineResponse20077Site',
        'status': 'str',
        'phone_numbers': 'list[InlineResponse20077PhoneNumbers]',
        'department': 'str',
        'cost_center': 'str'
    }

    attribute_map = {
        'calling_plans': 'calling_plans',
        'email': 'email',
        'extension_id': 'extension_id',
        'extension_number': 'extension_number',
        'id': 'id',
        'name': 'name',
        'phone_user_id': 'phone_user_id',
        'site': 'site',
        'status': 'status',
        'phone_numbers': 'phone_numbers',
        'department': 'department',
        'cost_center': 'cost_center'
    }

    def __init__(self, calling_plans=None, email=None, extension_id=None, extension_number=None, id=None, name=None, phone_user_id=None, site=None, status=None, phone_numbers=None, department=None, cost_center=None):  # noqa: E501
        """InlineResponse20077Users - a model defined in Swagger"""  # noqa: E501
        self._calling_plans = None
        self._email = None
        self._extension_id = None
        self._extension_number = None
        self._id = None
        self._name = None
        self._phone_user_id = None
        self._site = None
        self._status = None
        self._phone_numbers = None
        self._department = None
        self._cost_center = None
        self.discriminator = None
        if calling_plans is not None:
            self.calling_plans = calling_plans
        if email is not None:
            self.email = email
        if extension_id is not None:
            self.extension_id = extension_id
        if extension_number is not None:
            self.extension_number = extension_number
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if phone_user_id is not None:
            self.phone_user_id = phone_user_id
        if site is not None:
            self.site = site
        if status is not None:
            self.status = status
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if department is not None:
            self.department = department
        if cost_center is not None:
            self.cost_center = cost_center

    @property
    def calling_plans(self):
        """Gets the calling_plans of this InlineResponse20077Users.  # noqa: E501


        :return: The calling_plans of this InlineResponse20077Users.  # noqa: E501
        :rtype: list[InlineResponse20077CallingPlans]
        """
        return self._calling_plans

    @calling_plans.setter
    def calling_plans(self, calling_plans):
        """Sets the calling_plans of this InlineResponse20077Users.


        :param calling_plans: The calling_plans of this InlineResponse20077Users.  # noqa: E501
        :type: list[InlineResponse20077CallingPlans]
        """

        self._calling_plans = calling_plans

    @property
    def email(self):
        """Gets the email of this InlineResponse20077Users.  # noqa: E501

        The email address of the user.  # noqa: E501

        :return: The email of this InlineResponse20077Users.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InlineResponse20077Users.

        The email address of the user.  # noqa: E501

        :param email: The email of this InlineResponse20077Users.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def extension_id(self):
        """Gets the extension_id of this InlineResponse20077Users.  # noqa: E501

        The extension ID.  # noqa: E501

        :return: The extension_id of this InlineResponse20077Users.  # noqa: E501
        :rtype: str
        """
        return self._extension_id

    @extension_id.setter
    def extension_id(self, extension_id):
        """Sets the extension_id of this InlineResponse20077Users.

        The extension ID.  # noqa: E501

        :param extension_id: The extension_id of this InlineResponse20077Users.  # noqa: E501
        :type: str
        """

        self._extension_id = extension_id

    @property
    def extension_number(self):
        """Gets the extension_number of this InlineResponse20077Users.  # noqa: E501

        The extension number assigned to the user's Zoom phone number.  # noqa: E501

        :return: The extension_number of this InlineResponse20077Users.  # noqa: E501
        :rtype: int
        """
        return self._extension_number

    @extension_number.setter
    def extension_number(self, extension_number):
        """Sets the extension_number of this InlineResponse20077Users.

        The extension number assigned to the user's Zoom phone number.  # noqa: E501

        :param extension_number: The extension_number of this InlineResponse20077Users.  # noqa: E501
        :type: int
        """

        self._extension_number = extension_number

    @property
    def id(self):
        """Gets the id of this InlineResponse20077Users.  # noqa: E501

        The unique identifier of the user (userId).  # noqa: E501

        :return: The id of this InlineResponse20077Users.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20077Users.

        The unique identifier of the user (userId).  # noqa: E501

        :param id: The id of this InlineResponse20077Users.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20077Users.  # noqa: E501

        The name of the user.  # noqa: E501

        :return: The name of this InlineResponse20077Users.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20077Users.

        The name of the user.  # noqa: E501

        :param name: The name of this InlineResponse20077Users.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone_user_id(self):
        """Gets the phone_user_id of this InlineResponse20077Users.  # noqa: E501

        The Zoom Phone Identifier of the user.  # noqa: E501

        :return: The phone_user_id of this InlineResponse20077Users.  # noqa: E501
        :rtype: str
        """
        return self._phone_user_id

    @phone_user_id.setter
    def phone_user_id(self, phone_user_id):
        """Sets the phone_user_id of this InlineResponse20077Users.

        The Zoom Phone Identifier of the user.  # noqa: E501

        :param phone_user_id: The phone_user_id of this InlineResponse20077Users.  # noqa: E501
        :type: str
        """

        self._phone_user_id = phone_user_id

    @property
    def site(self):
        """Gets the site of this InlineResponse20077Users.  # noqa: E501


        :return: The site of this InlineResponse20077Users.  # noqa: E501
        :rtype: InlineResponse20077Site
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this InlineResponse20077Users.


        :param site: The site of this InlineResponse20077Users.  # noqa: E501
        :type: InlineResponse20077Site
        """

        self._site = site

    @property
    def status(self):
        """Gets the status of this InlineResponse20077Users.  # noqa: E501

        This field displays the status of the user's Zoom Phone license. The value can be either of the following:  `activate`: Active Zoom phone user.  `deactivate`: User with Zoom phone license disabled. This type of user can't make or receive calls.  # noqa: E501

        :return: The status of this InlineResponse20077Users.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20077Users.

        This field displays the status of the user's Zoom Phone license. The value can be either of the following:  `activate`: Active Zoom phone user.  `deactivate`: User with Zoom phone license disabled. This type of user can't make or receive calls.  # noqa: E501

        :param status: The status of this InlineResponse20077Users.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this InlineResponse20077Users.  # noqa: E501


        :return: The phone_numbers of this InlineResponse20077Users.  # noqa: E501
        :rtype: list[InlineResponse20077PhoneNumbers]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this InlineResponse20077Users.


        :param phone_numbers: The phone_numbers of this InlineResponse20077Users.  # noqa: E501
        :type: list[InlineResponse20077PhoneNumbers]
        """

        self._phone_numbers = phone_numbers

    @property
    def department(self):
        """Gets the department of this InlineResponse20077Users.  # noqa: E501

        The department of which the user belongs.  # noqa: E501

        :return: The department of this InlineResponse20077Users.  # noqa: E501
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this InlineResponse20077Users.

        The department of which the user belongs.  # noqa: E501

        :param department: The department of this InlineResponse20077Users.  # noqa: E501
        :type: str
        """

        self._department = department

    @property
    def cost_center(self):
        """Gets the cost_center of this InlineResponse20077Users.  # noqa: E501

        The cost center of which the user belongs.  # noqa: E501

        :return: The cost_center of this InlineResponse20077Users.  # noqa: E501
        :rtype: str
        """
        return self._cost_center

    @cost_center.setter
    def cost_center(self, cost_center):
        """Sets the cost_center of this InlineResponse20077Users.

        The cost center of which the user belongs.  # noqa: E501

        :param cost_center: The cost_center of this InlineResponse20077Users.  # noqa: E501
        :type: str
        """

        self._cost_center = cost_center

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
        if issubclass(InlineResponse20077Users, dict):
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
        if not isinstance(other, InlineResponse20077Users):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
