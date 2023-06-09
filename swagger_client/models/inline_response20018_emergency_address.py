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

class InlineResponse20018EmergencyAddress(object):
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
        'address_line1': 'str',
        'address_line2': 'str',
        'city': 'str',
        'country': 'str',
        'id': 'str',
        'state_code': 'str',
        'status': 'int',
        'zip': 'str'
    }

    attribute_map = {
        'address_line1': 'address_line1',
        'address_line2': 'address_line2',
        'city': 'city',
        'country': 'country',
        'id': 'id',
        'state_code': 'state_code',
        'status': 'status',
        'zip': 'zip'
    }

    def __init__(self, address_line1=None, address_line2=None, city=None, country=None, id=None, state_code=None, status=None, zip=None):  # noqa: E501
        """InlineResponse20018EmergencyAddress - a model defined in Swagger"""  # noqa: E501
        self._address_line1 = None
        self._address_line2 = None
        self._city = None
        self._country = None
        self._id = None
        self._state_code = None
        self._status = None
        self._zip = None
        self.discriminator = None
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if id is not None:
            self.id = id
        if state_code is not None:
            self.state_code = state_code
        if status is not None:
            self.status = status
        if zip is not None:
            self.zip = zip

    @property
    def address_line1(self):
        """Gets the address_line1 of this InlineResponse20018EmergencyAddress.  # noqa: E501

        The emergency location address line 1.  # noqa: E501

        :return: The address_line1 of this InlineResponse20018EmergencyAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this InlineResponse20018EmergencyAddress.

        The emergency location address line 1.  # noqa: E501

        :param address_line1: The address_line1 of this InlineResponse20018EmergencyAddress.  # noqa: E501
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this InlineResponse20018EmergencyAddress.  # noqa: E501

        The emergency location address line 2.  # noqa: E501

        :return: The address_line2 of this InlineResponse20018EmergencyAddress.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this InlineResponse20018EmergencyAddress.

        The emergency location address line 2.  # noqa: E501

        :param address_line2: The address_line2 of this InlineResponse20018EmergencyAddress.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """Gets the city of this InlineResponse20018EmergencyAddress.  # noqa: E501

        The emergency location address's city.  # noqa: E501

        :return: The city of this InlineResponse20018EmergencyAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this InlineResponse20018EmergencyAddress.

        The emergency location address's city.  # noqa: E501

        :param city: The city of this InlineResponse20018EmergencyAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this InlineResponse20018EmergencyAddress.  # noqa: E501

        The emergency location address's country.  # noqa: E501

        :return: The country of this InlineResponse20018EmergencyAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this InlineResponse20018EmergencyAddress.

        The emergency location address's country.  # noqa: E501

        :param country: The country of this InlineResponse20018EmergencyAddress.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def id(self):
        """Gets the id of this InlineResponse20018EmergencyAddress.  # noqa: E501

        The emergency location address ID.  # noqa: E501

        :return: The id of this InlineResponse20018EmergencyAddress.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20018EmergencyAddress.

        The emergency location address ID.  # noqa: E501

        :param id: The id of this InlineResponse20018EmergencyAddress.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state_code(self):
        """Gets the state_code of this InlineResponse20018EmergencyAddress.  # noqa: E501

        The emergency location address's state code.  # noqa: E501

        :return: The state_code of this InlineResponse20018EmergencyAddress.  # noqa: E501
        :rtype: str
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code):
        """Sets the state_code of this InlineResponse20018EmergencyAddress.

        The emergency location address's state code.  # noqa: E501

        :param state_code: The state_code of this InlineResponse20018EmergencyAddress.  # noqa: E501
        :type: str
        """

        self._state_code = state_code

    @property
    def status(self):
        """Gets the status of this InlineResponse20018EmergencyAddress.  # noqa: E501

        The emergency address verification status.:  * `1` — Verification Not Required.  * `2` — Unverified.  * `3` — Verification Requested.  * `4` — Verfied.  * `5` — Rejected.  * `6` — Verification Failed.  # noqa: E501

        :return: The status of this InlineResponse20018EmergencyAddress.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20018EmergencyAddress.

        The emergency address verification status.:  * `1` — Verification Not Required.  * `2` — Unverified.  * `3` — Verification Requested.  * `4` — Verfied.  * `5` — Rejected.  * `6` — Verification Failed.  # noqa: E501

        :param status: The status of this InlineResponse20018EmergencyAddress.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3, 4, 5, 6]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def zip(self):
        """Gets the zip of this InlineResponse20018EmergencyAddress.  # noqa: E501

        The emergency address zip code.  # noqa: E501

        :return: The zip of this InlineResponse20018EmergencyAddress.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this InlineResponse20018EmergencyAddress.

        The emergency address zip code.  # noqa: E501

        :param zip: The zip of this InlineResponse20018EmergencyAddress.  # noqa: E501
        :type: str
        """

        self._zip = zip

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
        if issubclass(InlineResponse20018EmergencyAddress, dict):
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
        if not isinstance(other, InlineResponse20018EmergencyAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
