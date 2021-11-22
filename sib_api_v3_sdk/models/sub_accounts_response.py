# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SubAccountsResponse(object):
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
        'count': 'int',
        'sub_accounts': 'list[SubAccountsResponseSubAccounts]'
    }

    attribute_map = {
        'count': 'count',
        'sub_accounts': 'subAccounts'
    }

    def __init__(self, count=None, sub_accounts=None):  # noqa: E501
        """SubAccountsResponse - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._sub_accounts = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if sub_accounts is not None:
            self.sub_accounts = sub_accounts

    @property
    def count(self):
        """Gets the count of this SubAccountsResponse.  # noqa: E501

        Total number of subaccounts  # noqa: E501

        :return: The count of this SubAccountsResponse.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this SubAccountsResponse.

        Total number of subaccounts  # noqa: E501

        :param count: The count of this SubAccountsResponse.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def sub_accounts(self):
        """Gets the sub_accounts of this SubAccountsResponse.  # noqa: E501


        :return: The sub_accounts of this SubAccountsResponse.  # noqa: E501
        :rtype: list[SubAccountsResponseSubAccounts]
        """
        return self._sub_accounts

    @sub_accounts.setter
    def sub_accounts(self, sub_accounts):
        """Sets the sub_accounts of this SubAccountsResponse.


        :param sub_accounts: The sub_accounts of this SubAccountsResponse.  # noqa: E501
        :type: list[SubAccountsResponseSubAccounts]
        """

        self._sub_accounts = sub_accounts

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
        if issubclass(SubAccountsResponse, dict):
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
        if not isinstance(other, SubAccountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
