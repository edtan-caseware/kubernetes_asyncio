# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.15.9
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes_asyncio.client
from kubernetes_asyncio.client.models.apiregistration_v1beta1_service_reference import ApiregistrationV1beta1ServiceReference  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestApiregistrationV1beta1ServiceReference(unittest.TestCase):
    """ApiregistrationV1beta1ServiceReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiregistrationV1beta1ServiceReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.apiregistration_v1beta1_service_reference.ApiregistrationV1beta1ServiceReference()  # noqa: E501
        if include_optional :
            return ApiregistrationV1beta1ServiceReference(
                name = '0', 
                namespace = '0', 
                port = 56
            )
        else :
            return ApiregistrationV1beta1ServiceReference(
        )

    def testApiregistrationV1beta1ServiceReference(self):
        """Test ApiregistrationV1beta1ServiceReference"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
