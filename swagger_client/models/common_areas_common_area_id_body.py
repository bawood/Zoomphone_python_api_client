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

class CommonAreasCommonAreaIdBody(object):
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
        'area_code': 'str',
        'cost_center': 'str',
        'country_iso_code': 'str',
        'department': 'str',
        'display_name': 'str',
        'emergency_address_id': 'str',
        'extension_number': 'int',
        'outbound_caller_id': 'str',
        'policy': 'PhonecommonAreascommonAreaIdPolicy',
        'site_id': 'str',
        'timezone': 'str'
    }

    attribute_map = {
        'area_code': 'area_code',
        'cost_center': 'cost_center',
        'country_iso_code': 'country_iso_code',
        'department': 'department',
        'display_name': 'display_name',
        'emergency_address_id': 'emergency_address_id',
        'extension_number': 'extension_number',
        'outbound_caller_id': 'outbound_caller_id',
        'policy': 'policy',
        'site_id': 'site_id',
        'timezone': 'timezone'
    }

    def __init__(self, area_code=None, cost_center=None, country_iso_code=None, department=None, display_name=None, emergency_address_id=None, extension_number=None, outbound_caller_id=None, policy=None, site_id=None, timezone=None):  # noqa: E501
        """CommonAreasCommonAreaIdBody - a model defined in Swagger"""  # noqa: E501
        self._area_code = None
        self._cost_center = None
        self._country_iso_code = None
        self._department = None
        self._display_name = None
        self._emergency_address_id = None
        self._extension_number = None
        self._outbound_caller_id = None
        self._policy = None
        self._site_id = None
        self._timezone = None
        self.discriminator = None
        if area_code is not None:
            self.area_code = area_code
        if cost_center is not None:
            self.cost_center = cost_center
        if country_iso_code is not None:
            self.country_iso_code = country_iso_code
        if department is not None:
            self.department = department
        if display_name is not None:
            self.display_name = display_name
        if emergency_address_id is not None:
            self.emergency_address_id = emergency_address_id
        if extension_number is not None:
            self.extension_number = extension_number
        if outbound_caller_id is not None:
            self.outbound_caller_id = outbound_caller_id
        if policy is not None:
            self.policy = policy
        if site_id is not None:
            self.site_id = site_id
        if timezone is not None:
            self.timezone = timezone

    @property
    def area_code(self):
        """Gets the area_code of this CommonAreasCommonAreaIdBody.  # noqa: E501

        Area code of the common area.  # noqa: E501

        :return: The area_code of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :rtype: str
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this CommonAreasCommonAreaIdBody.

        Area code of the common area.  # noqa: E501

        :param area_code: The area_code of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :type: str
        """

        self._area_code = area_code

    @property
    def cost_center(self):
        """Gets the cost_center of this CommonAreasCommonAreaIdBody.  # noqa: E501

        The cost center the common area belongs to.  # noqa: E501

        :return: The cost_center of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :rtype: str
        """
        return self._cost_center

    @cost_center.setter
    def cost_center(self, cost_center):
        """Sets the cost_center of this CommonAreasCommonAreaIdBody.

        The cost center the common area belongs to.  # noqa: E501

        :param cost_center: The cost_center of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :type: str
        """

        self._cost_center = cost_center

    @property
    def country_iso_code(self):
        """Gets the country_iso_code of this CommonAreasCommonAreaIdBody.  # noqa: E501

        Two-lettered country [code](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries).  # noqa: E501

        :return: The country_iso_code of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :rtype: str
        """
        return self._country_iso_code

    @country_iso_code.setter
    def country_iso_code(self, country_iso_code):
        """Sets the country_iso_code of this CommonAreasCommonAreaIdBody.

        Two-lettered country [code](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries).  # noqa: E501

        :param country_iso_code: The country_iso_code of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :type: str
        """

        self._country_iso_code = country_iso_code

    @property
    def department(self):
        """Gets the department of this CommonAreasCommonAreaIdBody.  # noqa: E501

        The department the common area belongs to.  # noqa: E501

        :return: The department of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this CommonAreasCommonAreaIdBody.

        The department the common area belongs to.  # noqa: E501

        :param department: The department of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :type: str
        """

        self._department = department

    @property
    def display_name(self):
        """Gets the display_name of this CommonAreasCommonAreaIdBody.  # noqa: E501

        Display name of the common area.  # noqa: E501

        :return: The display_name of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CommonAreasCommonAreaIdBody.

        Display name of the common area.  # noqa: E501

        :param display_name: The display_name of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def emergency_address_id(self):
        """Gets the emergency_address_id of this CommonAreasCommonAreaIdBody.  # noqa: E501

        The emergency location's address ID.  # noqa: E501

        :return: The emergency_address_id of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :rtype: str
        """
        return self._emergency_address_id

    @emergency_address_id.setter
    def emergency_address_id(self, emergency_address_id):
        """Sets the emergency_address_id of this CommonAreasCommonAreaIdBody.

        The emergency location's address ID.  # noqa: E501

        :param emergency_address_id: The emergency_address_id of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :type: str
        """

        self._emergency_address_id = emergency_address_id

    @property
    def extension_number(self):
        """Gets the extension_number of this CommonAreasCommonAreaIdBody.  # noqa: E501

        Extension number of the phone. If the site code is enabled, provide the short extension number instead.  # noqa: E501

        :return: The extension_number of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :rtype: int
        """
        return self._extension_number

    @extension_number.setter
    def extension_number(self, extension_number):
        """Sets the extension_number of this CommonAreasCommonAreaIdBody.

        Extension number of the phone. If the site code is enabled, provide the short extension number instead.  # noqa: E501

        :param extension_number: The extension_number of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :type: int
        """

        self._extension_number = extension_number

    @property
    def outbound_caller_id(self):
        """Gets the outbound_caller_id of this CommonAreasCommonAreaIdBody.  # noqa: E501

        The user's outbound caller ID phone number in E164 format.  # noqa: E501

        :return: The outbound_caller_id of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :rtype: str
        """
        return self._outbound_caller_id

    @outbound_caller_id.setter
    def outbound_caller_id(self, outbound_caller_id):
        """Sets the outbound_caller_id of this CommonAreasCommonAreaIdBody.

        The user's outbound caller ID phone number in E164 format.  # noqa: E501

        :param outbound_caller_id: The outbound_caller_id of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :type: str
        """

        self._outbound_caller_id = outbound_caller_id

    @property
    def policy(self):
        """Gets the policy of this CommonAreasCommonAreaIdBody.  # noqa: E501


        :return: The policy of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :rtype: PhonecommonAreascommonAreaIdPolicy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this CommonAreasCommonAreaIdBody.


        :param policy: The policy of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :type: PhonecommonAreascommonAreaIdPolicy
        """

        self._policy = policy

    @property
    def site_id(self):
        """Gets the site_id of this CommonAreasCommonAreaIdBody.  # noqa: E501

        Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites) to which the common area desk phone is assigned.  # noqa: E501

        :return: The site_id of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this CommonAreasCommonAreaIdBody.

        Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites) to which the common area desk phone is assigned.  # noqa: E501

        :param site_id: The site_id of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :type: str
        """

        self._site_id = site_id

    @property
    def timezone(self):
        """Gets the timezone of this CommonAreasCommonAreaIdBody.  # noqa: E501

        [Timezone ID](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists) for the common area.  # noqa: E501

        :return: The timezone of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this CommonAreasCommonAreaIdBody.

        [Timezone ID](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists) for the common area.  # noqa: E501

        :param timezone: The timezone of this CommonAreasCommonAreaIdBody.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

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
        if issubclass(CommonAreasCommonAreaIdBody, dict):
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
        if not isinstance(other, CommonAreasCommonAreaIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
