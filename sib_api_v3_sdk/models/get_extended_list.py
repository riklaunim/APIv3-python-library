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


class GetExtendedList(object):
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
        'id': 'int',
        'name': 'str',
        'total_blacklisted': 'int',
        'total_subscribers': 'int',
        'unique_subscribers': 'int',
        'folder_id': 'int',
        'created_at': 'datetime',
        'campaign_stats': 'list[GetExtendedListCampaignStats]',
        'dynamic_list': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'total_blacklisted': 'totalBlacklisted',
        'total_subscribers': 'totalSubscribers',
        'unique_subscribers': 'uniqueSubscribers',
        'folder_id': 'folderId',
        'created_at': 'createdAt',
        'campaign_stats': 'campaignStats',
        'dynamic_list': 'dynamicList'
    }

    def __init__(self, id=None, name=None, total_blacklisted=None, total_subscribers=None, unique_subscribers=None, folder_id=None, created_at=None, campaign_stats=None, dynamic_list=None):  # noqa: E501
        """GetExtendedList - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._total_blacklisted = None
        self._total_subscribers = None
        self._unique_subscribers = None
        self._folder_id = None
        self._created_at = None
        self._campaign_stats = None
        self._dynamic_list = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.total_blacklisted = total_blacklisted
        self.total_subscribers = total_subscribers
        self.unique_subscribers = unique_subscribers
        self.folder_id = folder_id
        self.created_at = created_at
        if campaign_stats is not None:
            self.campaign_stats = campaign_stats
        if dynamic_list is not None:
            self.dynamic_list = dynamic_list

    @property
    def id(self):
        """Gets the id of this GetExtendedList.  # noqa: E501

        ID of the list  # noqa: E501

        :return: The id of this GetExtendedList.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetExtendedList.

        ID of the list  # noqa: E501

        :param id: The id of this GetExtendedList.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetExtendedList.  # noqa: E501

        Name of the list  # noqa: E501

        :return: The name of this GetExtendedList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetExtendedList.

        Name of the list  # noqa: E501

        :param name: The name of this GetExtendedList.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def total_blacklisted(self):
        """Gets the total_blacklisted of this GetExtendedList.  # noqa: E501

        Number of blacklisted contacts in the list  # noqa: E501

        :return: The total_blacklisted of this GetExtendedList.  # noqa: E501
        :rtype: int
        """
        return self._total_blacklisted

    @total_blacklisted.setter
    def total_blacklisted(self, total_blacklisted):
        """Sets the total_blacklisted of this GetExtendedList.

        Number of blacklisted contacts in the list  # noqa: E501

        :param total_blacklisted: The total_blacklisted of this GetExtendedList.  # noqa: E501
        :type: int
        """
        if total_blacklisted is None:
            raise ValueError("Invalid value for `total_blacklisted`, must not be `None`")  # noqa: E501

        self._total_blacklisted = total_blacklisted

    @property
    def total_subscribers(self):
        """Gets the total_subscribers of this GetExtendedList.  # noqa: E501

        Number of contacts in the list  # noqa: E501

        :return: The total_subscribers of this GetExtendedList.  # noqa: E501
        :rtype: int
        """
        return self._total_subscribers

    @total_subscribers.setter
    def total_subscribers(self, total_subscribers):
        """Sets the total_subscribers of this GetExtendedList.

        Number of contacts in the list  # noqa: E501

        :param total_subscribers: The total_subscribers of this GetExtendedList.  # noqa: E501
        :type: int
        """
        if total_subscribers is None:
            raise ValueError("Invalid value for `total_subscribers`, must not be `None`")  # noqa: E501

        self._total_subscribers = total_subscribers

    @property
    def unique_subscribers(self):
        """Gets the unique_subscribers of this GetExtendedList.  # noqa: E501

        Number of unique contacts in the list  # noqa: E501

        :return: The unique_subscribers of this GetExtendedList.  # noqa: E501
        :rtype: int
        """
        return self._unique_subscribers

    @unique_subscribers.setter
    def unique_subscribers(self, unique_subscribers):
        """Sets the unique_subscribers of this GetExtendedList.

        Number of unique contacts in the list  # noqa: E501

        :param unique_subscribers: The unique_subscribers of this GetExtendedList.  # noqa: E501
        :type: int
        """
        if unique_subscribers is None:
            raise ValueError("Invalid value for `unique_subscribers`, must not be `None`")  # noqa: E501

        self._unique_subscribers = unique_subscribers

    @property
    def folder_id(self):
        """Gets the folder_id of this GetExtendedList.  # noqa: E501

        ID of the folder  # noqa: E501

        :return: The folder_id of this GetExtendedList.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this GetExtendedList.

        ID of the folder  # noqa: E501

        :param folder_id: The folder_id of this GetExtendedList.  # noqa: E501
        :type: int
        """
        if folder_id is None:
            raise ValueError("Invalid value for `folder_id`, must not be `None`")  # noqa: E501

        self._folder_id = folder_id

    @property
    def created_at(self):
        """Gets the created_at of this GetExtendedList.  # noqa: E501

        Creation UTC date-time of the list (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :return: The created_at of this GetExtendedList.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetExtendedList.

        Creation UTC date-time of the list (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :param created_at: The created_at of this GetExtendedList.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def campaign_stats(self):
        """Gets the campaign_stats of this GetExtendedList.  # noqa: E501


        :return: The campaign_stats of this GetExtendedList.  # noqa: E501
        :rtype: list[GetExtendedListCampaignStats]
        """
        return self._campaign_stats

    @campaign_stats.setter
    def campaign_stats(self, campaign_stats):
        """Sets the campaign_stats of this GetExtendedList.


        :param campaign_stats: The campaign_stats of this GetExtendedList.  # noqa: E501
        :type: list[GetExtendedListCampaignStats]
        """

        self._campaign_stats = campaign_stats

    @property
    def dynamic_list(self):
        """Gets the dynamic_list of this GetExtendedList.  # noqa: E501

        Status telling if the list is dynamic or not (true=dynamic, false=not dynamic)  # noqa: E501

        :return: The dynamic_list of this GetExtendedList.  # noqa: E501
        :rtype: bool
        """
        return self._dynamic_list

    @dynamic_list.setter
    def dynamic_list(self, dynamic_list):
        """Sets the dynamic_list of this GetExtendedList.

        Status telling if the list is dynamic or not (true=dynamic, false=not dynamic)  # noqa: E501

        :param dynamic_list: The dynamic_list of this GetExtendedList.  # noqa: E501
        :type: bool
        """

        self._dynamic_list = dynamic_list

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
        if issubclass(GetExtendedList, dict):
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
        if not isinstance(other, GetExtendedList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
