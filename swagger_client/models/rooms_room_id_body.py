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

class RoomsRoomIdBody(object):
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
        'extension_number': 'int',
        'policy': 'PhoneroomsroomIdPolicy',
        'site_id': 'str'
    }

    attribute_map = {
        'extension_number': 'extension_number',
        'policy': 'policy',
        'site_id': 'site_id'
    }

    def __init__(self, extension_number=None, policy=None, site_id=None):  # noqa: E501
        """RoomsRoomIdBody - a model defined in Swagger"""  # noqa: E501
        self._extension_number = None
        self._policy = None
        self._site_id = None
        self.discriminator = None
        if extension_number is not None:
            self.extension_number = extension_number
        if policy is not None:
            self.policy = policy
        if site_id is not None:
            self.site_id = site_id

    @property
    def extension_number(self):
        """Gets the extension_number of this RoomsRoomIdBody.  # noqa: E501

        The extension number of the Zoom Room. The number must be complete (i.e. site number + short extension).  # noqa: E501

        :return: The extension_number of this RoomsRoomIdBody.  # noqa: E501
        :rtype: int
        """
        return self._extension_number

    @extension_number.setter
    def extension_number(self, extension_number):
        """Sets the extension_number of this RoomsRoomIdBody.

        The extension number of the Zoom Room. The number must be complete (i.e. site number + short extension).  # noqa: E501

        :param extension_number: The extension_number of this RoomsRoomIdBody.  # noqa: E501
        :type: int
        """

        self._extension_number = extension_number

    @property
    def policy(self):
        """Gets the policy of this RoomsRoomIdBody.  # noqa: E501


        :return: The policy of this RoomsRoomIdBody.  # noqa: E501
        :rtype: PhoneroomsroomIdPolicy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this RoomsRoomIdBody.


        :param policy: The policy of this RoomsRoomIdBody.  # noqa: E501
        :type: PhoneroomsroomIdPolicy
        """

        self._policy = policy

    @property
    def site_id(self):
        """Gets the site_id of this RoomsRoomIdBody.  # noqa: E501

        Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites).  # noqa: E501

        :return: The site_id of this RoomsRoomIdBody.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this RoomsRoomIdBody.

        Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites).  # noqa: E501

        :param site_id: The site_id of this RoomsRoomIdBody.  # noqa: E501
        :type: str
        """

        self._site_id = site_id

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
        if issubclass(RoomsRoomIdBody, dict):
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
        if not isinstance(other, RoomsRoomIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
