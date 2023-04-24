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

class InlineResponse20019CommonAreas(object):
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
        'calling_plans': 'list[InlineResponse20019CallingPlans]',
        'display_name': 'str',
        'id': 'str',
        'phone_numbers': 'list[InlineResponse20019PhoneNumbers]',
        'site': 'InlineResponse20019Site',
        'status': 'str',
        'desk_phones': 'list[InlineResponse20019DeskPhones]'
    }

    attribute_map = {
        'calling_plans': 'calling_plans',
        'display_name': 'display_name',
        'id': 'id',
        'phone_numbers': 'phone_numbers',
        'site': 'site',
        'status': 'status',
        'desk_phones': 'desk_phones'
    }

    def __init__(self, calling_plans=None, display_name=None, id=None, phone_numbers=None, site=None, status=None, desk_phones=None):  # noqa: E501
        """InlineResponse20019CommonAreas - a model defined in Swagger"""  # noqa: E501
        self._calling_plans = None
        self._display_name = None
        self._id = None
        self._phone_numbers = None
        self._site = None
        self._status = None
        self._desk_phones = None
        self.discriminator = None
        if calling_plans is not None:
            self.calling_plans = calling_plans
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if site is not None:
            self.site = site
        if status is not None:
            self.status = status
        if desk_phones is not None:
            self.desk_phones = desk_phones

    @property
    def calling_plans(self):
        """Gets the calling_plans of this InlineResponse20019CommonAreas.  # noqa: E501


        :return: The calling_plans of this InlineResponse20019CommonAreas.  # noqa: E501
        :rtype: list[InlineResponse20019CallingPlans]
        """
        return self._calling_plans

    @calling_plans.setter
    def calling_plans(self, calling_plans):
        """Sets the calling_plans of this InlineResponse20019CommonAreas.


        :param calling_plans: The calling_plans of this InlineResponse20019CommonAreas.  # noqa: E501
        :type: list[InlineResponse20019CallingPlans]
        """

        self._calling_plans = calling_plans

    @property
    def display_name(self):
        """Gets the display_name of this InlineResponse20019CommonAreas.  # noqa: E501

        The display name of the common area.  # noqa: E501

        :return: The display_name of this InlineResponse20019CommonAreas.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InlineResponse20019CommonAreas.

        The display name of the common area.  # noqa: E501

        :param display_name: The display_name of this InlineResponse20019CommonAreas.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this InlineResponse20019CommonAreas.  # noqa: E501

        The common area ID or common area extension ID.  # noqa: E501

        :return: The id of this InlineResponse20019CommonAreas.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20019CommonAreas.

        The common area ID or common area extension ID.  # noqa: E501

        :param id: The id of this InlineResponse20019CommonAreas.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this InlineResponse20019CommonAreas.  # noqa: E501


        :return: The phone_numbers of this InlineResponse20019CommonAreas.  # noqa: E501
        :rtype: list[InlineResponse20019PhoneNumbers]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this InlineResponse20019CommonAreas.


        :param phone_numbers: The phone_numbers of this InlineResponse20019CommonAreas.  # noqa: E501
        :type: list[InlineResponse20019PhoneNumbers]
        """

        self._phone_numbers = phone_numbers

    @property
    def site(self):
        """Gets the site of this InlineResponse20019CommonAreas.  # noqa: E501


        :return: The site of this InlineResponse20019CommonAreas.  # noqa: E501
        :rtype: InlineResponse20019Site
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this InlineResponse20019CommonAreas.


        :param site: The site of this InlineResponse20019CommonAreas.  # noqa: E501
        :type: InlineResponse20019Site
        """

        self._site = site

    @property
    def status(self):
        """Gets the status of this InlineResponse20019CommonAreas.  # noqa: E501

        The status of the common area.  # noqa: E501

        :return: The status of this InlineResponse20019CommonAreas.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20019CommonAreas.

        The status of the common area.  # noqa: E501

        :param status: The status of this InlineResponse20019CommonAreas.  # noqa: E501
        :type: str
        """
        allowed_values = ["online", "offline"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def desk_phones(self):
        """Gets the desk_phones of this InlineResponse20019CommonAreas.  # noqa: E501

        The common area's desk phones.  # noqa: E501

        :return: The desk_phones of this InlineResponse20019CommonAreas.  # noqa: E501
        :rtype: list[InlineResponse20019DeskPhones]
        """
        return self._desk_phones

    @desk_phones.setter
    def desk_phones(self, desk_phones):
        """Sets the desk_phones of this InlineResponse20019CommonAreas.

        The common area's desk phones.  # noqa: E501

        :param desk_phones: The desk_phones of this InlineResponse20019CommonAreas.  # noqa: E501
        :type: list[InlineResponse20019DeskPhones]
        """

        self._desk_phones = desk_phones

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
        if issubclass(InlineResponse20019CommonAreas, dict):
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
        if not isinstance(other, InlineResponse20019CommonAreas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
