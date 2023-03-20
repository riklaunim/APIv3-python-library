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


class SendWhatsappMessage(object):
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
        'template_id': 'int',
        'text': 'str',
        'sender_number': 'str',
        'contact_numbers': 'list[str]'
    }

    attribute_map = {
        'template_id': 'templateId',
        'text': 'text',
        'sender_number': 'senderNumber',
        'contact_numbers': 'contactNumbers'
    }

    def __init__(self, template_id=None, text=None, sender_number=None, contact_numbers=None):  # noqa: E501
        """SendWhatsappMessage - a model defined in Swagger"""  # noqa: E501

        self._template_id = None
        self._text = None
        self._sender_number = None
        self._contact_numbers = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if text is not None:
            self.text = text
        self.sender_number = sender_number
        self.contact_numbers = contact_numbers

    @property
    def template_id(self):
        """Gets the template_id of this SendWhatsappMessage.  # noqa: E501

        ID of the template to send  # noqa: E501

        :return: The template_id of this SendWhatsappMessage.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this SendWhatsappMessage.

        ID of the template to send  # noqa: E501

        :param template_id: The template_id of this SendWhatsappMessage.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

    @property
    def text(self):
        """Gets the text of this SendWhatsappMessage.  # noqa: E501

        Text to be sent as message body (will be overridden if templateId is passed in the same request)  # noqa: E501

        :return: The text of this SendWhatsappMessage.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SendWhatsappMessage.

        Text to be sent as message body (will be overridden if templateId is passed in the same request)  # noqa: E501

        :param text: The text of this SendWhatsappMessage.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def sender_number(self):
        """Gets the sender_number of this SendWhatsappMessage.  # noqa: E501

        WhatsApp Number with country code. Example, 85264318721  # noqa: E501

        :return: The sender_number of this SendWhatsappMessage.  # noqa: E501
        :rtype: str
        """
        return self._sender_number

    @sender_number.setter
    def sender_number(self, sender_number):
        """Sets the sender_number of this SendWhatsappMessage.

        WhatsApp Number with country code. Example, 85264318721  # noqa: E501

        :param sender_number: The sender_number of this SendWhatsappMessage.  # noqa: E501
        :type: str
        """
        if sender_number is None:
            raise ValueError("Invalid value for `sender_number`, must not be `None`")  # noqa: E501

        self._sender_number = sender_number

    @property
    def contact_numbers(self):
        """Gets the contact_numbers of this SendWhatsappMessage.  # noqa: E501

        List of phone numbers of the contacts  # noqa: E501

        :return: The contact_numbers of this SendWhatsappMessage.  # noqa: E501
        :rtype: list[str]
        """
        return self._contact_numbers

    @contact_numbers.setter
    def contact_numbers(self, contact_numbers):
        """Sets the contact_numbers of this SendWhatsappMessage.

        List of phone numbers of the contacts  # noqa: E501

        :param contact_numbers: The contact_numbers of this SendWhatsappMessage.  # noqa: E501
        :type: list[str]
        """
        if contact_numbers is None:
            raise ValueError("Invalid value for `contact_numbers`, must not be `None`")  # noqa: E501

        self._contact_numbers = contact_numbers

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
        if issubclass(SendWhatsappMessage, dict):
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
        if not isinstance(other, SendWhatsappMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
