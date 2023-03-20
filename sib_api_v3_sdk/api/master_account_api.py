# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sib_api_v3_sdk.api_client import ApiClient


class MasterAccountApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def corporate_master_account_get(self, **kwargs):  # noqa: E501
        """Get the details of requested master account  # noqa: E501

        This endpoint will provide the details of the master account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.corporate_master_account_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MasterDetailsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.corporate_master_account_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.corporate_master_account_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def corporate_master_account_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get the details of requested master account  # noqa: E501

        This endpoint will provide the details of the master account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.corporate_master_account_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: MasterDetailsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method corporate_master_account_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/corporate/masterAccount', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MasterDetailsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def corporate_sub_account_get(self, offset, limit, **kwargs):  # noqa: E501
        """Get the list of all the sub-accounts of the master account.  # noqa: E501

        This endpoint will provide the list all the sub-accounts of the master account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.corporate_sub_account_get(offset, limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Index of the first sub-account in the page (required)
        :param int limit: Number of sub-accounts to be displayed on each page (required)
        :return: SubAccountsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.corporate_sub_account_get_with_http_info(offset, limit, **kwargs)  # noqa: E501
        else:
            (data) = self.corporate_sub_account_get_with_http_info(offset, limit, **kwargs)  # noqa: E501
            return data

    def corporate_sub_account_get_with_http_info(self, offset, limit, **kwargs):  # noqa: E501
        """Get the list of all the sub-accounts of the master account.  # noqa: E501

        This endpoint will provide the list all the sub-accounts of the master account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.corporate_sub_account_get_with_http_info(offset, limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Index of the first sub-account in the page (required)
        :param int limit: Number of sub-accounts to be displayed on each page (required)
        :return: SubAccountsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method corporate_sub_account_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'offset' is set
        if ('offset' not in params or
                params['offset'] is None):
            raise ValueError("Missing the required parameter `offset` when calling `corporate_sub_account_get`")  # noqa: E501
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `corporate_sub_account_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/corporate/subAccount', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SubAccountsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def corporate_sub_account_id_delete(self, id, **kwargs):  # noqa: E501
        """Delete a sub-account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.corporate_sub_account_id_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id of the sub-account organization to be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.corporate_sub_account_id_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.corporate_sub_account_id_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def corporate_sub_account_id_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a sub-account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.corporate_sub_account_id_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id of the sub-account organization to be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method corporate_sub_account_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `corporate_sub_account_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/corporate/subAccount/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def corporate_sub_account_id_get(self, id, **kwargs):  # noqa: E501
        """Get sub-account details  # noqa: E501

        This endpoint will provide the details for the specified sub-account company  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.corporate_sub_account_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id of the sub-account organization (required)
        :return: SubAccountDetailsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.corporate_sub_account_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.corporate_sub_account_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def corporate_sub_account_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get sub-account details  # noqa: E501

        This endpoint will provide the details for the specified sub-account company  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.corporate_sub_account_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id of the sub-account organization (required)
        :return: SubAccountDetailsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method corporate_sub_account_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `corporate_sub_account_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/corporate/subAccount/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SubAccountDetailsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def corporate_sub_account_id_plan_put(self, id, update_plan_details, **kwargs):  # noqa: E501
        """Update sub-account plan  # noqa: E501

        This endpoint will update the sub-account plan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.corporate_sub_account_id_plan_put(id, update_plan_details, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id of the sub-account organization (required)
        :param SubAccountUpdatePlanRequest update_plan_details: Values to update a sub-account plan (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.corporate_sub_account_id_plan_put_with_http_info(id, update_plan_details, **kwargs)  # noqa: E501
        else:
            (data) = self.corporate_sub_account_id_plan_put_with_http_info(id, update_plan_details, **kwargs)  # noqa: E501
            return data

    def corporate_sub_account_id_plan_put_with_http_info(self, id, update_plan_details, **kwargs):  # noqa: E501
        """Update sub-account plan  # noqa: E501

        This endpoint will update the sub-account plan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.corporate_sub_account_id_plan_put_with_http_info(id, update_plan_details, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id of the sub-account organization (required)
        :param SubAccountUpdatePlanRequest update_plan_details: Values to update a sub-account plan (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'update_plan_details']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method corporate_sub_account_id_plan_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `corporate_sub_account_id_plan_put`")  # noqa: E501
        # verify the required parameter 'update_plan_details' is set
        if ('update_plan_details' not in params or
                params['update_plan_details'] is None):
            raise ValueError("Missing the required parameter `update_plan_details` when calling `corporate_sub_account_id_plan_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_plan_details' in params:
            body_params = params['update_plan_details']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/corporate/subAccount/{id}/plan', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def corporate_sub_account_key_post(self, create_api_key_request, **kwargs):  # noqa: E501
        """Create an API key for a sub-account  # noqa: E501

        This endpoint will generate an API v3 key for a sub account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.corporate_sub_account_key_post(create_api_key_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateApiKeyRequest create_api_key_request: Values to generate API key for sub-account (required)
        :return: CreateApiKeyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.corporate_sub_account_key_post_with_http_info(create_api_key_request, **kwargs)  # noqa: E501
        else:
            (data) = self.corporate_sub_account_key_post_with_http_info(create_api_key_request, **kwargs)  # noqa: E501
            return data

    def corporate_sub_account_key_post_with_http_info(self, create_api_key_request, **kwargs):  # noqa: E501
        """Create an API key for a sub-account  # noqa: E501

        This endpoint will generate an API v3 key for a sub account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.corporate_sub_account_key_post_with_http_info(create_api_key_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateApiKeyRequest create_api_key_request: Values to generate API key for sub-account (required)
        :return: CreateApiKeyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_api_key_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method corporate_sub_account_key_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_api_key_request' is set
        if ('create_api_key_request' not in params or
                params['create_api_key_request'] is None):
            raise ValueError("Missing the required parameter `create_api_key_request` when calling `corporate_sub_account_key_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_api_key_request' in params:
            body_params = params['create_api_key_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/corporate/subAccount/key', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateApiKeyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def corporate_sub_account_post(self, sub_account_create, **kwargs):  # noqa: E501
        """Create a new sub-account under a master account.  # noqa: E501

        This endpoint will create a new sub-account under a master account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.corporate_sub_account_post(sub_account_create, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateSubAccount sub_account_create: values to create new sub-account (required)
        :return: CreateSubAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.corporate_sub_account_post_with_http_info(sub_account_create, **kwargs)  # noqa: E501
        else:
            (data) = self.corporate_sub_account_post_with_http_info(sub_account_create, **kwargs)  # noqa: E501
            return data

    def corporate_sub_account_post_with_http_info(self, sub_account_create, **kwargs):  # noqa: E501
        """Create a new sub-account under a master account.  # noqa: E501

        This endpoint will create a new sub-account under a master account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.corporate_sub_account_post_with_http_info(sub_account_create, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateSubAccount sub_account_create: values to create new sub-account (required)
        :return: CreateSubAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sub_account_create']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method corporate_sub_account_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sub_account_create' is set
        if ('sub_account_create' not in params or
                params['sub_account_create'] is None):
            raise ValueError("Missing the required parameter `sub_account_create` when calling `corporate_sub_account_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sub_account_create' in params:
            body_params = params['sub_account_create']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/corporate/subAccount', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateSubAccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def corporate_sub_account_sso_token_post(self, sso_token_request, **kwargs):  # noqa: E501
        """Generate SSO token to access Sendinblue  # noqa: E501

        This endpoint generates an sso token to authenticate and access a sub-account of the master using the account endpoint https://account-app.sendinblue.com/account/login/sub-account/sso/[token], where [token] will be replaced by the actual token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.corporate_sub_account_sso_token_post(sso_token_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SsoTokenRequest sso_token_request: Values to generate SSO token for sub-account (required)
        :return: GetSsoToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.corporate_sub_account_sso_token_post_with_http_info(sso_token_request, **kwargs)  # noqa: E501
        else:
            (data) = self.corporate_sub_account_sso_token_post_with_http_info(sso_token_request, **kwargs)  # noqa: E501
            return data

    def corporate_sub_account_sso_token_post_with_http_info(self, sso_token_request, **kwargs):  # noqa: E501
        """Generate SSO token to access Sendinblue  # noqa: E501

        This endpoint generates an sso token to authenticate and access a sub-account of the master using the account endpoint https://account-app.sendinblue.com/account/login/sub-account/sso/[token], where [token] will be replaced by the actual token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.corporate_sub_account_sso_token_post_with_http_info(sso_token_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SsoTokenRequest sso_token_request: Values to generate SSO token for sub-account (required)
        :return: GetSsoToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sso_token_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method corporate_sub_account_sso_token_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sso_token_request' is set
        if ('sso_token_request' not in params or
                params['sso_token_request'] is None):
            raise ValueError("Missing the required parameter `sso_token_request` when calling `corporate_sub_account_sso_token_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sso_token_request' in params:
            body_params = params['sso_token_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/corporate/subAccount/ssoToken', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetSsoToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
