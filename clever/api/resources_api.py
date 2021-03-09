# coding: utf-8

"""
    Data API

    Serves the Clever Data API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from clever.api_client import ApiClient


class ResourcesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_courses_for_resource(self, id, **kwargs):  # noqa: E501
        """get_courses_for_resource  # noqa: E501

        Returns the courses for a resource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_courses_for_resource(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: CoursesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_courses_for_resource_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_courses_for_resource_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_courses_for_resource_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_courses_for_resource  # noqa: E501

        Returns the courses for a resource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_courses_for_resource_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: CoursesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'limit', 'starting_after', 'ending_before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_courses_for_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_courses_for_resource`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'starting_after' in params:
            query_params.append(('starting_after', params['starting_after']))  # noqa: E501
        if 'ending_before' in params:
            query_params.append(('ending_before', params['ending_before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/resources/{id}/courses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CoursesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_resource(self, id, **kwargs):  # noqa: E501
        """get_resource  # noqa: E501

        Returns a specific resource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_resource(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: ResourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_resource_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_resource_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_resource_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_resource  # noqa: E501

        Returns a specific resource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_resource_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: ResourceResponse
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
                    " to method get_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_resource`")  # noqa: E501

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

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/resources/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_resources(self, **kwargs):  # noqa: E501
        """get_resources  # noqa: E501

        Returns a list of resources  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_resources(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: ResourcesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_resources_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_resources_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_resources_with_http_info(self, **kwargs):  # noqa: E501
        """get_resources  # noqa: E501

        Returns a list of resources  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_resources_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: ResourcesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'starting_after', 'ending_before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resources" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'starting_after' in params:
            query_params.append(('starting_after', params['starting_after']))  # noqa: E501
        if 'ending_before' in params:
            query_params.append(('ending_before', params['ending_before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/resources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourcesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sections_for_resource(self, id, **kwargs):  # noqa: E501
        """get_sections_for_resource  # noqa: E501

        Returns the sections for a resource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sections_for_resource(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: SectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sections_for_resource_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sections_for_resource_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_sections_for_resource_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_sections_for_resource  # noqa: E501

        Returns the sections for a resource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sections_for_resource_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: SectionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'limit', 'starting_after', 'ending_before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sections_for_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_sections_for_resource`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'starting_after' in params:
            query_params.append(('starting_after', params['starting_after']))  # noqa: E501
        if 'ending_before' in params:
            query_params.append(('ending_before', params['ending_before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/resources/{id}/sections', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SectionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_users_for_resource(self, id, **kwargs):  # noqa: E501
        """get_users_for_resource  # noqa: E501

        Returns the student and/or teacher users for a resource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users_for_resource(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str role:
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: UsersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_users_for_resource_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_users_for_resource_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_users_for_resource_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_users_for_resource  # noqa: E501

        Returns the student and/or teacher users for a resource  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users_for_resource_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str role:
        :param int limit:
        :param str starting_after:
        :param str ending_before:
        :return: UsersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'role', 'limit', 'starting_after', 'ending_before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users_for_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_users_for_resource`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'role' in params:
            query_params.append(('role', params['role']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'starting_after' in params:
            query_params.append(('starting_after', params['starting_after']))  # noqa: E501
        if 'ending_before' in params:
            query_params.append(('ending_before', params['ending_before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/resources/{id}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UsersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
