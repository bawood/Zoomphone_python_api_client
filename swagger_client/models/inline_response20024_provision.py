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

class InlineResponse20024Provision(object):
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
        'sip_accounts': 'list[InlineResponse20024ProvisionSipAccounts]',
        'type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'sip_accounts': 'sip_accounts',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, sip_accounts=None, type=None, url=None):  # noqa: E501
        """InlineResponse20024Provision - a model defined in Swagger"""  # noqa: E501
        self._sip_accounts = None
        self._type = None
        self._url = None
        self.discriminator = None
        if sip_accounts is not None:
            self.sip_accounts = sip_accounts
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url

    @property
    def sip_accounts(self):
        """Gets the sip_accounts of this InlineResponse20024Provision.  # noqa: E501

        SIP Account details registered during the device provisioning process. This object will only be returned if manual provisioning was used for the device.    # noqa: E501

        :return: The sip_accounts of this InlineResponse20024Provision.  # noqa: E501
        :rtype: list[InlineResponse20024ProvisionSipAccounts]
        """
        return self._sip_accounts

    @sip_accounts.setter
    def sip_accounts(self, sip_accounts):
        """Sets the sip_accounts of this InlineResponse20024Provision.

        SIP Account details registered during the device provisioning process. This object will only be returned if manual provisioning was used for the device.    # noqa: E501

        :param sip_accounts: The sip_accounts of this InlineResponse20024Provision.  # noqa: E501
        :type: list[InlineResponse20024ProvisionSipAccounts]
        """

        self._sip_accounts = sip_accounts

    @property
    def type(self):
        """Gets the type of this InlineResponse20024Provision.  # noqa: E501

        [Provisioning type](https://support.zoom.us/hc/en-us/articles/360033223411). The value can be one of the following:  * `ztp` : Zero touch provisioning. * `assisted`: Assisted provisioning. * `manual`: Manual provisioning.     # noqa: E501

        :return: The type of this InlineResponse20024Provision.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20024Provision.

        [Provisioning type](https://support.zoom.us/hc/en-us/articles/360033223411). The value can be one of the following:  * `ztp` : Zero touch provisioning. * `assisted`: Assisted provisioning. * `manual`: Manual provisioning.     # noqa: E501

        :param type: The type of this InlineResponse20024Provision.  # noqa: E501
        :type: str
        """
        allowed_values = ["assisted", "ztp", "manual"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def url(self):
        """Gets the url of this InlineResponse20024Provision.  # noqa: E501

        Provisioning URL. This field will only be returned for devices that were provisioned via `assisted` provisioning type.  # noqa: E501

        :return: The url of this InlineResponse20024Provision.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineResponse20024Provision.

        Provisioning URL. This field will only be returned for devices that were provisioned via `assisted` provisioning type.  # noqa: E501

        :param url: The url of this InlineResponse20024Provision.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(InlineResponse20024Provision, dict):
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
        if not isinstance(other, InlineResponse20024Provision):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
