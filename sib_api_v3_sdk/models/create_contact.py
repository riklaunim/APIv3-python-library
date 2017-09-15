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


class CreateContact(object):
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
        'email': 'str',
        'attributes': 'object',
        'email_blacklisted': 'bool',
        'sms_blacklisted': 'bool',
        'list_ids': 'list[int]'
    }

    attribute_map = {
        'email': 'email',
        'attributes': 'attributes',
        'email_blacklisted': 'emailBlacklisted',
        'sms_blacklisted': 'smsBlacklisted',
        'list_ids': 'listIds'
    }

    def __init__(self, email=None, attributes=None, email_blacklisted=None, sms_blacklisted=None, list_ids=None):
        """
        CreateContact - a model defined in Swagger
        """

        self._email = None
        self._attributes = None
        self._email_blacklisted = None
        self._sms_blacklisted = None
        self._list_ids = None

        if email is not None:
          self.email = email
        if attributes is not None:
          self.attributes = attributes
        if email_blacklisted is not None:
          self.email_blacklisted = email_blacklisted
        if sms_blacklisted is not None:
          self.sms_blacklisted = sms_blacklisted
        if list_ids is not None:
          self.list_ids = list_ids

    @property
    def email(self):
        """
        Gets the email of this CreateContact.
        Email address of the user. Mandatory if `attributes.sms` is not passed

        :return: The email of this CreateContact.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CreateContact.
        Email address of the user. Mandatory if `attributes.sms` is not passed

        :param email: The email of this CreateContact.
        :type: str
        """

        self._email = email

    @property
    def attributes(self):
        """
        Gets the attributes of this CreateContact.
        Values of the attributes to fill. The attributes must exist in you contact database

        :return: The attributes of this CreateContact.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this CreateContact.
        Values of the attributes to fill. The attributes must exist in you contact database

        :param attributes: The attributes of this CreateContact.
        :type: object
        """

        self._attributes = attributes

    @property
    def email_blacklisted(self):
        """
        Gets the email_blacklisted of this CreateContact.
        Blacklist the contact for emails (emailBlacklisted = true)

        :return: The email_blacklisted of this CreateContact.
        :rtype: bool
        """
        return self._email_blacklisted

    @email_blacklisted.setter
    def email_blacklisted(self, email_blacklisted):
        """
        Sets the email_blacklisted of this CreateContact.
        Blacklist the contact for emails (emailBlacklisted = true)

        :param email_blacklisted: The email_blacklisted of this CreateContact.
        :type: bool
        """

        self._email_blacklisted = email_blacklisted

    @property
    def sms_blacklisted(self):
        """
        Gets the sms_blacklisted of this CreateContact.
        Blacklist the contact for SMS (smsBlacklisted = true)

        :return: The sms_blacklisted of this CreateContact.
        :rtype: bool
        """
        return self._sms_blacklisted

    @sms_blacklisted.setter
    def sms_blacklisted(self, sms_blacklisted):
        """
        Sets the sms_blacklisted of this CreateContact.
        Blacklist the contact for SMS (smsBlacklisted = true)

        :param sms_blacklisted: The sms_blacklisted of this CreateContact.
        :type: bool
        """

        self._sms_blacklisted = sms_blacklisted

    @property
    def list_ids(self):
        """
        Gets the list_ids of this CreateContact.
        Ids of the lists to add the contact to

        :return: The list_ids of this CreateContact.
        :rtype: list[int]
        """
        return self._list_ids

    @list_ids.setter
    def list_ids(self, list_ids):
        """
        Sets the list_ids of this CreateContact.
        Ids of the lists to add the contact to

        :param list_ids: The list_ids of this CreateContact.
        :type: list[int]
        """

        self._list_ids = list_ids

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
        if not isinstance(other, CreateContact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
