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

class PhoneGroupCallPickupBody(object):
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
        'display_name': 'str',
        'site_id': 'str',
        'description': 'str',
        'extension_number': 'int',
        'delay': 'int',
        'play_incoming_calls_sound': 'PhonegroupCallPickupPlayIncomingCallsSound',
        'directed_call_pickup': 'bool',
        'member_extension_ids': 'list[str]'
    }

    attribute_map = {
        'display_name': 'display_name',
        'site_id': 'site_id',
        'description': 'description',
        'extension_number': 'extension_number',
        'delay': 'delay',
        'play_incoming_calls_sound': 'play_incoming_calls_sound',
        'directed_call_pickup': 'directed_call_pickup',
        'member_extension_ids': 'member_extension_ids'
    }

    def __init__(self, display_name=None, site_id=None, description=None, extension_number=None, delay=DelayEnum._0, play_incoming_calls_sound=None, directed_call_pickup=False, member_extension_ids=None):  # noqa: E501
        """PhoneGroupCallPickupBody - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._site_id = None
        self._description = None
        self._extension_number = None
        self._delay = None
        self._play_incoming_calls_sound = None
        self._directed_call_pickup = None
        self._member_extension_ids = None
        self.discriminator = None
        self.display_name = display_name
        self.site_id = site_id
        if description is not None:
            self.description = description
        if extension_number is not None:
            self.extension_number = extension_number
        if delay is not None:
            self.delay = delay
        if play_incoming_calls_sound is not None:
            self.play_incoming_calls_sound = play_incoming_calls_sound
        if directed_call_pickup is not None:
            self.directed_call_pickup = directed_call_pickup
        if member_extension_ids is not None:
            self.member_extension_ids = member_extension_ids

    @property
    def display_name(self):
        """Gets the display_name of this PhoneGroupCallPickupBody.  # noqa: E501

        Name of the group.  # noqa: E501

        :return: The display_name of this PhoneGroupCallPickupBody.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PhoneGroupCallPickupBody.

        Name of the group.  # noqa: E501

        :param display_name: The display_name of this PhoneGroupCallPickupBody.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def site_id(self):
        """Gets the site_id of this PhoneGroupCallPickupBody.  # noqa: E501

        Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites).  # noqa: E501

        :return: The site_id of this PhoneGroupCallPickupBody.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this PhoneGroupCallPickupBody.

        Unique identifier of the [site](https://support.zoom.us/hc/en-us/articles/360020809672-Managing-Multiple-Sites).  # noqa: E501

        :param site_id: The site_id of this PhoneGroupCallPickupBody.  # noqa: E501
        :type: str
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def description(self):
        """Gets the description of this PhoneGroupCallPickupBody.  # noqa: E501

        Group call pickup description.  # noqa: E501

        :return: The description of this PhoneGroupCallPickupBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PhoneGroupCallPickupBody.

        Group call pickup description.  # noqa: E501

        :param description: The description of this PhoneGroupCallPickupBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def extension_number(self):
        """Gets the extension_number of this PhoneGroupCallPickupBody.  # noqa: E501

        Short extension number.  # noqa: E501

        :return: The extension_number of this PhoneGroupCallPickupBody.  # noqa: E501
        :rtype: int
        """
        return self._extension_number

    @extension_number.setter
    def extension_number(self, extension_number):
        """Sets the extension_number of this PhoneGroupCallPickupBody.

        Short extension number.  # noqa: E501

        :param extension_number: The extension_number of this PhoneGroupCallPickupBody.  # noqa: E501
        :type: int
        """

        self._extension_number = extension_number

    @property
    def delay(self):
        """Gets the delay of this PhoneGroupCallPickupBody.  # noqa: E501

        Determines after how much time (in seconds) the group should be notified.  # noqa: E501

        :return: The delay of this PhoneGroupCallPickupBody.  # noqa: E501
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this PhoneGroupCallPickupBody.

        Determines after how much time (in seconds) the group should be notified.  # noqa: E501

        :param delay: The delay of this PhoneGroupCallPickupBody.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 5, 10, 15]  # noqa: E501
        if delay not in allowed_values:
            raise ValueError(
                "Invalid value for `delay` ({0}), must be one of {1}"  # noqa: E501
                .format(delay, allowed_values)
            )

        self._delay = delay

    @property
    def play_incoming_calls_sound(self):
        """Gets the play_incoming_calls_sound of this PhoneGroupCallPickupBody.  # noqa: E501


        :return: The play_incoming_calls_sound of this PhoneGroupCallPickupBody.  # noqa: E501
        :rtype: PhonegroupCallPickupPlayIncomingCallsSound
        """
        return self._play_incoming_calls_sound

    @play_incoming_calls_sound.setter
    def play_incoming_calls_sound(self, play_incoming_calls_sound):
        """Sets the play_incoming_calls_sound of this PhoneGroupCallPickupBody.


        :param play_incoming_calls_sound: The play_incoming_calls_sound of this PhoneGroupCallPickupBody.  # noqa: E501
        :type: PhonegroupCallPickupPlayIncomingCallsSound
        """

        self._play_incoming_calls_sound = play_incoming_calls_sound

    @property
    def directed_call_pickup(self):
        """Gets the directed_call_pickup of this PhoneGroupCallPickupBody.  # noqa: E501

        Whether the ringtone is on.  # noqa: E501

        :return: The directed_call_pickup of this PhoneGroupCallPickupBody.  # noqa: E501
        :rtype: bool
        """
        return self._directed_call_pickup

    @directed_call_pickup.setter
    def directed_call_pickup(self, directed_call_pickup):
        """Sets the directed_call_pickup of this PhoneGroupCallPickupBody.

        Whether the ringtone is on.  # noqa: E501

        :param directed_call_pickup: The directed_call_pickup of this PhoneGroupCallPickupBody.  # noqa: E501
        :type: bool
        """

        self._directed_call_pickup = directed_call_pickup

    @property
    def member_extension_ids(self):
        """Gets the member_extension_ids of this PhoneGroupCallPickupBody.  # noqa: E501

        Extension ID.  # noqa: E501

        :return: The member_extension_ids of this PhoneGroupCallPickupBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._member_extension_ids

    @member_extension_ids.setter
    def member_extension_ids(self, member_extension_ids):
        """Sets the member_extension_ids of this PhoneGroupCallPickupBody.

        Extension ID.  # noqa: E501

        :param member_extension_ids: The member_extension_ids of this PhoneGroupCallPickupBody.  # noqa: E501
        :type: list[str]
        """

        self._member_extension_ids = member_extension_ids

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
        if issubclass(PhoneGroupCallPickupBody, dict):
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
        if not isinstance(other, PhoneGroupCallPickupBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
