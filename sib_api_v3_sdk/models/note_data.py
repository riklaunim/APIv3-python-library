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


class NoteData(object):
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
        'text': 'str',
        'contact_ids': 'list[int]',
        'deal_ids': 'list[str]'
    }

    attribute_map = {
        'text': 'text',
        'contact_ids': 'contactIds',
        'deal_ids': 'dealIds'
    }

    def __init__(self, text=None, contact_ids=None, deal_ids=None):  # noqa: E501
        """NoteData - a model defined in Swagger"""  # noqa: E501

        self._text = None
        self._contact_ids = None
        self._deal_ids = None
        self.discriminator = None

        self.text = text
        if contact_ids is not None:
            self.contact_ids = contact_ids
        if deal_ids is not None:
            self.deal_ids = deal_ids

    @property
    def text(self):
        """Gets the text of this NoteData.  # noqa: E501

        Text content of a note  # noqa: E501

        :return: The text of this NoteData.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this NoteData.

        Text content of a note  # noqa: E501

        :param text: The text of this NoteData.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501
        if text is not None and len(text) > 3000:
            raise ValueError("Invalid value for `text`, length must be less than or equal to `3000`")  # noqa: E501
        if text is not None and len(text) < 1:
            raise ValueError("Invalid value for `text`, length must be greater than or equal to `1`")  # noqa: E501

        self._text = text

    @property
    def contact_ids(self):
        """Gets the contact_ids of this NoteData.  # noqa: E501

        Contact Ids linked to a note  # noqa: E501

        :return: The contact_ids of this NoteData.  # noqa: E501
        :rtype: list[int]
        """
        return self._contact_ids

    @contact_ids.setter
    def contact_ids(self, contact_ids):
        """Sets the contact_ids of this NoteData.

        Contact Ids linked to a note  # noqa: E501

        :param contact_ids: The contact_ids of this NoteData.  # noqa: E501
        :type: list[int]
        """

        self._contact_ids = contact_ids

    @property
    def deal_ids(self):
        """Gets the deal_ids of this NoteData.  # noqa: E501

        Deal Ids linked to a note  # noqa: E501

        :return: The deal_ids of this NoteData.  # noqa: E501
        :rtype: list[str]
        """
        return self._deal_ids

    @deal_ids.setter
    def deal_ids(self, deal_ids):
        """Sets the deal_ids of this NoteData.

        Deal Ids linked to a note  # noqa: E501

        :param deal_ids: The deal_ids of this NoteData.  # noqa: E501
        :type: list[str]
        """

        self._deal_ids = deal_ids

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
        if issubclass(NoteData, dict):
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
        if not isinstance(other, NoteData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
