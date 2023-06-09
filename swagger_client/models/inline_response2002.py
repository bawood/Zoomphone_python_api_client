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

class InlineResponse2002(object):
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
        'cost_center': 'str',
        'department': 'str',
        'extension_id': 'str',
        'extension_number': 'int',
        'name': 'str',
        'timezone': 'str',
        'audio_prompt_language': 'str',
        'holiday_hours': 'list[InlineResponse2001HolidayHours]',
        'phone_numbers': 'list[InlineResponse2001PhoneNumbers]',
        'site': 'InlineResponse2001Site'
    }

    attribute_map = {
        'cost_center': 'cost_center',
        'department': 'department',
        'extension_id': 'extension_id',
        'extension_number': 'extension_number',
        'name': 'name',
        'timezone': 'timezone',
        'audio_prompt_language': 'audio_prompt_language',
        'holiday_hours': 'holiday_hours',
        'phone_numbers': 'phone_numbers',
        'site': 'site'
    }

    def __init__(self, cost_center=None, department=None, extension_id=None, extension_number=None, name=None, timezone=None, audio_prompt_language=None, holiday_hours=None, phone_numbers=None, site=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger"""  # noqa: E501
        self._cost_center = None
        self._department = None
        self._extension_id = None
        self._extension_number = None
        self._name = None
        self._timezone = None
        self._audio_prompt_language = None
        self._holiday_hours = None
        self._phone_numbers = None
        self._site = None
        self.discriminator = None
        if cost_center is not None:
            self.cost_center = cost_center
        if department is not None:
            self.department = department
        if extension_id is not None:
            self.extension_id = extension_id
        if extension_number is not None:
            self.extension_number = extension_number
        if name is not None:
            self.name = name
        if timezone is not None:
            self.timezone = timezone
        if audio_prompt_language is not None:
            self.audio_prompt_language = audio_prompt_language
        if holiday_hours is not None:
            self.holiday_hours = holiday_hours
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if site is not None:
            self.site = site

    @property
    def cost_center(self):
        """Gets the cost_center of this InlineResponse2002.  # noqa: E501

        `nullable` Cost center name.  # noqa: E501

        :return: The cost_center of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._cost_center

    @cost_center.setter
    def cost_center(self, cost_center):
        """Sets the cost_center of this InlineResponse2002.

        `nullable` Cost center name.  # noqa: E501

        :param cost_center: The cost_center of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._cost_center = cost_center

    @property
    def department(self):
        """Gets the department of this InlineResponse2002.  # noqa: E501

        `nullable` Department name.  # noqa: E501

        :return: The department of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this InlineResponse2002.

        `nullable` Department name.  # noqa: E501

        :param department: The department of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._department = department

    @property
    def extension_id(self):
        """Gets the extension_id of this InlineResponse2002.  # noqa: E501

        Extension ID  # noqa: E501

        :return: The extension_id of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._extension_id

    @extension_id.setter
    def extension_id(self, extension_id):
        """Sets the extension_id of this InlineResponse2002.

        Extension ID  # noqa: E501

        :param extension_id: The extension_id of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._extension_id = extension_id

    @property
    def extension_number(self):
        """Gets the extension_number of this InlineResponse2002.  # noqa: E501

        Extension number of the auto receptionist.  # noqa: E501

        :return: The extension_number of this InlineResponse2002.  # noqa: E501
        :rtype: int
        """
        return self._extension_number

    @extension_number.setter
    def extension_number(self, extension_number):
        """Sets the extension_number of this InlineResponse2002.

        Extension number of the auto receptionist.  # noqa: E501

        :param extension_number: The extension_number of this InlineResponse2002.  # noqa: E501
        :type: int
        """

        self._extension_number = extension_number

    @property
    def name(self):
        """Gets the name of this InlineResponse2002.  # noqa: E501

        Name of the auto receptionist.  # noqa: E501

        :return: The name of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2002.

        Name of the auto receptionist.  # noqa: E501

        :param name: The name of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def timezone(self):
        """Gets the timezone of this InlineResponse2002.  # noqa: E501

        [Timezone](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#timezones) of the Auto Receptionist.  # noqa: E501

        :return: The timezone of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this InlineResponse2002.

        [Timezone](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#timezones) of the Auto Receptionist.  # noqa: E501

        :param timezone: The timezone of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def audio_prompt_language(self):
        """Gets the audio_prompt_language of this InlineResponse2002.  # noqa: E501

        Audio prompt language.  # noqa: E501

        :return: The audio_prompt_language of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._audio_prompt_language

    @audio_prompt_language.setter
    def audio_prompt_language(self, audio_prompt_language):
        """Sets the audio_prompt_language of this InlineResponse2002.

        Audio prompt language.  # noqa: E501

        :param audio_prompt_language: The audio_prompt_language of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._audio_prompt_language = audio_prompt_language

    @property
    def holiday_hours(self):
        """Gets the holiday_hours of this InlineResponse2002.  # noqa: E501

        The holiday hours.  # noqa: E501

        :return: The holiday_hours of this InlineResponse2002.  # noqa: E501
        :rtype: list[InlineResponse2001HolidayHours]
        """
        return self._holiday_hours

    @holiday_hours.setter
    def holiday_hours(self, holiday_hours):
        """Sets the holiday_hours of this InlineResponse2002.

        The holiday hours.  # noqa: E501

        :param holiday_hours: The holiday_hours of this InlineResponse2002.  # noqa: E501
        :type: list[InlineResponse2001HolidayHours]
        """

        self._holiday_hours = holiday_hours

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this InlineResponse2002.  # noqa: E501


        :return: The phone_numbers of this InlineResponse2002.  # noqa: E501
        :rtype: list[InlineResponse2001PhoneNumbers]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this InlineResponse2002.


        :param phone_numbers: The phone_numbers of this InlineResponse2002.  # noqa: E501
        :type: list[InlineResponse2001PhoneNumbers]
        """

        self._phone_numbers = phone_numbers

    @property
    def site(self):
        """Gets the site of this InlineResponse2002.  # noqa: E501


        :return: The site of this InlineResponse2002.  # noqa: E501
        :rtype: InlineResponse2001Site
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this InlineResponse2002.


        :param site: The site of this InlineResponse2002.  # noqa: E501
        :type: InlineResponse2001Site
        """

        self._site = site

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
        if issubclass(InlineResponse2002, dict):
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
        if not isinstance(other, InlineResponse2002):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
