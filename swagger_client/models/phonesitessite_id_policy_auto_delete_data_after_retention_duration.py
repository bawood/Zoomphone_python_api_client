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

class PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration(object):
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
        'enable': 'bool',
        'reset': 'bool',
        'locked': 'bool',
        'items': 'list[PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDurationItems]',
        'delete_type': 'int'
    }

    attribute_map = {
        'enable': 'enable',
        'reset': 'reset',
        'locked': 'locked',
        'items': 'items',
        'delete_type': 'delete_type'
    }

    def __init__(self, enable=None, reset=None, locked=None, items=None, delete_type=None):  # noqa: E501
        """PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._reset = None
        self._locked = None
        self._items = None
        self._delete_type = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if reset is not None:
            self.reset = reset
        if locked is not None:
            self.locked = locked
        if items is not None:
            self.items = items
        if delete_type is not None:
            self.delete_type = delete_type

    @property
    def enable(self):
        """Gets the enable of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.  # noqa: E501

        Allow Zoom to automatically delete data after the retention duration has lapsed.  # noqa: E501

        :return: The enable of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.

        Allow Zoom to automatically delete data after the retention duration has lapsed.  # noqa: E501

        :param enable: The enable of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def reset(self):
        """Gets the reset of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.  # noqa: E501

        Whether the current settings will use the phone account's settings (applicable if the current settings are using the new policy framework).  # noqa: E501

        :return: The reset of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.  # noqa: E501
        :rtype: bool
        """
        return self._reset

    @reset.setter
    def reset(self, reset):
        """Sets the reset of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.

        Whether the current settings will use the phone account's settings (applicable if the current settings are using the new policy framework).  # noqa: E501

        :param reset: The reset of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.  # noqa: E501
        :type: bool
        """

        self._reset = reset

    @property
    def locked(self):
        """Gets the locked of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.  # noqa: E501

        Whether the senior administrator allows users to modify the current settings.  # noqa: E501

        :return: The locked of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.

        Whether the senior administrator allows users to modify the current settings.  # noqa: E501

        :param locked: The locked of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def items(self):
        """Gets the items of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.  # noqa: E501


        :return: The items of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.  # noqa: E501
        :rtype: list[PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDurationItems]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.


        :param items: The items of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.  # noqa: E501
        :type: list[PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDurationItems]
        """

        self._items = items

    @property
    def delete_type(self):
        """Gets the delete_type of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.  # noqa: E501

        Delete policy <br>* 1 - soft delete <br>* 2 - permanent delete  # noqa: E501

        :return: The delete_type of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.  # noqa: E501
        :rtype: int
        """
        return self._delete_type

    @delete_type.setter
    def delete_type(self, delete_type):
        """Sets the delete_type of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.

        Delete policy <br>* 1 - soft delete <br>* 2 - permanent delete  # noqa: E501

        :param delete_type: The delete_type of this PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2]  # noqa: E501
        if delete_type not in allowed_values:
            raise ValueError(
                "Invalid value for `delete_type` ({0}), must be one of {1}"  # noqa: E501
                .format(delete_type, allowed_values)
            )

        self._delete_type = delete_type

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
        if issubclass(PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration, dict):
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
        if not isinstance(other, PhonesitessiteIdPolicyAutoDeleteDataAfterRetentionDuration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
