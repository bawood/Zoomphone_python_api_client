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

class InlineResponse20127VoiceMail(object):
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
        'access_user_id': 'str',
        'delete': 'bool',
        'download': 'bool',
        'shared_id': 'str'
    }

    attribute_map = {
        'access_user_id': 'access_user_id',
        'delete': 'delete',
        'download': 'download',
        'shared_id': 'shared_id'
    }

    def __init__(self, access_user_id=None, delete=None, download=None, shared_id=None):  # noqa: E501
        """InlineResponse20127VoiceMail - a model defined in Swagger"""  # noqa: E501
        self._access_user_id = None
        self._delete = None
        self._download = None
        self._shared_id = None
        self.discriminator = None
        if access_user_id is not None:
            self.access_user_id = access_user_id
        if delete is not None:
            self.delete = delete
        if download is not None:
            self.download = download
        if shared_id is not None:
            self.shared_id = shared_id

    @property
    def access_user_id(self):
        """Gets the access_user_id of this InlineResponse20127VoiceMail.  # noqa: E501

        The user that is allowed to access voicemail messages for the extension.  # noqa: E501

        :return: The access_user_id of this InlineResponse20127VoiceMail.  # noqa: E501
        :rtype: str
        """
        return self._access_user_id

    @access_user_id.setter
    def access_user_id(self, access_user_id):
        """Sets the access_user_id of this InlineResponse20127VoiceMail.

        The user that is allowed to access voicemail messages for the extension.  # noqa: E501

        :param access_user_id: The access_user_id of this InlineResponse20127VoiceMail.  # noqa: E501
        :type: str
        """

        self._access_user_id = access_user_id

    @property
    def delete(self):
        """Gets the delete of this InlineResponse20127VoiceMail.  # noqa: E501

        Whether the user has delete permissions. The default is **false**.  # noqa: E501

        :return: The delete of this InlineResponse20127VoiceMail.  # noqa: E501
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """Sets the delete of this InlineResponse20127VoiceMail.

        Whether the user has delete permissions. The default is **false**.  # noqa: E501

        :param delete: The delete of this InlineResponse20127VoiceMail.  # noqa: E501
        :type: bool
        """

        self._delete = delete

    @property
    def download(self):
        """Gets the download of this InlineResponse20127VoiceMail.  # noqa: E501

        Whether the user has download permissions. The default is **false**.  # noqa: E501

        :return: The download of this InlineResponse20127VoiceMail.  # noqa: E501
        :rtype: bool
        """
        return self._download

    @download.setter
    def download(self, download):
        """Sets the download of this InlineResponse20127VoiceMail.

        Whether the user has download permissions. The default is **false**.  # noqa: E501

        :param download: The download of this InlineResponse20127VoiceMail.  # noqa: E501
        :type: bool
        """

        self._download = download

    @property
    def shared_id(self):
        """Gets the shared_id of this InlineResponse20127VoiceMail.  # noqa: E501

        The unique identifier of the voicemail that the user can access.  # noqa: E501

        :return: The shared_id of this InlineResponse20127VoiceMail.  # noqa: E501
        :rtype: str
        """
        return self._shared_id

    @shared_id.setter
    def shared_id(self, shared_id):
        """Sets the shared_id of this InlineResponse20127VoiceMail.

        The unique identifier of the voicemail that the user can access.  # noqa: E501

        :param shared_id: The shared_id of this InlineResponse20127VoiceMail.  # noqa: E501
        :type: str
        """

        self._shared_id = shared_id

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
        if issubclass(InlineResponse20127VoiceMail, dict):
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
        if not isinstance(other, InlineResponse20127VoiceMail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
