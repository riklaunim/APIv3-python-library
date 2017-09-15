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


class UpdateEmailCampaign(object):
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
        'tag': 'str',
        'sender': 'UpdateEmailCampaignSender',
        'name': 'str',
        'html_content': 'str',
        'html_url': 'str',
        'scheduled_at': 'str',
        'subject': 'str',
        'reply_to': 'str',
        'to_field': 'str',
        'recipients': 'UpdateEmailCampaignRecipients',
        'attachment_url': 'str',
        'inline_image_activation': 'bool',
        'mirror_active': 'bool',
        'recurring': 'bool',
        'footer': 'str',
        'header': 'str',
        'utm_campaign': 'str'
    }

    attribute_map = {
        'tag': 'tag',
        'sender': 'sender',
        'name': 'name',
        'html_content': 'htmlContent',
        'html_url': 'htmlUrl',
        'scheduled_at': 'scheduledAt',
        'subject': 'subject',
        'reply_to': 'replyTo',
        'to_field': 'toField',
        'recipients': 'recipients',
        'attachment_url': 'attachmentUrl',
        'inline_image_activation': 'inlineImageActivation',
        'mirror_active': 'mirrorActive',
        'recurring': 'recurring',
        'footer': 'footer',
        'header': 'header',
        'utm_campaign': 'utmCampaign'
    }

    def __init__(self, tag=None, sender=None, name=None, html_content=None, html_url=None, scheduled_at=None, subject=None, reply_to=None, to_field=None, recipients=None, attachment_url=None, inline_image_activation=False, mirror_active=None, recurring=False, footer=None, header=None, utm_campaign=None):
        """
        UpdateEmailCampaign - a model defined in Swagger
        """

        self._tag = None
        self._sender = None
        self._name = None
        self._html_content = None
        self._html_url = None
        self._scheduled_at = None
        self._subject = None
        self._reply_to = None
        self._to_field = None
        self._recipients = None
        self._attachment_url = None
        self._inline_image_activation = None
        self._mirror_active = None
        self._recurring = None
        self._footer = None
        self._header = None
        self._utm_campaign = None

        if tag is not None:
          self.tag = tag
        if sender is not None:
          self.sender = sender
        if name is not None:
          self.name = name
        if html_content is not None:
          self.html_content = html_content
        if html_url is not None:
          self.html_url = html_url
        if scheduled_at is not None:
          self.scheduled_at = scheduled_at
        if subject is not None:
          self.subject = subject
        if reply_to is not None:
          self.reply_to = reply_to
        if to_field is not None:
          self.to_field = to_field
        if recipients is not None:
          self.recipients = recipients
        if attachment_url is not None:
          self.attachment_url = attachment_url
        if inline_image_activation is not None:
          self.inline_image_activation = inline_image_activation
        if mirror_active is not None:
          self.mirror_active = mirror_active
        if recurring is not None:
          self.recurring = recurring
        if footer is not None:
          self.footer = footer
        if header is not None:
          self.header = header
        if utm_campaign is not None:
          self.utm_campaign = utm_campaign

    @property
    def tag(self):
        """
        Gets the tag of this UpdateEmailCampaign.
        Tag of the campaign

        :return: The tag of this UpdateEmailCampaign.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this UpdateEmailCampaign.
        Tag of the campaign

        :param tag: The tag of this UpdateEmailCampaign.
        :type: str
        """

        self._tag = tag

    @property
    def sender(self):
        """
        Gets the sender of this UpdateEmailCampaign.

        :return: The sender of this UpdateEmailCampaign.
        :rtype: UpdateEmailCampaignSender
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """
        Sets the sender of this UpdateEmailCampaign.

        :param sender: The sender of this UpdateEmailCampaign.
        :type: UpdateEmailCampaignSender
        """

        self._sender = sender

    @property
    def name(self):
        """
        Gets the name of this UpdateEmailCampaign.
        Name of the campaign

        :return: The name of this UpdateEmailCampaign.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateEmailCampaign.
        Name of the campaign

        :param name: The name of this UpdateEmailCampaign.
        :type: str
        """

        self._name = name

    @property
    def html_content(self):
        """
        Gets the html_content of this UpdateEmailCampaign.
        Body of the message (HTML version). REQUIRED if htmlUrl is empty

        :return: The html_content of this UpdateEmailCampaign.
        :rtype: str
        """
        return self._html_content

    @html_content.setter
    def html_content(self, html_content):
        """
        Sets the html_content of this UpdateEmailCampaign.
        Body of the message (HTML version). REQUIRED if htmlUrl is empty

        :param html_content: The html_content of this UpdateEmailCampaign.
        :type: str
        """

        self._html_content = html_content

    @property
    def html_url(self):
        """
        Gets the html_url of this UpdateEmailCampaign.
        Url which contents the body of the email message. REQUIRED if htmlContent is empty

        :return: The html_url of this UpdateEmailCampaign.
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """
        Sets the html_url of this UpdateEmailCampaign.
        Url which contents the body of the email message. REQUIRED if htmlContent is empty

        :param html_url: The html_url of this UpdateEmailCampaign.
        :type: str
        """

        self._html_url = html_url

    @property
    def scheduled_at(self):
        """
        Gets the scheduled_at of this UpdateEmailCampaign.
        Date and time on which the campaign has to run (YYYY-MM-DD HH:mm:ss)

        :return: The scheduled_at of this UpdateEmailCampaign.
        :rtype: str
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """
        Sets the scheduled_at of this UpdateEmailCampaign.
        Date and time on which the campaign has to run (YYYY-MM-DD HH:mm:ss)

        :param scheduled_at: The scheduled_at of this UpdateEmailCampaign.
        :type: str
        """
        if scheduled_at is not None and not re.search('^([1-9]\\d{3}-\\d{2}-\\d{2} [0-2]\\d:[0-5]\\d:[0-5]\\d)?$', scheduled_at):
            raise ValueError("Invalid value for `scheduled_at`, must be a follow pattern or equal to `/^([1-9]\\d{3}-\\d{2}-\\d{2} [0-2]\\d:[0-5]\\d:[0-5]\\d)?$/`")

        self._scheduled_at = scheduled_at

    @property
    def subject(self):
        """
        Gets the subject of this UpdateEmailCampaign.
        Subject of the campaign

        :return: The subject of this UpdateEmailCampaign.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this UpdateEmailCampaign.
        Subject of the campaign

        :param subject: The subject of this UpdateEmailCampaign.
        :type: str
        """

        self._subject = subject

    @property
    def reply_to(self):
        """
        Gets the reply_to of this UpdateEmailCampaign.
        Email on which campaign recipients will be able to reply to

        :return: The reply_to of this UpdateEmailCampaign.
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """
        Sets the reply_to of this UpdateEmailCampaign.
        Email on which campaign recipients will be able to reply to

        :param reply_to: The reply_to of this UpdateEmailCampaign.
        :type: str
        """

        self._reply_to = reply_to

    @property
    def to_field(self):
        """
        Gets the to_field of this UpdateEmailCampaign.
        This is to personalize the «To» Field. If you want to include the first name and last name of your recipient, add [FNAME] [LNAME]. To use the contact attributes here, these must already exist in SendinBlue account

        :return: The to_field of this UpdateEmailCampaign.
        :rtype: str
        """
        return self._to_field

    @to_field.setter
    def to_field(self, to_field):
        """
        Sets the to_field of this UpdateEmailCampaign.
        This is to personalize the «To» Field. If you want to include the first name and last name of your recipient, add [FNAME] [LNAME]. To use the contact attributes here, these must already exist in SendinBlue account

        :param to_field: The to_field of this UpdateEmailCampaign.
        :type: str
        """

        self._to_field = to_field

    @property
    def recipients(self):
        """
        Gets the recipients of this UpdateEmailCampaign.

        :return: The recipients of this UpdateEmailCampaign.
        :rtype: UpdateEmailCampaignRecipients
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """
        Sets the recipients of this UpdateEmailCampaign.

        :param recipients: The recipients of this UpdateEmailCampaign.
        :type: UpdateEmailCampaignRecipients
        """

        self._recipients = recipients

    @property
    def attachment_url(self):
        """
        Gets the attachment_url of this UpdateEmailCampaign.
        Absolute url of the attachment. Url not allowed from local machine. File must be hosted somewhere.Possilbe extension values are xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff and rtf

        :return: The attachment_url of this UpdateEmailCampaign.
        :rtype: str
        """
        return self._attachment_url

    @attachment_url.setter
    def attachment_url(self, attachment_url):
        """
        Sets the attachment_url of this UpdateEmailCampaign.
        Absolute url of the attachment. Url not allowed from local machine. File must be hosted somewhere.Possilbe extension values are xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff and rtf

        :param attachment_url: The attachment_url of this UpdateEmailCampaign.
        :type: str
        """

        self._attachment_url = attachment_url

    @property
    def inline_image_activation(self):
        """
        Gets the inline_image_activation of this UpdateEmailCampaign.
        Status of inline image. inlineImageActivation = false means image can’t be embedded, & inlineImageActivation = true means image can be embedded, in the email. You cannot send a campaign of more than 4MB with images embedded in the email. Campaigns with the images embedded in the email must be sent to less than 5000 contacts.

        :return: The inline_image_activation of this UpdateEmailCampaign.
        :rtype: bool
        """
        return self._inline_image_activation

    @inline_image_activation.setter
    def inline_image_activation(self, inline_image_activation):
        """
        Sets the inline_image_activation of this UpdateEmailCampaign.
        Status of inline image. inlineImageActivation = false means image can’t be embedded, & inlineImageActivation = true means image can be embedded, in the email. You cannot send a campaign of more than 4MB with images embedded in the email. Campaigns with the images embedded in the email must be sent to less than 5000 contacts.

        :param inline_image_activation: The inline_image_activation of this UpdateEmailCampaign.
        :type: bool
        """

        self._inline_image_activation = inline_image_activation

    @property
    def mirror_active(self):
        """
        Gets the mirror_active of this UpdateEmailCampaign.
        Status of mirror links in campaign. mirrorActive = false means mirror links are deactivated, & mirrorActive = true means mirror links are activated, in the campaign

        :return: The mirror_active of this UpdateEmailCampaign.
        :rtype: bool
        """
        return self._mirror_active

    @mirror_active.setter
    def mirror_active(self, mirror_active):
        """
        Sets the mirror_active of this UpdateEmailCampaign.
        Status of mirror links in campaign. mirrorActive = false means mirror links are deactivated, & mirrorActive = true means mirror links are activated, in the campaign

        :param mirror_active: The mirror_active of this UpdateEmailCampaign.
        :type: bool
        """

        self._mirror_active = mirror_active

    @property
    def recurring(self):
        """
        Gets the recurring of this UpdateEmailCampaign.
        FOR TRIGGER ONLY ! Type of trigger campaign.recurring = false means contact can receive the same Trigger campaign only once, & recurring = true means contact can receive the same Trigger campaign several times

        :return: The recurring of this UpdateEmailCampaign.
        :rtype: bool
        """
        return self._recurring

    @recurring.setter
    def recurring(self, recurring):
        """
        Sets the recurring of this UpdateEmailCampaign.
        FOR TRIGGER ONLY ! Type of trigger campaign.recurring = false means contact can receive the same Trigger campaign only once, & recurring = true means contact can receive the same Trigger campaign several times

        :param recurring: The recurring of this UpdateEmailCampaign.
        :type: bool
        """

        self._recurring = recurring

    @property
    def footer(self):
        """
        Gets the footer of this UpdateEmailCampaign.
        Footer of the email campaign

        :return: The footer of this UpdateEmailCampaign.
        :rtype: str
        """
        return self._footer

    @footer.setter
    def footer(self, footer):
        """
        Sets the footer of this UpdateEmailCampaign.
        Footer of the email campaign

        :param footer: The footer of this UpdateEmailCampaign.
        :type: str
        """

        self._footer = footer

    @property
    def header(self):
        """
        Gets the header of this UpdateEmailCampaign.
        Header of the email campaign

        :return: The header of this UpdateEmailCampaign.
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """
        Sets the header of this UpdateEmailCampaign.
        Header of the email campaign

        :param header: The header of this UpdateEmailCampaign.
        :type: str
        """

        self._header = header

    @property
    def utm_campaign(self):
        """
        Gets the utm_campaign of this UpdateEmailCampaign.
        Customize the utm_campaign value. If this field is empty, the campaign name will be used. Only alphanumeric characters and spaces are allowed

        :return: The utm_campaign of this UpdateEmailCampaign.
        :rtype: str
        """
        return self._utm_campaign

    @utm_campaign.setter
    def utm_campaign(self, utm_campaign):
        """
        Sets the utm_campaign of this UpdateEmailCampaign.
        Customize the utm_campaign value. If this field is empty, the campaign name will be used. Only alphanumeric characters and spaces are allowed

        :param utm_campaign: The utm_campaign of this UpdateEmailCampaign.
        :type: str
        """

        self._utm_campaign = utm_campaign

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
        if not isinstance(other, UpdateEmailCampaign):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
