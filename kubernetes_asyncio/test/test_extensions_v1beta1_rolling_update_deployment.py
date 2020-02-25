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
from kubernetes_asyncio.client.models.extensions_v1beta1_rolling_update_deployment import ExtensionsV1beta1RollingUpdateDeployment  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestExtensionsV1beta1RollingUpdateDeployment(unittest.TestCase):
    """ExtensionsV1beta1RollingUpdateDeployment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExtensionsV1beta1RollingUpdateDeployment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.extensions_v1beta1_rolling_update_deployment.ExtensionsV1beta1RollingUpdateDeployment()  # noqa: E501
        if include_optional :
            return ExtensionsV1beta1RollingUpdateDeployment(
                max_surge = kubernetes_asyncio.client.models.max_surge.maxSurge(), 
                max_unavailable = kubernetes_asyncio.client.models.max_unavailable.maxUnavailable()
            )
        else :
            return ExtensionsV1beta1RollingUpdateDeployment(
        )

    def testExtensionsV1beta1RollingUpdateDeployment(self):
        """Test ExtensionsV1beta1RollingUpdateDeployment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
