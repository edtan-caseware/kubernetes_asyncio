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
from kubernetes_asyncio.client.models.v1beta1_policy_rule import V1beta1PolicyRule  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1beta1PolicyRule(unittest.TestCase):
    """V1beta1PolicyRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1PolicyRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1beta1_policy_rule.V1beta1PolicyRule()  # noqa: E501
        if include_optional :
            return V1beta1PolicyRule(
                api_groups = [
                    '0'
                    ], 
                non_resource_ur_ls = [
                    '0'
                    ], 
                resource_names = [
                    '0'
                    ], 
                resources = [
                    '0'
                    ], 
                verbs = [
                    '0'
                    ]
            )
        else :
            return V1beta1PolicyRule(
                verbs = [
                    '0'
                    ],
        )

    def testV1beta1PolicyRule(self):
        """Test V1beta1PolicyRule"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
