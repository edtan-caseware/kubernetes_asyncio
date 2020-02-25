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
from kubernetes_asyncio.client.models.v1_config_map_node_config_source import V1ConfigMapNodeConfigSource  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1ConfigMapNodeConfigSource(unittest.TestCase):
    """V1ConfigMapNodeConfigSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ConfigMapNodeConfigSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1_config_map_node_config_source.V1ConfigMapNodeConfigSource()  # noqa: E501
        if include_optional :
            return V1ConfigMapNodeConfigSource(
                kubelet_config_key = '0', 
                name = '0', 
                namespace = '0', 
                resource_version = '0', 
                uid = '0'
            )
        else :
            return V1ConfigMapNodeConfigSource(
                kubelet_config_key = '0',
                name = '0',
                namespace = '0',
        )

    def testV1ConfigMapNodeConfigSource(self):
        """Test V1ConfigMapNodeConfigSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
