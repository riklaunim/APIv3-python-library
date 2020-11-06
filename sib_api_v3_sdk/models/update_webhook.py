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


class UpdateWebhook(object):
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
        'url': 'str',
        'description': 'str',
        'events': 'list[str]'
    }

    attribute_map = {
        'url': 'url',
        'description': 'description',
        'events': 'events'
    }

    def __init__(self, url=None, description=None, events=None):  # noqa: E501
        """UpdateWebhook - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._description = None
        self._events = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if description is not None:
            self.description = description
        if events is not None:
            self.events = events

    @property
    def url(self):
        """Gets the url of this UpdateWebhook.  # noqa: E501

        URL of the webhook  # noqa: E501

        :return: The url of this UpdateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UpdateWebhook.

        URL of the webhook  # noqa: E501

        :param url: The url of this UpdateWebhook.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def description(self):
        """Gets the description of this UpdateWebhook.  # noqa: E501

        Description of the webhook  # noqa: E501

        :return: The description of this UpdateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateWebhook.

        Description of the webhook  # noqa: E501

        :param description: The description of this UpdateWebhook.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def events(self):
        """Gets the events of this UpdateWebhook.  # noqa: E501

        Events triggering the webhook. Possible values for Transactional type webhook – `sent` OR `request`, `delivered`, `hardBounce`, `softBounce`, `blocked`, `spam`, `invalid`, `deferred`, `click`, `opened`, `uniqueOpened` and `unsubscribed` and possible values for Marketing type webhook – `spam`, `opened`, `click`, `hardBounce`, `softBounce`, `unsubscribed`, `listAddition` and `delivered`  # noqa: E501

        :return: The events of this UpdateWebhook.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this UpdateWebhook.

        Events triggering the webhook. Possible values for Transactional type webhook – `sent` OR `request`, `delivered`, `hardBounce`, `softBounce`, `blocked`, `spam`, `invalid`, `deferred`, `click`, `opened`, `uniqueOpened` and `unsubscribed` and possible values for Marketing type webhook – `spam`, `opened`, `click`, `hardBounce`, `softBounce`, `unsubscribed`, `listAddition` and `delivered`  # noqa: E501

        :param events: The events of this UpdateWebhook.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["hardBounce", "softBounce", "blocked", "spam", "delivered", "request", "click", "invalid", "deferred", "opened", "uniqueOpened", "unsubscribed", "listAddition", "contactUpdated", "contactDeleted"]  # noqa: E501
        if not set(events).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `events` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(events) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._events = events

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
        if issubclass(UpdateWebhook, dict):
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
        if not isinstance(other, UpdateWebhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
