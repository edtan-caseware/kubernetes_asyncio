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
from kubernetes_asyncio.client.models.v1_quobyte_volume_source import V1QuobyteVolumeSource  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1QuobyteVolumeSource(unittest.TestCase):
    """V1QuobyteVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1QuobyteVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1_quobyte_volume_source.V1QuobyteVolumeSource()  # noqa: E501
        if include_optional :
            return V1QuobyteVolumeSource(
                group = '0', 
                read_only = True, 
                registry = '0', 
                tenant = '0', 
                user = '0', 
                volume = '0'
            )
        else :
            return V1QuobyteVolumeSource(
                registry = '0',
                volume = '0',
        )

    def testV1QuobyteVolumeSource(self):
        """Test V1QuobyteVolumeSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
