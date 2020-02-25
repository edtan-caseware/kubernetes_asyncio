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
from kubernetes_asyncio.client.models.policy_v1beta1_allowed_host_path import PolicyV1beta1AllowedHostPath  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestPolicyV1beta1AllowedHostPath(unittest.TestCase):
    """PolicyV1beta1AllowedHostPath unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PolicyV1beta1AllowedHostPath
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.policy_v1beta1_allowed_host_path.PolicyV1beta1AllowedHostPath()  # noqa: E501
        if include_optional :
            return PolicyV1beta1AllowedHostPath(
                path_prefix = '0', 
                read_only = True
            )
        else :
            return PolicyV1beta1AllowedHostPath(
        )

    def testPolicyV1beta1AllowedHostPath(self):
        """Test PolicyV1beta1AllowedHostPath"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
