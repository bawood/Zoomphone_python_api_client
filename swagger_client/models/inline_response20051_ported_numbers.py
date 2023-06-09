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

class InlineResponse20051PortedNumbers(object):
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
        'numbers': 'list[str]',
        'order_id': 'str',
        'replacing_numbers': 'list[InlineResponse20051ReplacingNumbers]',
        'status': 'str',
        'submission_date_time': 'str'
    }

    attribute_map = {
        'numbers': 'numbers',
        'order_id': 'order_id',
        'replacing_numbers': 'replacing_numbers',
        'status': 'status',
        'submission_date_time': 'submission_date_time'
    }

    def __init__(self, numbers=None, order_id=None, replacing_numbers=None, status=None, submission_date_time=None):  # noqa: E501
        """InlineResponse20051PortedNumbers - a model defined in Swagger"""  # noqa: E501
        self._numbers = None
        self._order_id = None
        self._replacing_numbers = None
        self._status = None
        self._submission_date_time = None
        self.discriminator = None
        if numbers is not None:
            self.numbers = numbers
        if order_id is not None:
            self.order_id = order_id
        if replacing_numbers is not None:
            self.replacing_numbers = replacing_numbers
        if status is not None:
            self.status = status
        if submission_date_time is not None:
            self.submission_date_time = submission_date_time

    @property
    def numbers(self):
        """Gets the numbers of this InlineResponse20051PortedNumbers.  # noqa: E501

        The ported numbers.  # noqa: E501

        :return: The numbers of this InlineResponse20051PortedNumbers.  # noqa: E501
        :rtype: list[str]
        """
        return self._numbers

    @numbers.setter
    def numbers(self, numbers):
        """Sets the numbers of this InlineResponse20051PortedNumbers.

        The ported numbers.  # noqa: E501

        :param numbers: The numbers of this InlineResponse20051PortedNumbers.  # noqa: E501
        :type: list[str]
        """

        self._numbers = numbers

    @property
    def order_id(self):
        """Gets the order_id of this InlineResponse20051PortedNumbers.  # noqa: E501

        The ported numbers' order ID.  # noqa: E501

        :return: The order_id of this InlineResponse20051PortedNumbers.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this InlineResponse20051PortedNumbers.

        The ported numbers' order ID.  # noqa: E501

        :param order_id: The order_id of this InlineResponse20051PortedNumbers.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def replacing_numbers(self):
        """Gets the replacing_numbers of this InlineResponse20051PortedNumbers.  # noqa: E501

        The ported numbers' replacement numbers.  # noqa: E501

        :return: The replacing_numbers of this InlineResponse20051PortedNumbers.  # noqa: E501
        :rtype: list[InlineResponse20051ReplacingNumbers]
        """
        return self._replacing_numbers

    @replacing_numbers.setter
    def replacing_numbers(self, replacing_numbers):
        """Sets the replacing_numbers of this InlineResponse20051PortedNumbers.

        The ported numbers' replacement numbers.  # noqa: E501

        :param replacing_numbers: The replacing_numbers of this InlineResponse20051PortedNumbers.  # noqa: E501
        :type: list[InlineResponse20051ReplacingNumbers]
        """

        self._replacing_numbers = replacing_numbers

    @property
    def status(self):
        """Gets the status of this InlineResponse20051PortedNumbers.  # noqa: E501

        The ported numbers' status.  # noqa: E501

        :return: The status of this InlineResponse20051PortedNumbers.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20051PortedNumbers.

        The ported numbers' status.  # noqa: E501

        :param status: The status of this InlineResponse20051PortedNumbers.  # noqa: E501
        :type: str
        """
        allowed_values = ["Not_Submitted", "Waiting", "Processing", "Successfully", "Rejected", "Canceled", "FOC"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def submission_date_time(self):
        """Gets the submission_date_time of this InlineResponse20051PortedNumbers.  # noqa: E501

        The time ported numbers were submitted (format: 'yyyy-MM-ddThh:dd:ssZ').  # noqa: E501

        :return: The submission_date_time of this InlineResponse20051PortedNumbers.  # noqa: E501
        :rtype: str
        """
        return self._submission_date_time

    @submission_date_time.setter
    def submission_date_time(self, submission_date_time):
        """Sets the submission_date_time of this InlineResponse20051PortedNumbers.

        The time ported numbers were submitted (format: 'yyyy-MM-ddThh:dd:ssZ').  # noqa: E501

        :param submission_date_time: The submission_date_time of this InlineResponse20051PortedNumbers.  # noqa: E501
        :type: str
        """

        self._submission_date_time = submission_date_time

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
        if issubclass(InlineResponse20051PortedNumbers, dict):
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
        if not isinstance(other, InlineResponse20051PortedNumbers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
