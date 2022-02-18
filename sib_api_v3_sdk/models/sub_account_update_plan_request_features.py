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


class SubAccountUpdatePlanRequestFeatures(object):
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
        'users': 'int',
        'landing_page': 'int',
        'inbox': 'int'
    }

    attribute_map = {
        'users': 'users',
        'landing_page': 'landingPage',
        'inbox': 'inbox'
    }

    def __init__(self, users=None, landing_page=None, inbox=None):  # noqa: E501
        """SubAccountUpdatePlanRequestFeatures - a model defined in Swagger"""  # noqa: E501

        self._users = None
        self._landing_page = None
        self._inbox = None
        self.discriminator = None

        if users is not None:
            self.users = users
        if landing_page is not None:
            self.landing_page = landing_page
        if inbox is not None:
            self.inbox = inbox

    @property
    def users(self):
        """Gets the users of this SubAccountUpdatePlanRequestFeatures.  # noqa: E501

        Number of multi-users  # noqa: E501

        :return: The users of this SubAccountUpdatePlanRequestFeatures.  # noqa: E501
        :rtype: int
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this SubAccountUpdatePlanRequestFeatures.

        Number of multi-users  # noqa: E501

        :param users: The users of this SubAccountUpdatePlanRequestFeatures.  # noqa: E501
        :type: int
        """

        self._users = users

    @property
    def landing_page(self):
        """Gets the landing_page of this SubAccountUpdatePlanRequestFeatures.  # noqa: E501

        Number of landing pages  # noqa: E501

        :return: The landing_page of this SubAccountUpdatePlanRequestFeatures.  # noqa: E501
        :rtype: int
        """
        return self._landing_page

    @landing_page.setter
    def landing_page(self, landing_page):
        """Sets the landing_page of this SubAccountUpdatePlanRequestFeatures.

        Number of landing pages  # noqa: E501

        :param landing_page: The landing_page of this SubAccountUpdatePlanRequestFeatures.  # noqa: E501
        :type: int
        """

        self._landing_page = landing_page

    @property
    def inbox(self):
        """Gets the inbox of this SubAccountUpdatePlanRequestFeatures.  # noqa: E501

        Number of inboxes  # noqa: E501

        :return: The inbox of this SubAccountUpdatePlanRequestFeatures.  # noqa: E501
        :rtype: int
        """
        return self._inbox

    @inbox.setter
    def inbox(self, inbox):
        """Sets the inbox of this SubAccountUpdatePlanRequestFeatures.

        Number of inboxes  # noqa: E501

        :param inbox: The inbox of this SubAccountUpdatePlanRequestFeatures.  # noqa: E501
        :type: int
        """

        self._inbox = inbox

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
        if issubclass(SubAccountUpdatePlanRequestFeatures, dict):
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
        if not isinstance(other, SubAccountUpdatePlanRequestFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
