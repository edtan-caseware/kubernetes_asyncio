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
from kubernetes_asyncio.client.models.v1_non_resource_attributes import V1NonResourceAttributes  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1NonResourceAttributes(unittest.TestCase):
    """V1NonResourceAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1NonResourceAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1_non_resource_attributes.V1NonResourceAttributes()  # noqa: E501
        if include_optional :
            return V1NonResourceAttributes(
                path = '0', 
                verb = '0'
            )
        else :
            return V1NonResourceAttributes(
        )

    def testV1NonResourceAttributes(self):
        """Test V1NonResourceAttributes"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
