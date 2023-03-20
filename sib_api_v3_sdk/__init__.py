# coding: utf-8

# flake8: noqa

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from sib_api_v3_sdk.api.account_api import AccountApi
from sib_api_v3_sdk.api.companies_api import CompaniesApi
from sib_api_v3_sdk.api.contacts_api import ContactsApi
from sib_api_v3_sdk.api.conversations_api import ConversationsApi
from sib_api_v3_sdk.api.deals_api import DealsApi
from sib_api_v3_sdk.api.ecommerce_api import EcommerceApi
from sib_api_v3_sdk.api.email_campaigns_api import EmailCampaignsApi
from sib_api_v3_sdk.api.external_feeds_api import ExternalFeedsApi
from sib_api_v3_sdk.api.files_api import FilesApi
from sib_api_v3_sdk.api.inbound_parsing_api import InboundParsingApi
from sib_api_v3_sdk.api.master_account_api import MasterAccountApi
from sib_api_v3_sdk.api.notes_api import NotesApi
from sib_api_v3_sdk.api.process_api import ProcessApi
from sib_api_v3_sdk.api.reseller_api import ResellerApi
from sib_api_v3_sdk.api.sms_campaigns_api import SMSCampaignsApi
from sib_api_v3_sdk.api.senders_api import SendersApi
from sib_api_v3_sdk.api.tasks_api import TasksApi
from sib_api_v3_sdk.api.transactional_sms_api import TransactionalSMSApi
from sib_api_v3_sdk.api.transactional_whats_app_api import TransactionalWhatsAppApi
from sib_api_v3_sdk.api.transactional_emails_api import TransactionalEmailsApi
from sib_api_v3_sdk.api.webhooks_api import WebhooksApi
from sib_api_v3_sdk.api.whatsapp_campaigns_api import WhatsappCampaignsApi

# import ApiClient
from sib_api_v3_sdk.api_client import ApiClient
from sib_api_v3_sdk.configuration import Configuration
# import models into sdk package
from sib_api_v3_sdk.models.ab_test_campaign_result import AbTestCampaignResult
from sib_api_v3_sdk.models.ab_test_campaign_result_clicked_links import AbTestCampaignResultClickedLinks
from sib_api_v3_sdk.models.ab_test_campaign_result_statistics import AbTestCampaignResultStatistics
from sib_api_v3_sdk.models.ab_test_version_clicks import AbTestVersionClicks
from sib_api_v3_sdk.models.ab_test_version_clicks_inner import AbTestVersionClicksInner
from sib_api_v3_sdk.models.ab_test_version_stats import AbTestVersionStats
from sib_api_v3_sdk.models.add_child_domain import AddChildDomain
from sib_api_v3_sdk.models.add_contact_to_list import AddContactToList
from sib_api_v3_sdk.models.add_credits import AddCredits
from sib_api_v3_sdk.models.block_domain import BlockDomain
from sib_api_v3_sdk.models.body import Body
from sib_api_v3_sdk.models.body1 import Body1
from sib_api_v3_sdk.models.body10 import Body10
from sib_api_v3_sdk.models.body11 import Body11
from sib_api_v3_sdk.models.body12 import Body12
from sib_api_v3_sdk.models.body2 import Body2
from sib_api_v3_sdk.models.body3 import Body3
from sib_api_v3_sdk.models.body4 import Body4
from sib_api_v3_sdk.models.body5 import Body5
from sib_api_v3_sdk.models.body6 import Body6
from sib_api_v3_sdk.models.body7 import Body7
from sib_api_v3_sdk.models.body8 import Body8
from sib_api_v3_sdk.models.body9 import Body9
from sib_api_v3_sdk.models.body_variables_items import BodyVariablesItems
from sib_api_v3_sdk.models.companies_list import CompaniesList
from sib_api_v3_sdk.models.company import Company
from sib_api_v3_sdk.models.company_attributes import CompanyAttributes
from sib_api_v3_sdk.models.company_attributes_inner import CompanyAttributesInner
from sib_api_v3_sdk.models.component_items import ComponentItems
from sib_api_v3_sdk.models.conversations_message import ConversationsMessage
from sib_api_v3_sdk.models.conversations_message_file import ConversationsMessageFile
from sib_api_v3_sdk.models.conversations_message_file_image_info import ConversationsMessageFileImageInfo
from sib_api_v3_sdk.models.create_api_key_request import CreateApiKeyRequest
from sib_api_v3_sdk.models.create_api_key_response import CreateApiKeyResponse
from sib_api_v3_sdk.models.create_attribute import CreateAttribute
from sib_api_v3_sdk.models.create_attribute_enumeration import CreateAttributeEnumeration
from sib_api_v3_sdk.models.create_category_model import CreateCategoryModel
from sib_api_v3_sdk.models.create_child import CreateChild
from sib_api_v3_sdk.models.create_contact import CreateContact
from sib_api_v3_sdk.models.create_doi_contact import CreateDoiContact
from sib_api_v3_sdk.models.create_email_campaign import CreateEmailCampaign
from sib_api_v3_sdk.models.create_email_campaign_recipients import CreateEmailCampaignRecipients
from sib_api_v3_sdk.models.create_email_campaign_sender import CreateEmailCampaignSender
from sib_api_v3_sdk.models.create_external_feed import CreateExternalFeed
from sib_api_v3_sdk.models.create_list import CreateList
from sib_api_v3_sdk.models.create_model import CreateModel
from sib_api_v3_sdk.models.create_product_model import CreateProductModel
from sib_api_v3_sdk.models.create_reseller import CreateReseller
from sib_api_v3_sdk.models.create_sender import CreateSender
from sib_api_v3_sdk.models.create_sender_ips import CreateSenderIps
from sib_api_v3_sdk.models.create_sender_model import CreateSenderModel
from sib_api_v3_sdk.models.create_sms_campaign import CreateSmsCampaign
from sib_api_v3_sdk.models.create_sms_campaign_recipients import CreateSmsCampaignRecipients
from sib_api_v3_sdk.models.create_smtp_email import CreateSmtpEmail
from sib_api_v3_sdk.models.create_smtp_template import CreateSmtpTemplate
from sib_api_v3_sdk.models.create_smtp_template_sender import CreateSmtpTemplateSender
from sib_api_v3_sdk.models.create_sub_account import CreateSubAccount
from sib_api_v3_sdk.models.create_sub_account_response import CreateSubAccountResponse
from sib_api_v3_sdk.models.create_update_batch_category import CreateUpdateBatchCategory
from sib_api_v3_sdk.models.create_update_batch_category_model import CreateUpdateBatchCategoryModel
from sib_api_v3_sdk.models.create_update_batch_products import CreateUpdateBatchProducts
from sib_api_v3_sdk.models.create_update_batch_products_model import CreateUpdateBatchProductsModel
from sib_api_v3_sdk.models.create_update_categories import CreateUpdateCategories
from sib_api_v3_sdk.models.create_update_category import CreateUpdateCategory
from sib_api_v3_sdk.models.create_update_contact_model import CreateUpdateContactModel
from sib_api_v3_sdk.models.create_update_folder import CreateUpdateFolder
from sib_api_v3_sdk.models.create_update_product import CreateUpdateProduct
from sib_api_v3_sdk.models.create_update_products import CreateUpdateProducts
from sib_api_v3_sdk.models.create_webhook import CreateWebhook
from sib_api_v3_sdk.models.created_batch_id import CreatedBatchId
from sib_api_v3_sdk.models.created_process_id import CreatedProcessId
from sib_api_v3_sdk.models.deal import Deal
from sib_api_v3_sdk.models.deal_attributes import DealAttributes
from sib_api_v3_sdk.models.deal_attributes_inner import DealAttributesInner
from sib_api_v3_sdk.models.deals_list import DealsList
from sib_api_v3_sdk.models.delete_hardbounces import DeleteHardbounces
from sib_api_v3_sdk.models.email_export_recipients import EmailExportRecipients
from sib_api_v3_sdk.models.error_model import ErrorModel
from sib_api_v3_sdk.models.file_data import FileData
from sib_api_v3_sdk.models.file_downloadable_link import FileDownloadableLink
from sib_api_v3_sdk.models.file_list import FileList
from sib_api_v3_sdk.models.get_account_marketing_automation import GetAccountMarketingAutomation
from sib_api_v3_sdk.models.get_account_plan import GetAccountPlan
from sib_api_v3_sdk.models.get_account_relay import GetAccountRelay
from sib_api_v3_sdk.models.get_account_relay_data import GetAccountRelayData
from sib_api_v3_sdk.models.get_aggregated_report import GetAggregatedReport
from sib_api_v3_sdk.models.get_all_external_feeds import GetAllExternalFeeds
from sib_api_v3_sdk.models.get_all_external_feeds_feeds import GetAllExternalFeedsFeeds
from sib_api_v3_sdk.models.get_attributes import GetAttributes
from sib_api_v3_sdk.models.get_attributes_attributes import GetAttributesAttributes
from sib_api_v3_sdk.models.get_attributes_enumeration import GetAttributesEnumeration
from sib_api_v3_sdk.models.get_blocked_domains import GetBlockedDomains
from sib_api_v3_sdk.models.get_campaign_overview import GetCampaignOverview
from sib_api_v3_sdk.models.get_campaign_recipients import GetCampaignRecipients
from sib_api_v3_sdk.models.get_campaign_stats import GetCampaignStats
from sib_api_v3_sdk.models.get_categories import GetCategories
from sib_api_v3_sdk.models.get_category_details import GetCategoryDetails
from sib_api_v3_sdk.models.get_child_account_creation_status import GetChildAccountCreationStatus
from sib_api_v3_sdk.models.get_child_domain import GetChildDomain
from sib_api_v3_sdk.models.get_child_domains import GetChildDomains
from sib_api_v3_sdk.models.get_child_info_api_keys import GetChildInfoApiKeys
from sib_api_v3_sdk.models.get_child_info_api_keys_v2 import GetChildInfoApiKeysV2
from sib_api_v3_sdk.models.get_child_info_api_keys_v3 import GetChildInfoApiKeysV3
from sib_api_v3_sdk.models.get_child_info_credits import GetChildInfoCredits
from sib_api_v3_sdk.models.get_child_info_statistics import GetChildInfoStatistics
from sib_api_v3_sdk.models.get_children_list import GetChildrenList
from sib_api_v3_sdk.models.get_client import GetClient
from sib_api_v3_sdk.models.get_contact_campaign_stats import GetContactCampaignStats
from sib_api_v3_sdk.models.get_contact_campaign_stats_clicked import GetContactCampaignStatsClicked
from sib_api_v3_sdk.models.get_contact_campaign_stats_opened import GetContactCampaignStatsOpened
from sib_api_v3_sdk.models.get_contact_campaign_stats_transac_attributes import GetContactCampaignStatsTransacAttributes
from sib_api_v3_sdk.models.get_contact_campaign_stats_unsubscriptions import GetContactCampaignStatsUnsubscriptions
from sib_api_v3_sdk.models.get_contact_details import GetContactDetails
from sib_api_v3_sdk.models.get_contacts import GetContacts
from sib_api_v3_sdk.models.get_device_browser_stats import GetDeviceBrowserStats
from sib_api_v3_sdk.models.get_email_campaigns import GetEmailCampaigns
from sib_api_v3_sdk.models.get_email_event_report import GetEmailEventReport
from sib_api_v3_sdk.models.get_email_event_report_events import GetEmailEventReportEvents
from sib_api_v3_sdk.models.get_extended_campaign_overview_sender import GetExtendedCampaignOverviewSender
from sib_api_v3_sdk.models.get_extended_campaign_stats import GetExtendedCampaignStats
from sib_api_v3_sdk.models.get_extended_client_address import GetExtendedClientAddress
from sib_api_v3_sdk.models.get_extended_contact_details_statistics import GetExtendedContactDetailsStatistics
from sib_api_v3_sdk.models.get_extended_contact_details_statistics_clicked import GetExtendedContactDetailsStatisticsClicked
from sib_api_v3_sdk.models.get_extended_contact_details_statistics_delivered import GetExtendedContactDetailsStatisticsDelivered
from sib_api_v3_sdk.models.get_extended_contact_details_statistics_links import GetExtendedContactDetailsStatisticsLinks
from sib_api_v3_sdk.models.get_extended_contact_details_statistics_messages_sent import GetExtendedContactDetailsStatisticsMessagesSent
from sib_api_v3_sdk.models.get_extended_contact_details_statistics_opened import GetExtendedContactDetailsStatisticsOpened
from sib_api_v3_sdk.models.get_extended_contact_details_statistics_unsubscriptions import GetExtendedContactDetailsStatisticsUnsubscriptions
from sib_api_v3_sdk.models.get_extended_contact_details_statistics_unsubscriptions_admin_unsubscription import GetExtendedContactDetailsStatisticsUnsubscriptionsAdminUnsubscription
from sib_api_v3_sdk.models.get_extended_contact_details_statistics_unsubscriptions_user_unsubscription import GetExtendedContactDetailsStatisticsUnsubscriptionsUserUnsubscription
from sib_api_v3_sdk.models.get_extended_list_campaign_stats import GetExtendedListCampaignStats
from sib_api_v3_sdk.models.get_external_feed_by_uuid import GetExternalFeedByUUID
from sib_api_v3_sdk.models.get_external_feed_by_uuid_headers import GetExternalFeedByUUIDHeaders
from sib_api_v3_sdk.models.get_folder import GetFolder
from sib_api_v3_sdk.models.get_folder_lists import GetFolderLists
from sib_api_v3_sdk.models.get_folders import GetFolders
from sib_api_v3_sdk.models.get_inbound_email_events import GetInboundEmailEvents
from sib_api_v3_sdk.models.get_inbound_email_events_by_uuid import GetInboundEmailEventsByUuid
from sib_api_v3_sdk.models.get_inbound_email_events_by_uuid_attachments import GetInboundEmailEventsByUuidAttachments
from sib_api_v3_sdk.models.get_inbound_email_events_by_uuid_logs import GetInboundEmailEventsByUuidLogs
from sib_api_v3_sdk.models.get_inbound_email_events_events import GetInboundEmailEventsEvents
from sib_api_v3_sdk.models.get_ip import GetIp
from sib_api_v3_sdk.models.get_ip_from_sender import GetIpFromSender
from sib_api_v3_sdk.models.get_ips import GetIps
from sib_api_v3_sdk.models.get_ips_from_sender import GetIpsFromSender
from sib_api_v3_sdk.models.get_list import GetList
from sib_api_v3_sdk.models.get_lists import GetLists
from sib_api_v3_sdk.models.get_process import GetProcess
from sib_api_v3_sdk.models.get_processes import GetProcesses
from sib_api_v3_sdk.models.get_product_details import GetProductDetails
from sib_api_v3_sdk.models.get_products import GetProducts
from sib_api_v3_sdk.models.get_reports import GetReports
from sib_api_v3_sdk.models.get_reports_reports import GetReportsReports
from sib_api_v3_sdk.models.get_scheduled_email_by_batch_id import GetScheduledEmailByBatchId
from sib_api_v3_sdk.models.get_scheduled_email_by_batch_id_batches import GetScheduledEmailByBatchIdBatches
from sib_api_v3_sdk.models.get_scheduled_email_by_message_id import GetScheduledEmailByMessageId
from sib_api_v3_sdk.models.get_senders_list import GetSendersList
from sib_api_v3_sdk.models.get_senders_list_ips import GetSendersListIps
from sib_api_v3_sdk.models.get_senders_list_senders import GetSendersListSenders
from sib_api_v3_sdk.models.get_shared_template_url import GetSharedTemplateUrl
from sib_api_v3_sdk.models.get_sms_campaign_overview import GetSmsCampaignOverview
from sib_api_v3_sdk.models.get_sms_campaign_stats import GetSmsCampaignStats
from sib_api_v3_sdk.models.get_sms_campaigns import GetSmsCampaigns
from sib_api_v3_sdk.models.get_sms_event_report import GetSmsEventReport
from sib_api_v3_sdk.models.get_sms_event_report_events import GetSmsEventReportEvents
from sib_api_v3_sdk.models.get_smtp_template_overview import GetSmtpTemplateOverview
from sib_api_v3_sdk.models.get_smtp_template_overview_sender import GetSmtpTemplateOverviewSender
from sib_api_v3_sdk.models.get_smtp_templates import GetSmtpTemplates
from sib_api_v3_sdk.models.get_sso_token import GetSsoToken
from sib_api_v3_sdk.models.get_stats_by_browser import GetStatsByBrowser
from sib_api_v3_sdk.models.get_stats_by_device import GetStatsByDevice
from sib_api_v3_sdk.models.get_stats_by_domain import GetStatsByDomain
from sib_api_v3_sdk.models.get_transac_aggregated_sms_report import GetTransacAggregatedSmsReport
from sib_api_v3_sdk.models.get_transac_blocked_contacts import GetTransacBlockedContacts
from sib_api_v3_sdk.models.get_transac_blocked_contacts_contacts import GetTransacBlockedContactsContacts
from sib_api_v3_sdk.models.get_transac_blocked_contacts_reason import GetTransacBlockedContactsReason
from sib_api_v3_sdk.models.get_transac_email_content import GetTransacEmailContent
from sib_api_v3_sdk.models.get_transac_email_content_events import GetTransacEmailContentEvents
from sib_api_v3_sdk.models.get_transac_emails_list import GetTransacEmailsList
from sib_api_v3_sdk.models.get_transac_emails_list_transactional_emails import GetTransacEmailsListTransactionalEmails
from sib_api_v3_sdk.models.get_transac_sms_report import GetTransacSmsReport
from sib_api_v3_sdk.models.get_transac_sms_report_reports import GetTransacSmsReportReports
from sib_api_v3_sdk.models.get_wa_templates import GetWATemplates
from sib_api_v3_sdk.models.get_wa_templates_templates import GetWATemplatesTemplates
from sib_api_v3_sdk.models.get_webhook import GetWebhook
from sib_api_v3_sdk.models.get_webhooks import GetWebhooks
from sib_api_v3_sdk.models.get_whatsapp_campaign_overview import GetWhatsappCampaignOverview
from sib_api_v3_sdk.models.get_whatsapp_event_report import GetWhatsappEventReport
from sib_api_v3_sdk.models.get_whatsapp_event_report_events import GetWhatsappEventReportEvents
from sib_api_v3_sdk.models.inline_response200 import InlineResponse200
from sib_api_v3_sdk.models.inline_response201 import InlineResponse201
from sib_api_v3_sdk.models.inline_response2011 import InlineResponse2011
from sib_api_v3_sdk.models.inline_response2012 import InlineResponse2012
from sib_api_v3_sdk.models.inline_response2013 import InlineResponse2013
from sib_api_v3_sdk.models.manage_ip import ManageIp
from sib_api_v3_sdk.models.master_details_response import MasterDetailsResponse
from sib_api_v3_sdk.models.master_details_response_billing_info import MasterDetailsResponseBillingInfo
from sib_api_v3_sdk.models.master_details_response_billing_info_address import MasterDetailsResponseBillingInfoAddress
from sib_api_v3_sdk.models.master_details_response_billing_info_name import MasterDetailsResponseBillingInfoName
from sib_api_v3_sdk.models.master_details_response_plan_info import MasterDetailsResponsePlanInfo
from sib_api_v3_sdk.models.master_details_response_plan_info_features import MasterDetailsResponsePlanInfoFeatures
from sib_api_v3_sdk.models.note import Note
from sib_api_v3_sdk.models.note_data import NoteData
from sib_api_v3_sdk.models.note_id import NoteId
from sib_api_v3_sdk.models.note_list import NoteList
from sib_api_v3_sdk.models.order import Order
from sib_api_v3_sdk.models.order_batch import OrderBatch
from sib_api_v3_sdk.models.order_billing import OrderBilling
from sib_api_v3_sdk.models.order_products import OrderProducts
from sib_api_v3_sdk.models.pipeline import Pipeline
from sib_api_v3_sdk.models.pipeline_stage import PipelineStage
from sib_api_v3_sdk.models.post_contact_info import PostContactInfo
from sib_api_v3_sdk.models.post_contact_info_contacts import PostContactInfoContacts
from sib_api_v3_sdk.models.post_send_failed import PostSendFailed
from sib_api_v3_sdk.models.post_send_sms_test_failed import PostSendSmsTestFailed
from sib_api_v3_sdk.models.remaining_credit_model import RemainingCreditModel
from sib_api_v3_sdk.models.remaining_credit_model_child import RemainingCreditModelChild
from sib_api_v3_sdk.models.remaining_credit_model_reseller import RemainingCreditModelReseller
from sib_api_v3_sdk.models.remove_contact_from_list import RemoveContactFromList
from sib_api_v3_sdk.models.remove_credits import RemoveCredits
from sib_api_v3_sdk.models.request_contact_export import RequestContactExport
from sib_api_v3_sdk.models.request_contact_export_custom_contact_filter import RequestContactExportCustomContactFilter
from sib_api_v3_sdk.models.request_contact_import import RequestContactImport
from sib_api_v3_sdk.models.request_contact_import_new_list import RequestContactImportNewList
from sib_api_v3_sdk.models.request_sms_recipient_export import RequestSmsRecipientExport
from sib_api_v3_sdk.models.schedule_smtp_email import ScheduleSmtpEmail
from sib_api_v3_sdk.models.send_report import SendReport
from sib_api_v3_sdk.models.send_report_email import SendReportEmail
from sib_api_v3_sdk.models.send_sms import SendSms
from sib_api_v3_sdk.models.send_smtp_email import SendSmtpEmail
from sib_api_v3_sdk.models.send_smtp_email_attachment import SendSmtpEmailAttachment
from sib_api_v3_sdk.models.send_smtp_email_bcc import SendSmtpEmailBcc
from sib_api_v3_sdk.models.send_smtp_email_cc import SendSmtpEmailCc
from sib_api_v3_sdk.models.send_smtp_email_message_versions import SendSmtpEmailMessageVersions
from sib_api_v3_sdk.models.send_smtp_email_reply_to import SendSmtpEmailReplyTo
from sib_api_v3_sdk.models.send_smtp_email_reply_to1 import SendSmtpEmailReplyTo1
from sib_api_v3_sdk.models.send_smtp_email_sender import SendSmtpEmailSender
from sib_api_v3_sdk.models.send_smtp_email_to import SendSmtpEmailTo
from sib_api_v3_sdk.models.send_smtp_email_to1 import SendSmtpEmailTo1
from sib_api_v3_sdk.models.send_test_email import SendTestEmail
from sib_api_v3_sdk.models.send_test_sms import SendTestSms
from sib_api_v3_sdk.models.send_transac_sms import SendTransacSms
from sib_api_v3_sdk.models.send_whatsapp_message import SendWhatsappMessage
from sib_api_v3_sdk.models.sso_token_request import SsoTokenRequest
from sib_api_v3_sdk.models.sub_account_details_response import SubAccountDetailsResponse
from sib_api_v3_sdk.models.sub_account_details_response_plan_info import SubAccountDetailsResponsePlanInfo
from sib_api_v3_sdk.models.sub_account_details_response_plan_info_credits import SubAccountDetailsResponsePlanInfoCredits
from sib_api_v3_sdk.models.sub_account_details_response_plan_info_credits_emails import SubAccountDetailsResponsePlanInfoCreditsEmails
from sib_api_v3_sdk.models.sub_account_details_response_plan_info_features import SubAccountDetailsResponsePlanInfoFeatures
from sib_api_v3_sdk.models.sub_account_details_response_plan_info_features_inbox import SubAccountDetailsResponsePlanInfoFeaturesInbox
from sib_api_v3_sdk.models.sub_account_details_response_plan_info_features_landing_page import SubAccountDetailsResponsePlanInfoFeaturesLandingPage
from sib_api_v3_sdk.models.sub_account_details_response_plan_info_features_users import SubAccountDetailsResponsePlanInfoFeaturesUsers
from sib_api_v3_sdk.models.sub_account_update_plan_request import SubAccountUpdatePlanRequest
from sib_api_v3_sdk.models.sub_account_update_plan_request_credits import SubAccountUpdatePlanRequestCredits
from sib_api_v3_sdk.models.sub_account_update_plan_request_features import SubAccountUpdatePlanRequestFeatures
from sib_api_v3_sdk.models.sub_accounts_response import SubAccountsResponse
from sib_api_v3_sdk.models.sub_accounts_response_sub_accounts import SubAccountsResponseSubAccounts
from sib_api_v3_sdk.models.task import Task
from sib_api_v3_sdk.models.task_list import TaskList
from sib_api_v3_sdk.models.task_reminder import TaskReminder
from sib_api_v3_sdk.models.task_types import TaskTypes
from sib_api_v3_sdk.models.update_attribute import UpdateAttribute
from sib_api_v3_sdk.models.update_attribute_enumeration import UpdateAttributeEnumeration
from sib_api_v3_sdk.models.update_batch_contacts import UpdateBatchContacts
from sib_api_v3_sdk.models.update_batch_contacts_contacts import UpdateBatchContactsContacts
from sib_api_v3_sdk.models.update_batch_contacts_model import UpdateBatchContactsModel
from sib_api_v3_sdk.models.update_campaign_status import UpdateCampaignStatus
from sib_api_v3_sdk.models.update_child import UpdateChild
from sib_api_v3_sdk.models.update_child_account_status import UpdateChildAccountStatus
from sib_api_v3_sdk.models.update_child_domain import UpdateChildDomain
from sib_api_v3_sdk.models.update_contact import UpdateContact
from sib_api_v3_sdk.models.update_email_campaign import UpdateEmailCampaign
from sib_api_v3_sdk.models.update_email_campaign_recipients import UpdateEmailCampaignRecipients
from sib_api_v3_sdk.models.update_email_campaign_sender import UpdateEmailCampaignSender
from sib_api_v3_sdk.models.update_external_feed import UpdateExternalFeed
from sib_api_v3_sdk.models.update_list import UpdateList
from sib_api_v3_sdk.models.update_sender import UpdateSender
from sib_api_v3_sdk.models.update_sms_campaign import UpdateSmsCampaign
from sib_api_v3_sdk.models.update_smtp_template import UpdateSmtpTemplate
from sib_api_v3_sdk.models.update_smtp_template_sender import UpdateSmtpTemplateSender
from sib_api_v3_sdk.models.update_webhook import UpdateWebhook
from sib_api_v3_sdk.models.upload_image_model import UploadImageModel
from sib_api_v3_sdk.models.upload_image_to_gallery import UploadImageToGallery
from sib_api_v3_sdk.models.variables_items import VariablesItems
from sib_api_v3_sdk.models.whatsapp_camp_stats import WhatsappCampStats
from sib_api_v3_sdk.models.whatsapp_camp_template import WhatsappCampTemplate
from sib_api_v3_sdk.models.get_child_info import GetChildInfo
from sib_api_v3_sdk.models.get_extended_campaign_overview import GetExtendedCampaignOverview
from sib_api_v3_sdk.models.get_extended_client import GetExtendedClient
from sib_api_v3_sdk.models.get_extended_contact_details import GetExtendedContactDetails
from sib_api_v3_sdk.models.get_extended_list import GetExtendedList
from sib_api_v3_sdk.models.get_sms_campaign import GetSmsCampaign
from sib_api_v3_sdk.models.get_account import GetAccount
from sib_api_v3_sdk.models.get_email_campaign import GetEmailCampaign
