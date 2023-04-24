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

class PhonesitessiteIdsettingssettingTypeHolidays(object):
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
        '_from': 'datetime',
        'to': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, name=None, _from=None, to=None):  # noqa: E501
        """PhonesitessiteIdsettingssettingTypeHolidays - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self.__from = None
        self._to = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to

    @property
    def name(self):
        """Gets the name of this PhonesitessiteIdsettingssettingTypeHolidays.  # noqa: E501

        The name of the holiday.  # noqa: E501

        :return: The name of this PhonesitessiteIdsettingssettingTypeHolidays.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PhonesitessiteIdsettingssettingTypeHolidays.

        The name of the holiday.  # noqa: E501

        :param name: The name of this PhonesitessiteIdsettingssettingTypeHolidays.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def _from(self):
        """Gets the _from of this PhonesitessiteIdsettingssettingTypeHolidays.  # noqa: E501

        The holiday start date and time in `yyyy-MM-dd'T'HH:mm:ss'Z'` format.  # noqa: E501

        :return: The _from of this PhonesitessiteIdsettingssettingTypeHolidays.  # noqa: E501
        :rtype: datetime
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this PhonesitessiteIdsettingssettingTypeHolidays.

        The holiday start date and time in `yyyy-MM-dd'T'HH:mm:ss'Z'` format.  # noqa: E501

        :param _from: The _from of this PhonesitessiteIdsettingssettingTypeHolidays.  # noqa: E501
        :type: datetime
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this PhonesitessiteIdsettingssettingTypeHolidays.  # noqa: E501

        The holiday end date and time, in `yyyy-MM-dd'T'HH:mm:ss'Z'` format.  # noqa: E501

        :return: The to of this PhonesitessiteIdsettingssettingTypeHolidays.  # noqa: E501
        :rtype: datetime
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this PhonesitessiteIdsettingssettingTypeHolidays.

        The holiday end date and time, in `yyyy-MM-dd'T'HH:mm:ss'Z'` format.  # noqa: E501

        :param to: The to of this PhonesitessiteIdsettingssettingTypeHolidays.  # noqa: E501
        :type: datetime
        """

        self._to = to

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
        if issubclass(PhonesitessiteIdsettingssettingTypeHolidays, dict):
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
        if not isinstance(other, PhonesitessiteIdsettingssettingTypeHolidays):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
