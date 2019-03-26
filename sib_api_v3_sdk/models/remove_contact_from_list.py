# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class RemoveContactFromList(object):
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
        'emails': 'list[str]',
        'all': 'bool'
    }

    attribute_map = {
        'emails': 'emails',
        'all': 'all'
    }

    def __init__(self, emails=None, all=None):  # noqa: E501
        """RemoveContactFromList - a model defined in Swagger"""  # noqa: E501
        self._emails = None
        self._all = None
        self.discriminator = None
        if emails is not None:
            self.emails = emails
        if all is not None:
            self.all = all

    @property
    def emails(self):
        """Gets the emails of this RemoveContactFromList.  # noqa: E501

        Required if 'all' is false. Emails to remove from a list  # noqa: E501

        :return: The emails of this RemoveContactFromList.  # noqa: E501
        :rtype: list[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this RemoveContactFromList.

        Required if 'all' is false. Emails to remove from a list  # noqa: E501

        :param emails: The emails of this RemoveContactFromList.  # noqa: E501
        :type: list[str]
        """

        self._emails = emails

    @property
    def all(self):
        """Gets the all of this RemoveContactFromList.  # noqa: E501

        Required if 'emails' is empty. Remove all existing contacts from a list  # noqa: E501

        :return: The all of this RemoveContactFromList.  # noqa: E501
        :rtype: bool
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this RemoveContactFromList.

        Required if 'emails' is empty. Remove all existing contacts from a list  # noqa: E501

        :param all: The all of this RemoveContactFromList.  # noqa: E501
        :type: bool
        """

        self._all = all

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
        if issubclass(RemoveContactFromList, dict):
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
        if not isinstance(other, RemoveContactFromList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
