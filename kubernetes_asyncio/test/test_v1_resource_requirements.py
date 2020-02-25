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
from kubernetes_asyncio.client.models.v1_resource_requirements import V1ResourceRequirements  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1ResourceRequirements(unittest.TestCase):
    """V1ResourceRequirements unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ResourceRequirements
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1_resource_requirements.V1ResourceRequirements()  # noqa: E501
        if include_optional :
            return V1ResourceRequirements(
                limits = {
                    'key' : '0'
                    }, 
                requests = {
                    'key' : '0'
                    }
            )
        else :
            return V1ResourceRequirements(
        )

    def testV1ResourceRequirements(self):
        """Test V1ResourceRequirements"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
