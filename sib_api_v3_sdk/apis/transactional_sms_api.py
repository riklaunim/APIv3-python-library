# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  | 

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class TransactionalSMSApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_sms_events(self, **kwargs):
        """
        Get all the SMS activity (unaggregated events)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sms_events(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int limit: Number of documents per page
        :param date start_date: Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report
        :param date end_date: Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report
        :param int offset: Index of the first document of the page
        :param int days: Number of days in the past including today (positive integer). Not compatible with 'startDate' and 'endDate'
        :param str phone_number: Filter the report for a specific phone number
        :param str event: Filter the report for specific events
        :param str tags: Filter the report for specific tags passed as a serialized urlencoded array
        :return: GetSmsEventReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_sms_events_with_http_info(**kwargs)
        else:
            (data) = self.get_sms_events_with_http_info(**kwargs)
            return data

    def get_sms_events_with_http_info(self, **kwargs):
        """
        Get all the SMS activity (unaggregated events)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_sms_events_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int limit: Number of documents per page
        :param date start_date: Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report
        :param date end_date: Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report
        :param int offset: Index of the first document of the page
        :param int days: Number of days in the past including today (positive integer). Not compatible with 'startDate' and 'endDate'
        :param str phone_number: Filter the report for a specific phone number
        :param str event: Filter the report for specific events
        :param str tags: Filter the report for specific tags passed as a serialized urlencoded array
        :return: GetSmsEventReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'start_date', 'end_date', 'offset', 'days', 'phone_number', 'event', 'tags']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sms_events" % key
                )
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 100:
            raise ValueError("Invalid value for parameter `limit` when calling `get_sms_events`, must be a value less than or equal to `100`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'days' in params:
            query_params.append(('days', params['days']))
        if 'phone_number' in params:
            query_params.append(('phoneNumber', params['phone_number']))
        if 'event' in params:
            query_params.append(('event', params['event']))
        if 'tags' in params:
            query_params.append(('tags', params['tags']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api-key']

        return self.api_client.call_api('/transactionalSMS/statistics/events', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetSmsEventReport',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_transac_aggregated_sms_report(self, **kwargs):
        """
        Get your SMS activity aggregated over a period of time
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_transac_aggregated_sms_report(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param date start_date: Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report
        :param date end_date: Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report
        :param int days: Number of days in the past including today (positive integer). Not compatible with startDate and endDate
        :param str tag: Filter on a tag
        :return: GetTransacAggregatedSmsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_transac_aggregated_sms_report_with_http_info(**kwargs)
        else:
            (data) = self.get_transac_aggregated_sms_report_with_http_info(**kwargs)
            return data

    def get_transac_aggregated_sms_report_with_http_info(self, **kwargs):
        """
        Get your SMS activity aggregated over a period of time
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_transac_aggregated_sms_report_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param date start_date: Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report
        :param date end_date: Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report
        :param int days: Number of days in the past including today (positive integer). Not compatible with startDate and endDate
        :param str tag: Filter on a tag
        :return: GetTransacAggregatedSmsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'days', 'tag']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transac_aggregated_sms_report" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))
        if 'days' in params:
            query_params.append(('days', params['days']))
        if 'tag' in params:
            query_params.append(('tag', params['tag']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api-key']

        return self.api_client.call_api('/transactionalSMS/statistics/aggregatedReport', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetTransacAggregatedSmsReport',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_transac_sms_report(self, **kwargs):
        """
        Get your SMS activity aggregated per day
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_transac_sms_report(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param date start_date: Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report
        :param date end_date: Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report
        :param int days: Number of days in the past including today (positive integer). Not compatible with 'startDate' and 'endDate'
        :param str tag: Filter on a tag
        :return: GetTransacSmsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_transac_sms_report_with_http_info(**kwargs)
        else:
            (data) = self.get_transac_sms_report_with_http_info(**kwargs)
            return data

    def get_transac_sms_report_with_http_info(self, **kwargs):
        """
        Get your SMS activity aggregated per day
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_transac_sms_report_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param date start_date: Mandatory if endDate is used. Starting date (YYYY-MM-DD) of the report
        :param date end_date: Mandatory if startDate is used. Ending date (YYYY-MM-DD) of the report
        :param int days: Number of days in the past including today (positive integer). Not compatible with 'startDate' and 'endDate'
        :param str tag: Filter on a tag
        :return: GetTransacSmsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'days', 'tag']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transac_sms_report" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))
        if 'days' in params:
            query_params.append(('days', params['days']))
        if 'tag' in params:
            query_params.append(('tag', params['tag']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api-key']

        return self.api_client.call_api('/transactionalSMS/statistics/reports', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetTransacSmsReport',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def send_transac_sms(self, send_transac_sms, **kwargs):
        """
        Send the SMS campaign to the specified mobile number
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.send_transac_sms(send_transac_sms, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SendTransacSms send_transac_sms: Values to send a transactional SMS (required)
        :return: SendSms
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.send_transac_sms_with_http_info(send_transac_sms, **kwargs)
        else:
            (data) = self.send_transac_sms_with_http_info(send_transac_sms, **kwargs)
            return data

    def send_transac_sms_with_http_info(self, send_transac_sms, **kwargs):
        """
        Send the SMS campaign to the specified mobile number
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.send_transac_sms_with_http_info(send_transac_sms, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SendTransacSms send_transac_sms: Values to send a transactional SMS (required)
        :return: SendSms
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['send_transac_sms']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_transac_sms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'send_transac_sms' is set
        if ('send_transac_sms' not in params) or (params['send_transac_sms'] is None):
            raise ValueError("Missing the required parameter `send_transac_sms` when calling `send_transac_sms`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'send_transac_sms' in params:
            body_params = params['send_transac_sms']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api-key']

        return self.api_client.call_api('/transactionalSMS/sms', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SendSms',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
