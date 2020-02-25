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
from kubernetes_asyncio.client.models.v1_rbd_volume_source import V1RBDVolumeSource  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1RBDVolumeSource(unittest.TestCase):
    """V1RBDVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1RBDVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1_rbd_volume_source.V1RBDVolumeSource()  # noqa: E501
        if include_optional :
            return V1RBDVolumeSource(
                fs_type = '0', 
                image = '0', 
                keyring = '0', 
                monitors = [
                    '0'
                    ], 
                pool = '0', 
                read_only = True, 
                secret_ref = kubernetes_asyncio.client.models.v1/local_object_reference.v1.LocalObjectReference(
                    name = '0', ), 
                user = '0'
            )
        else :
            return V1RBDVolumeSource(
                image = '0',
                monitors = [
                    '0'
                    ],
        )

    def testV1RBDVolumeSource(self):
        """Test V1RBDVolumeSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
