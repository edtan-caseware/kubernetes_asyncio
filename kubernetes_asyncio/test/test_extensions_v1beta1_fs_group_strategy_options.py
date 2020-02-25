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
from kubernetes_asyncio.client.models.extensions_v1beta1_fs_group_strategy_options import ExtensionsV1beta1FSGroupStrategyOptions  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestExtensionsV1beta1FSGroupStrategyOptions(unittest.TestCase):
    """ExtensionsV1beta1FSGroupStrategyOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExtensionsV1beta1FSGroupStrategyOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.extensions_v1beta1_fs_group_strategy_options.ExtensionsV1beta1FSGroupStrategyOptions()  # noqa: E501
        if include_optional :
            return ExtensionsV1beta1FSGroupStrategyOptions(
                ranges = [
                    kubernetes_asyncio.client.models.extensions/v1beta1/id_range.extensions.v1beta1.IDRange(
                        max = 56, 
                        min = 56, )
                    ], 
                rule = '0'
            )
        else :
            return ExtensionsV1beta1FSGroupStrategyOptions(
        )

    def testExtensionsV1beta1FSGroupStrategyOptions(self):
        """Test ExtensionsV1beta1FSGroupStrategyOptions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
