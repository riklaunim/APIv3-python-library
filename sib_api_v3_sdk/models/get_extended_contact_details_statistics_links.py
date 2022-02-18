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


class GetExtendedContactDetailsStatisticsLinks(object):
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
        'event_time': 'str',
        'ip': 'str',
        'url': 'str'
    }

    attribute_map = {
        'count': 'count',
        'event_time': 'eventTime',
        'ip': 'ip',
        'url': 'url'
    }

    def __init__(self, count=None, event_time=None, ip=None, url=None):  # noqa: E501
        """GetExtendedContactDetailsStatisticsLinks - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._event_time = None
        self._ip = None
        self._url = None
        self.discriminator = None

        self.count = count
        self.event_time = event_time
        self.ip = ip
        self.url = url

    @property
    def count(self):
        """Gets the count of this GetExtendedContactDetailsStatisticsLinks.  # noqa: E501

        Number of clicks on this link for the campaign  # noqa: E501

        :return: The count of this GetExtendedContactDetailsStatisticsLinks.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this GetExtendedContactDetailsStatisticsLinks.

        Number of clicks on this link for the campaign  # noqa: E501

        :param count: The count of this GetExtendedContactDetailsStatisticsLinks.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def event_time(self):
        """Gets the event_time of this GetExtendedContactDetailsStatisticsLinks.  # noqa: E501

        UTC date-time of the event  # noqa: E501

        :return: The event_time of this GetExtendedContactDetailsStatisticsLinks.  # noqa: E501
        :rtype: str
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this GetExtendedContactDetailsStatisticsLinks.

        UTC date-time of the event  # noqa: E501

        :param event_time: The event_time of this GetExtendedContactDetailsStatisticsLinks.  # noqa: E501
        :type: str
        """
        if event_time is None:
            raise ValueError("Invalid value for `event_time`, must not be `None`")  # noqa: E501

        self._event_time = event_time

    @property
    def ip(self):
        """Gets the ip of this GetExtendedContactDetailsStatisticsLinks.  # noqa: E501

        IP from which the user has clicked on the link  # noqa: E501

        :return: The ip of this GetExtendedContactDetailsStatisticsLinks.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this GetExtendedContactDetailsStatisticsLinks.

        IP from which the user has clicked on the link  # noqa: E501

        :param ip: The ip of this GetExtendedContactDetailsStatisticsLinks.  # noqa: E501
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def url(self):
        """Gets the url of this GetExtendedContactDetailsStatisticsLinks.  # noqa: E501

        URL of the clicked link  # noqa: E501

        :return: The url of this GetExtendedContactDetailsStatisticsLinks.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GetExtendedContactDetailsStatisticsLinks.

        URL of the clicked link  # noqa: E501

        :param url: The url of this GetExtendedContactDetailsStatisticsLinks.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

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
        if issubclass(GetExtendedContactDetailsStatisticsLinks, dict):
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
        if not isinstance(other, GetExtendedContactDetailsStatisticsLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
