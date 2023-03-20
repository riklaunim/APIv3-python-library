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


class Company(object):
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
        'id': 'str',
        'attributes': 'object',
        'linked_contacts_ids': 'list[int]',
        'linked_deals_ids': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'attributes': 'attributes',
        'linked_contacts_ids': 'linkedContactsIds',
        'linked_deals_ids': 'linkedDealsIds'
    }

    def __init__(self, id=None, attributes=None, linked_contacts_ids=None, linked_deals_ids=None):  # noqa: E501
        """Company - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._attributes = None
        self._linked_contacts_ids = None
        self._linked_deals_ids = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if attributes is not None:
            self.attributes = attributes
        if linked_contacts_ids is not None:
            self.linked_contacts_ids = linked_contacts_ids
        if linked_deals_ids is not None:
            self.linked_deals_ids = linked_deals_ids

    @property
    def id(self):
        """Gets the id of this Company.  # noqa: E501

        Unique company id  # noqa: E501

        :return: The id of this Company.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Company.

        Unique company id  # noqa: E501

        :param id: The id of this Company.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def attributes(self):
        """Gets the attributes of this Company.  # noqa: E501

        Company attributes with values  # noqa: E501

        :return: The attributes of this Company.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Company.

        Company attributes with values  # noqa: E501

        :param attributes: The attributes of this Company.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def linked_contacts_ids(self):
        """Gets the linked_contacts_ids of this Company.  # noqa: E501

        Contact ids for contacts linked to this company  # noqa: E501

        :return: The linked_contacts_ids of this Company.  # noqa: E501
        :rtype: list[int]
        """
        return self._linked_contacts_ids

    @linked_contacts_ids.setter
    def linked_contacts_ids(self, linked_contacts_ids):
        """Sets the linked_contacts_ids of this Company.

        Contact ids for contacts linked to this company  # noqa: E501

        :param linked_contacts_ids: The linked_contacts_ids of this Company.  # noqa: E501
        :type: list[int]
        """

        self._linked_contacts_ids = linked_contacts_ids

    @property
    def linked_deals_ids(self):
        """Gets the linked_deals_ids of this Company.  # noqa: E501

        Deals ids for companies linked to this company  # noqa: E501

        :return: The linked_deals_ids of this Company.  # noqa: E501
        :rtype: list[str]
        """
        return self._linked_deals_ids

    @linked_deals_ids.setter
    def linked_deals_ids(self, linked_deals_ids):
        """Sets the linked_deals_ids of this Company.

        Deals ids for companies linked to this company  # noqa: E501

        :param linked_deals_ids: The linked_deals_ids of this Company.  # noqa: E501
        :type: list[str]
        """

        self._linked_deals_ids = linked_deals_ids

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
        if issubclass(Company, dict):
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
        if not isinstance(other, Company):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
