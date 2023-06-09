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

class PhoneCommonAreasBody(object):
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
        'calling_plans': 'list[PhonecommonAreasCallingPlans]',
        'country_iso_code': 'str',
        'display_name': 'str',
        'extension_number': 'int',
        'site_id': 'str',
        'timezone': 'str'
    }

    attribute_map = {
        'calling_plans': 'calling_plans',
        'country_iso_code': 'country_iso_code',
        'display_name': 'display_name',
        'extension_number': 'extension_number',
        'site_id': 'site_id',
        'timezone': 'timezone'
    }

    def __init__(self, calling_plans=None, country_iso_code=None, display_name=None, extension_number=None, site_id=None, timezone=None):  # noqa: E501
        """PhoneCommonAreasBody - a model defined in Swagger"""  # noqa: E501
        self._calling_plans = None
        self._country_iso_code = None
        self._display_name = None
        self._extension_number = None
        self._site_id = None
        self._timezone = None
        self.discriminator = None
        if calling_plans is not None:
            self.calling_plans = calling_plans
        if country_iso_code is not None:
            self.country_iso_code = country_iso_code
        self.display_name = display_name
        if extension_number is not None:
            self.extension_number = extension_number
        if site_id is not None:
            self.site_id = site_id
        if timezone is not None:
            self.timezone = timezone

    @property
    def calling_plans(self):
        """Gets the calling_plans of this PhoneCommonAreasBody.  # noqa: E501


        :return: The calling_plans of this PhoneCommonAreasBody.  # noqa: E501
        :rtype: list[PhonecommonAreasCallingPlans]
        """
        return self._calling_plans

    @calling_plans.setter
    def calling_plans(self, calling_plans):
        """Sets the calling_plans of this PhoneCommonAreasBody.


        :param calling_plans: The calling_plans of this PhoneCommonAreasBody.  # noqa: E501
        :type: list[PhonecommonAreasCallingPlans]
        """

        self._calling_plans = calling_plans

    @property
    def country_iso_code(self):
        """Gets the country_iso_code of this PhoneCommonAreasBody.  # noqa: E501

        Two-lettered country [code](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries).  # noqa: E501

        :return: The country_iso_code of this PhoneCommonAreasBody.  # noqa: E501
        :rtype: str
        """
        return self._country_iso_code

    @country_iso_code.setter
    def country_iso_code(self, country_iso_code):
        """Sets the country_iso_code of this PhoneCommonAreasBody.

        Two-lettered country [code](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries).  # noqa: E501

        :param country_iso_code: The country_iso_code of this PhoneCommonAreasBody.  # noqa: E501
        :type: str
        """

        self._country_iso_code = country_iso_code

    @property
    def display_name(self):
        """Gets the display_name of this PhoneCommonAreasBody.  # noqa: E501

        Display name of the common area. Enter at least 3 characters.  # noqa: E501

        :return: The display_name of this PhoneCommonAreasBody.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PhoneCommonAreasBody.

        Display name of the common area. Enter at least 3 characters.  # noqa: E501

        :param display_name: The display_name of this PhoneCommonAreasBody.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def extension_number(self):
        """Gets the extension_number of this PhoneCommonAreasBody.  # noqa: E501

        Extension number assigned to the common area. If the site code is enabled, provide the short extension number instead.  # noqa: E501

        :return: The extension_number of this PhoneCommonAreasBody.  # noqa: E501
        :rtype: int
        """
        return self._extension_number

    @extension_number.setter
    def extension_number(self, extension_number):
        """Sets the extension_number of this PhoneCommonAreasBody.

        Extension number assigned to the common area. If the site code is enabled, provide the short extension number instead.  # noqa: E501

        :param extension_number: The extension_number of this PhoneCommonAreasBody.  # noqa: E501
        :type: int
        """

        self._extension_number = extension_number

    @property
    def site_id(self):
        """Gets the site_id of this PhoneCommonAreasBody.  # noqa: E501

        Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672). This can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API.  # noqa: E501

        :return: The site_id of this PhoneCommonAreasBody.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this PhoneCommonAreasBody.

        Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672). This can be retrieved from the [List Phone Sites](https://marketplace.zoom.us/docs/api-reference/phone/methods#operation/listPhoneSites) API.  # noqa: E501

        :param site_id: The site_id of this PhoneCommonAreasBody.  # noqa: E501
        :type: str
        """

        self._site_id = site_id

    @property
    def timezone(self):
        """Gets the timezone of this PhoneCommonAreasBody.  # noqa: E501

        [Timezone ID](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists) for the common area.  # noqa: E501

        :return: The timezone of this PhoneCommonAreasBody.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this PhoneCommonAreasBody.

        [Timezone ID](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists) for the common area.  # noqa: E501

        :param timezone: The timezone of this PhoneCommonAreasBody.  # noqa: E501
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
        if issubclass(PhoneCommonAreasBody, dict):
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
        if not isinstance(other, PhoneCommonAreasBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
