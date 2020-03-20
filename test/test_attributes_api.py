# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import sib_api_v3_sdk
from sib_api_v3_sdk.api.attributes_api import AttributesApi  # noqa: E501
from sib_api_v3_sdk.rest import ApiException


class TestAttributesApi(unittest.TestCase):
    """AttributesApi unit test stubs"""

    def setUp(self):
        self.api = sib_api_v3_sdk.api.attributes_api.AttributesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_attribute(self):
        """Test case for create_attribute

        Creates contact attribute  # noqa: E501
        """
        pass

    def test_delete_attribute(self):
        """Test case for delete_attribute

        Deletes an attribute  # noqa: E501
        """
        pass

    def test_get_attributes(self):
        """Test case for get_attributes

        Lists all attributes  # noqa: E501
        """
        pass

    def test_update_attribute(self):
        """Test case for update_attribute

        Updates contact attribute  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
