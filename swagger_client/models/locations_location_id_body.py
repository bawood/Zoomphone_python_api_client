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

class LocationsLocationIdBody(object):
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
        'bssid': 'str',
        'elin_phone_number_id': 'str',
        'emergency_address_id': 'str',
        'name': 'str',
        'network_switches': 'list[PhonelocationslocationIdNetworkSwitches]',
        'private_ip': 'str',
        'public_ip': 'str',
        'sip_group_id': 'str',
        'minimum_match_criteria': 'bool'
    }

    attribute_map = {
        'bssid': 'bssid',
        'elin_phone_number_id': 'elin_phone_number_id',
        'emergency_address_id': 'emergency_address_id',
        'name': 'name',
        'network_switches': 'network_switches',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'sip_group_id': 'sip_group_id',
        'minimum_match_criteria': 'minimum_match_criteria'
    }

    def __init__(self, bssid=None, elin_phone_number_id=None, emergency_address_id=None, name=None, network_switches=None, private_ip=None, public_ip=None, sip_group_id=None, minimum_match_criteria=None):  # noqa: E501
        """LocationsLocationIdBody - a model defined in Swagger"""  # noqa: E501
        self._bssid = None
        self._elin_phone_number_id = None
        self._emergency_address_id = None
        self._name = None
        self._network_switches = None
        self._private_ip = None
        self._public_ip = None
        self._sip_group_id = None
        self._minimum_match_criteria = None
        self.discriminator = None
        if bssid is not None:
            self.bssid = bssid
        if elin_phone_number_id is not None:
            self.elin_phone_number_id = elin_phone_number_id
        if emergency_address_id is not None:
            self.emergency_address_id = emergency_address_id
        if name is not None:
            self.name = name
        if network_switches is not None:
            self.network_switches = network_switches
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if sip_group_id is not None:
            self.sip_group_id = sip_group_id
        if minimum_match_criteria is not None:
            self.minimum_match_criteria = minimum_match_criteria

    @property
    def bssid(self):
        """Gets the bssid of this LocationsLocationIdBody.  # noqa: E501

        A comma-separated list of the emergency service location's BSSIDs (Basic Service Set Identifiers).  # noqa: E501

        :return: The bssid of this LocationsLocationIdBody.  # noqa: E501
        :rtype: str
        """
        return self._bssid

    @bssid.setter
    def bssid(self, bssid):
        """Sets the bssid of this LocationsLocationIdBody.

        A comma-separated list of the emergency service location's BSSIDs (Basic Service Set Identifiers).  # noqa: E501

        :param bssid: The bssid of this LocationsLocationIdBody.  # noqa: E501
        :type: str
        """

        self._bssid = bssid

    @property
    def elin_phone_number_id(self):
        """Gets the elin_phone_number_id of this LocationsLocationIdBody.  # noqa: E501

        The ELIN (Emergency Location Identification Number). This value must be a phone number ID or phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format.  # noqa: E501

        :return: The elin_phone_number_id of this LocationsLocationIdBody.  # noqa: E501
        :rtype: str
        """
        return self._elin_phone_number_id

    @elin_phone_number_id.setter
    def elin_phone_number_id(self, elin_phone_number_id):
        """Sets the elin_phone_number_id of this LocationsLocationIdBody.

        The ELIN (Emergency Location Identification Number). This value must be a phone number ID or phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format.  # noqa: E501

        :param elin_phone_number_id: The elin_phone_number_id of this LocationsLocationIdBody.  # noqa: E501
        :type: str
        """

        self._elin_phone_number_id = elin_phone_number_id

    @property
    def emergency_address_id(self):
        """Gets the emergency_address_id of this LocationsLocationIdBody.  # noqa: E501

        The emergency location's address ID.  # noqa: E501

        :return: The emergency_address_id of this LocationsLocationIdBody.  # noqa: E501
        :rtype: str
        """
        return self._emergency_address_id

    @emergency_address_id.setter
    def emergency_address_id(self, emergency_address_id):
        """Sets the emergency_address_id of this LocationsLocationIdBody.

        The emergency location's address ID.  # noqa: E501

        :param emergency_address_id: The emergency_address_id of this LocationsLocationIdBody.  # noqa: E501
        :type: str
        """

        self._emergency_address_id = emergency_address_id

    @property
    def name(self):
        """Gets the name of this LocationsLocationIdBody.  # noqa: E501

        The emergency location's name.  # noqa: E501

        :return: The name of this LocationsLocationIdBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LocationsLocationIdBody.

        The emergency location's name.  # noqa: E501

        :param name: The name of this LocationsLocationIdBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def network_switches(self):
        """Gets the network_switches of this LocationsLocationIdBody.  # noqa: E501


        :return: The network_switches of this LocationsLocationIdBody.  # noqa: E501
        :rtype: list[PhonelocationslocationIdNetworkSwitches]
        """
        return self._network_switches

    @network_switches.setter
    def network_switches(self, network_switches):
        """Sets the network_switches of this LocationsLocationIdBody.


        :param network_switches: The network_switches of this LocationsLocationIdBody.  # noqa: E501
        :type: list[PhonelocationslocationIdNetworkSwitches]
        """

        self._network_switches = network_switches

    @property
    def private_ip(self):
        """Gets the private_ip of this LocationsLocationIdBody.  # noqa: E501

        A comma-separated list of the emergency service location's subnet or private IP addresses. This field is required if `minimum_match_criteria` is true.  # noqa: E501

        :return: The private_ip of this LocationsLocationIdBody.  # noqa: E501
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this LocationsLocationIdBody.

        A comma-separated list of the emergency service location's subnet or private IP addresses. This field is required if `minimum_match_criteria` is true.  # noqa: E501

        :param private_ip: The private_ip of this LocationsLocationIdBody.  # noqa: E501
        :type: str
        """

        self._private_ip = private_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this LocationsLocationIdBody.  # noqa: E501

        A comma-separated list of the emergency service location's public IP addresses. This parameter is **required** for top locations.  # noqa: E501

        :return: The public_ip of this LocationsLocationIdBody.  # noqa: E501
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this LocationsLocationIdBody.

        A comma-separated list of the emergency service location's public IP addresses. This parameter is **required** for top locations.  # noqa: E501

        :param public_ip: The public_ip of this LocationsLocationIdBody.  # noqa: E501
        :type: str
        """

        self._public_ip = public_ip

    @property
    def sip_group_id(self):
        """Gets the sip_group_id of this LocationsLocationIdBody.  # noqa: E501

        The SIP group ID to assign to the emergency service location. This value is not required for non-top locations.  # noqa: E501

        :return: The sip_group_id of this LocationsLocationIdBody.  # noqa: E501
        :rtype: str
        """
        return self._sip_group_id

    @sip_group_id.setter
    def sip_group_id(self, sip_group_id):
        """Sets the sip_group_id of this LocationsLocationIdBody.

        The SIP group ID to assign to the emergency service location. This value is not required for non-top locations.  # noqa: E501

        :param sip_group_id: The sip_group_id of this LocationsLocationIdBody.  # noqa: E501
        :type: str
        """

        self._sip_group_id = sip_group_id

    @property
    def minimum_match_criteria(self):
        """Gets the minimum_match_criteria of this LocationsLocationIdBody.  # noqa: E501

        If true, it requires a user's location match on both public and private IP address, or BSSID, or network switch; detecting only a public IP address is not enough to detect the location.  # noqa: E501

        :return: The minimum_match_criteria of this LocationsLocationIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._minimum_match_criteria

    @minimum_match_criteria.setter
    def minimum_match_criteria(self, minimum_match_criteria):
        """Sets the minimum_match_criteria of this LocationsLocationIdBody.

        If true, it requires a user's location match on both public and private IP address, or BSSID, or network switch; detecting only a public IP address is not enough to detect the location.  # noqa: E501

        :param minimum_match_criteria: The minimum_match_criteria of this LocationsLocationIdBody.  # noqa: E501
        :type: bool
        """

        self._minimum_match_criteria = minimum_match_criteria

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
        if issubclass(LocationsLocationIdBody, dict):
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
        if not isinstance(other, LocationsLocationIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
