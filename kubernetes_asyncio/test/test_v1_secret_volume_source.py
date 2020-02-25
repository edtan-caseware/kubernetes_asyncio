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
from kubernetes_asyncio.client.models.v1_secret_volume_source import V1SecretVolumeSource  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1SecretVolumeSource(unittest.TestCase):
    """V1SecretVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1SecretVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1_secret_volume_source.V1SecretVolumeSource()  # noqa: E501
        if include_optional :
            return V1SecretVolumeSource(
                default_mode = 56, 
                items = [
                    kubernetes_asyncio.client.models.v1/key_to_path.v1.KeyToPath(
                        key = '0', 
                        mode = 56, 
                        path = '0', )
                    ], 
                optional = True, 
                secret_name = '0'
            )
        else :
            return V1SecretVolumeSource(
        )

    def testV1SecretVolumeSource(self):
        """Test V1SecretVolumeSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
