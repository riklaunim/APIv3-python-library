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


class Body1(object):
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
        'name': 'str',
        'duration': 'int',
        'task_type_id': 'str',
        '_date': 'datetime',
        'notes': 'str',
        'done': 'bool',
        'assign_to_id': 'str',
        'contacts_ids': 'list[int]',
        'deals_ids': 'list[str]',
        'companies_ids': 'list[str]',
        'reminder': 'TaskReminder'
    }

    attribute_map = {
        'name': 'name',
        'duration': 'duration',
        'task_type_id': 'taskTypeId',
        '_date': 'date',
        'notes': 'notes',
        'done': 'done',
        'assign_to_id': 'assignToId',
        'contacts_ids': 'contactsIds',
        'deals_ids': 'dealsIds',
        'companies_ids': 'companiesIds',
        'reminder': 'reminder'
    }

    def __init__(self, name=None, duration=None, task_type_id=None, _date=None, notes=None, done=None, assign_to_id=None, contacts_ids=None, deals_ids=None, companies_ids=None, reminder=None):  # noqa: E501
        """Body1 - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._duration = None
        self._task_type_id = None
        self.__date = None
        self._notes = None
        self._done = None
        self._assign_to_id = None
        self._contacts_ids = None
        self._deals_ids = None
        self._companies_ids = None
        self._reminder = None
        self.discriminator = None

        self.name = name
        if duration is not None:
            self.duration = duration
        self.task_type_id = task_type_id
        self._date = _date
        if notes is not None:
            self.notes = notes
        if done is not None:
            self.done = done
        if assign_to_id is not None:
            self.assign_to_id = assign_to_id
        if contacts_ids is not None:
            self.contacts_ids = contacts_ids
        if deals_ids is not None:
            self.deals_ids = deals_ids
        if companies_ids is not None:
            self.companies_ids = companies_ids
        if reminder is not None:
            self.reminder = reminder

    @property
    def name(self):
        """Gets the name of this Body1.  # noqa: E501

        Name of task  # noqa: E501

        :return: The name of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body1.

        Name of task  # noqa: E501

        :param name: The name of this Body1.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def duration(self):
        """Gets the duration of this Body1.  # noqa: E501

        Duration of task in milliseconds [1 minute = 60000 ms]  # noqa: E501

        :return: The duration of this Body1.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Body1.

        Duration of task in milliseconds [1 minute = 60000 ms]  # noqa: E501

        :param duration: The duration of this Body1.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def task_type_id(self):
        """Gets the task_type_id of this Body1.  # noqa: E501

        Id for type of task e.g Call / Email / Meeting etc.  # noqa: E501

        :return: The task_type_id of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._task_type_id

    @task_type_id.setter
    def task_type_id(self, task_type_id):
        """Sets the task_type_id of this Body1.

        Id for type of task e.g Call / Email / Meeting etc.  # noqa: E501

        :param task_type_id: The task_type_id of this Body1.  # noqa: E501
        :type: str
        """
        if task_type_id is None:
            raise ValueError("Invalid value for `task_type_id`, must not be `None`")  # noqa: E501

        self._task_type_id = task_type_id

    @property
    def _date(self):
        """Gets the _date of this Body1.  # noqa: E501

        Task date/time  # noqa: E501

        :return: The _date of this Body1.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Body1.

        Task date/time  # noqa: E501

        :param _date: The _date of this Body1.  # noqa: E501
        :type: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def notes(self):
        """Gets the notes of this Body1.  # noqa: E501

        Notes added to a task  # noqa: E501

        :return: The notes of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Body1.

        Notes added to a task  # noqa: E501

        :param notes: The notes of this Body1.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def done(self):
        """Gets the done of this Body1.  # noqa: E501

        Task marked as done  # noqa: E501

        :return: The done of this Body1.  # noqa: E501
        :rtype: bool
        """
        return self._done

    @done.setter
    def done(self, done):
        """Sets the done of this Body1.

        Task marked as done  # noqa: E501

        :param done: The done of this Body1.  # noqa: E501
        :type: bool
        """

        self._done = done

    @property
    def assign_to_id(self):
        """Gets the assign_to_id of this Body1.  # noqa: E501

        User id to whom task is assigned  # noqa: E501

        :return: The assign_to_id of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._assign_to_id

    @assign_to_id.setter
    def assign_to_id(self, assign_to_id):
        """Sets the assign_to_id of this Body1.

        User id to whom task is assigned  # noqa: E501

        :param assign_to_id: The assign_to_id of this Body1.  # noqa: E501
        :type: str
        """

        self._assign_to_id = assign_to_id

    @property
    def contacts_ids(self):
        """Gets the contacts_ids of this Body1.  # noqa: E501

        Contact ids for contacts linked to this task  # noqa: E501

        :return: The contacts_ids of this Body1.  # noqa: E501
        :rtype: list[int]
        """
        return self._contacts_ids

    @contacts_ids.setter
    def contacts_ids(self, contacts_ids):
        """Sets the contacts_ids of this Body1.

        Contact ids for contacts linked to this task  # noqa: E501

        :param contacts_ids: The contacts_ids of this Body1.  # noqa: E501
        :type: list[int]
        """

        self._contacts_ids = contacts_ids

    @property
    def deals_ids(self):
        """Gets the deals_ids of this Body1.  # noqa: E501

        Deal ids for deals a task is linked to  # noqa: E501

        :return: The deals_ids of this Body1.  # noqa: E501
        :rtype: list[str]
        """
        return self._deals_ids

    @deals_ids.setter
    def deals_ids(self, deals_ids):
        """Sets the deals_ids of this Body1.

        Deal ids for deals a task is linked to  # noqa: E501

        :param deals_ids: The deals_ids of this Body1.  # noqa: E501
        :type: list[str]
        """

        self._deals_ids = deals_ids

    @property
    def companies_ids(self):
        """Gets the companies_ids of this Body1.  # noqa: E501

        Companies ids for companies a task is linked to  # noqa: E501

        :return: The companies_ids of this Body1.  # noqa: E501
        :rtype: list[str]
        """
        return self._companies_ids

    @companies_ids.setter
    def companies_ids(self, companies_ids):
        """Sets the companies_ids of this Body1.

        Companies ids for companies a task is linked to  # noqa: E501

        :param companies_ids: The companies_ids of this Body1.  # noqa: E501
        :type: list[str]
        """

        self._companies_ids = companies_ids

    @property
    def reminder(self):
        """Gets the reminder of this Body1.  # noqa: E501


        :return: The reminder of this Body1.  # noqa: E501
        :rtype: TaskReminder
        """
        return self._reminder

    @reminder.setter
    def reminder(self, reminder):
        """Sets the reminder of this Body1.


        :param reminder: The reminder of this Body1.  # noqa: E501
        :type: TaskReminder
        """

        self._reminder = reminder

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
        if issubclass(Body1, dict):
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
        if not isinstance(other, Body1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
