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
from kubernetes_asyncio.client.models.apiextensions_v1beta1_webhook_client_config import ApiextensionsV1beta1WebhookClientConfig  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestApiextensionsV1beta1WebhookClientConfig(unittest.TestCase):
    """ApiextensionsV1beta1WebhookClientConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiextensionsV1beta1WebhookClientConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.apiextensions_v1beta1_webhook_client_config.ApiextensionsV1beta1WebhookClientConfig()  # noqa: E501
        if include_optional :
            return ApiextensionsV1beta1WebhookClientConfig(
                ca_bundle = 'YQ==', 
                service = kubernetes_asyncio.client.models.apiextensions/v1beta1/service_reference.apiextensions.v1beta1.ServiceReference(
                    name = '0', 
                    namespace = '0', 
                    path = '0', 
                    port = 56, ), 
                url = '0'
            )
        else :
            return ApiextensionsV1beta1WebhookClientConfig(
        )

    def testApiextensionsV1beta1WebhookClientConfig(self):
        """Test ApiextensionsV1beta1WebhookClientConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
