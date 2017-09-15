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


class SendTransacSms(object):
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
        'sender': 'str',
        'recipient': 'str',
        'content': 'str',
        'tag': 'str',
        'web_url': 'str'
    }

    attribute_map = {
        'sender': 'sender',
        'recipient': 'recipient',
        'content': 'content',
        'tag': 'tag',
        'web_url': 'webUrl'
    }

    def __init__(self, sender=None, recipient=None, content=None, tag=None, web_url=None):
        """
        SendTransacSms - a model defined in Swagger
        """

        self._sender = None
        self._recipient = None
        self._content = None
        self._tag = None
        self._web_url = None

        self.sender = sender
        self.recipient = recipient
        self.content = content
        if tag is not None:
          self.tag = tag
        if web_url is not None:
          self.web_url = web_url

    @property
    def sender(self):
        """
        Gets the sender of this SendTransacSms.
        Name of the sender. Only alphanumeric characters. No more than 11 characters

        :return: The sender of this SendTransacSms.
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """
        Sets the sender of this SendTransacSms.
        Name of the sender. Only alphanumeric characters. No more than 11 characters

        :param sender: The sender of this SendTransacSms.
        :type: str
        """
        if sender is None:
            raise ValueError("Invalid value for `sender`, must not be `None`")
        if sender is not None and len(sender) > 11:
            raise ValueError("Invalid value for `sender`, length must be less than or equal to `11`")

        self._sender = sender

    @property
    def recipient(self):
        """
        Gets the recipient of this SendTransacSms.
        Mobile number to send SMS with the country code

        :return: The recipient of this SendTransacSms.
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """
        Sets the recipient of this SendTransacSms.
        Mobile number to send SMS with the country code

        :param recipient: The recipient of this SendTransacSms.
        :type: str
        """
        if recipient is None:
            raise ValueError("Invalid value for `recipient`, must not be `None`")

        self._recipient = recipient

    @property
    def content(self):
        """
        Gets the content of this SendTransacSms.
        Content of the message. If more than 160 characters long, multiple text messages will be sent

        :return: The content of this SendTransacSms.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this SendTransacSms.
        Content of the message. If more than 160 characters long, multiple text messages will be sent

        :param content: The content of this SendTransacSms.
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")
        if content is not None and len(content) > 160:
            raise ValueError("Invalid value for `content`, length must be less than or equal to `160`")

        self._content = content

    @property
    def tag(self):
        """
        Gets the tag of this SendTransacSms.
        Tag of the message

        :return: The tag of this SendTransacSms.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this SendTransacSms.
        Tag of the message

        :param tag: The tag of this SendTransacSms.
        :type: str
        """

        self._tag = tag

    @property
    def web_url(self):
        """
        Gets the web_url of this SendTransacSms.
        Webhook to call for each event triggered by the message (delivered etc.)

        :return: The web_url of this SendTransacSms.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """
        Sets the web_url of this SendTransacSms.
        Webhook to call for each event triggered by the message (delivered etc.)

        :param web_url: The web_url of this SendTransacSms.
        :type: str
        """

        self._web_url = web_url

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
        if not isinstance(other, SendTransacSms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
