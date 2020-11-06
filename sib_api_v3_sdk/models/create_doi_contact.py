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


class CreateDoiContact(object):
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
        'email': 'str',
        'attributes': 'object',
        'include_list_ids': 'list[int]',
        'exclude_list_ids': 'list[int]',
        'template_id': 'int',
        'redirection_url': 'str'
    }

    attribute_map = {
        'email': 'email',
        'attributes': 'attributes',
        'include_list_ids': 'includeListIds',
        'exclude_list_ids': 'excludeListIds',
        'template_id': 'templateId',
        'redirection_url': 'redirectionUrl'
    }

    def __init__(self, email=None, attributes=None, include_list_ids=None, exclude_list_ids=None, template_id=None, redirection_url=None):  # noqa: E501
        """CreateDoiContact - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._attributes = None
        self._include_list_ids = None
        self._exclude_list_ids = None
        self._template_id = None
        self._redirection_url = None
        self.discriminator = None

        self.email = email
        if attributes is not None:
            self.attributes = attributes
        self.include_list_ids = include_list_ids
        if exclude_list_ids is not None:
            self.exclude_list_ids = exclude_list_ids
        self.template_id = template_id
        self.redirection_url = redirection_url

    @property
    def email(self):
        """Gets the email of this CreateDoiContact.  # noqa: E501

        Email address where the confirmation email will be sent. This email address will be the identifier for all other contact attributes.  # noqa: E501

        :return: The email of this CreateDoiContact.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateDoiContact.

        Email address where the confirmation email will be sent. This email address will be the identifier for all other contact attributes.  # noqa: E501

        :param email: The email of this CreateDoiContact.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def attributes(self):
        """Gets the attributes of this CreateDoiContact.  # noqa: E501

        Pass the set of attributes and their values. These attributes must be present in your SendinBlue account. For eg. {'FNAME':'Elly', 'LNAME':'Roger'}  # noqa: E501

        :return: The attributes of this CreateDoiContact.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CreateDoiContact.

        Pass the set of attributes and their values. These attributes must be present in your SendinBlue account. For eg. {'FNAME':'Elly', 'LNAME':'Roger'}  # noqa: E501

        :param attributes: The attributes of this CreateDoiContact.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def include_list_ids(self):
        """Gets the include_list_ids of this CreateDoiContact.  # noqa: E501

        Lists under user account where contact should be added  # noqa: E501

        :return: The include_list_ids of this CreateDoiContact.  # noqa: E501
        :rtype: list[int]
        """
        return self._include_list_ids

    @include_list_ids.setter
    def include_list_ids(self, include_list_ids):
        """Sets the include_list_ids of this CreateDoiContact.

        Lists under user account where contact should be added  # noqa: E501

        :param include_list_ids: The include_list_ids of this CreateDoiContact.  # noqa: E501
        :type: list[int]
        """
        if include_list_ids is None:
            raise ValueError("Invalid value for `include_list_ids`, must not be `None`")  # noqa: E501

        self._include_list_ids = include_list_ids

    @property
    def exclude_list_ids(self):
        """Gets the exclude_list_ids of this CreateDoiContact.  # noqa: E501

        Lists under user account where contact should not be added  # noqa: E501

        :return: The exclude_list_ids of this CreateDoiContact.  # noqa: E501
        :rtype: list[int]
        """
        return self._exclude_list_ids

    @exclude_list_ids.setter
    def exclude_list_ids(self, exclude_list_ids):
        """Sets the exclude_list_ids of this CreateDoiContact.

        Lists under user account where contact should not be added  # noqa: E501

        :param exclude_list_ids: The exclude_list_ids of this CreateDoiContact.  # noqa: E501
        :type: list[int]
        """

        self._exclude_list_ids = exclude_list_ids

    @property
    def template_id(self):
        """Gets the template_id of this CreateDoiContact.  # noqa: E501

        Id of the Double opt-in (DOI) template  # noqa: E501

        :return: The template_id of this CreateDoiContact.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this CreateDoiContact.

        Id of the Double opt-in (DOI) template  # noqa: E501

        :param template_id: The template_id of this CreateDoiContact.  # noqa: E501
        :type: int
        """
        if template_id is None:
            raise ValueError("Invalid value for `template_id`, must not be `None`")  # noqa: E501

        self._template_id = template_id

    @property
    def redirection_url(self):
        """Gets the redirection_url of this CreateDoiContact.  # noqa: E501

        URL of the web page that user will be redirected to after clicking on the double opt in URL. When editing your DOI template you can reference this URL by using the tag {{ params.DOIurl }}.  # noqa: E501

        :return: The redirection_url of this CreateDoiContact.  # noqa: E501
        :rtype: str
        """
        return self._redirection_url

    @redirection_url.setter
    def redirection_url(self, redirection_url):
        """Sets the redirection_url of this CreateDoiContact.

        URL of the web page that user will be redirected to after clicking on the double opt in URL. When editing your DOI template you can reference this URL by using the tag {{ params.DOIurl }}.  # noqa: E501

        :param redirection_url: The redirection_url of this CreateDoiContact.  # noqa: E501
        :type: str
        """
        if redirection_url is None:
            raise ValueError("Invalid value for `redirection_url`, must not be `None`")  # noqa: E501

        self._redirection_url = redirection_url

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
        if issubclass(CreateDoiContact, dict):
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
        if not isinstance(other, CreateDoiContact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
