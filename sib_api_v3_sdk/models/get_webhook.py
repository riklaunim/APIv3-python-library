# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  | 

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetWebhook(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'id': 'int',
        'description': 'str',
        'events': 'list[str]',
        'type': 'str',
        'created_at': 'str',
        'modified_at': 'str'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'description': 'description',
        'events': 'events',
        'type': 'type',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt'
    }

    def __init__(self, url=None, id=None, description=None, events=None, type=None, created_at=None, modified_at=None):
        """
        GetWebhook - a model defined in Swagger
        """

        self._url = None
        self._id = None
        self._description = None
        self._events = None
        self._type = None
        self._created_at = None
        self._modified_at = None

        self.url = url
        self.id = id
        self.description = description
        self.events = events
        self.type = type
        self.created_at = created_at
        self.modified_at = modified_at

    @property
    def url(self):
        """
        Gets the url of this GetWebhook.
        URL of the webhook

        :return: The url of this GetWebhook.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this GetWebhook.
        URL of the webhook

        :param url: The url of this GetWebhook.
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")

        self._url = url

    @property
    def id(self):
        """
        Gets the id of this GetWebhook.
        ID of the webhook

        :return: The id of this GetWebhook.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GetWebhook.
        ID of the webhook

        :param id: The id of this GetWebhook.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this GetWebhook.
        Description of the webhook

        :return: The description of this GetWebhook.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GetWebhook.
        Description of the webhook

        :param description: The description of this GetWebhook.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def events(self):
        """
        Gets the events of this GetWebhook.

        :return: The events of this GetWebhook.
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """
        Sets the events of this GetWebhook.

        :param events: The events of this GetWebhook.
        :type: list[str]
        """
        if events is None:
            raise ValueError("Invalid value for `events`, must not be `None`")

        self._events = events

    @property
    def type(self):
        """
        Gets the type of this GetWebhook.
        Type of webhook (marketing or transac)

        :return: The type of this GetWebhook.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this GetWebhook.
        Type of webhook (marketing or transac)

        :param type: The type of this GetWebhook.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = ["marketing", "transac"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def created_at(self):
        """
        Gets the created_at of this GetWebhook.
        Creation date of the webhook (YYYY-MM-DD)

        :return: The created_at of this GetWebhook.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this GetWebhook.
        Creation date of the webhook (YYYY-MM-DD)

        :param created_at: The created_at of this GetWebhook.
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")
        if created_at is not None and not re.search('^([1-9]\\d{3}-\\d{2}-\\d{2})?$', created_at):
            raise ValueError("Invalid value for `created_at`, must be a follow pattern or equal to `/^([1-9]\\d{3}-\\d{2}-\\d{2})?$/`")

        self._created_at = created_at

    @property
    def modified_at(self):
        """
        Gets the modified_at of this GetWebhook.
        Last modification date of the webhook (YYYY-MM-DD)

        :return: The modified_at of this GetWebhook.
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """
        Sets the modified_at of this GetWebhook.
        Last modification date of the webhook (YYYY-MM-DD)

        :param modified_at: The modified_at of this GetWebhook.
        :type: str
        """
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")
        if modified_at is not None and not re.search('^([1-9]\\d{3}-\\d{2}-\\d{2})?$', modified_at):
            raise ValueError("Invalid value for `modified_at`, must be a follow pattern or equal to `/^([1-9]\\d{3}-\\d{2}-\\d{2})?$/`")

        self._modified_at = modified_at

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, GetWebhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
