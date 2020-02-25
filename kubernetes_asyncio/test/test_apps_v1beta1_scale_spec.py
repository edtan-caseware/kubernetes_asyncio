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
from kubernetes_asyncio.client.models.apps_v1beta1_scale_spec import AppsV1beta1ScaleSpec  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestAppsV1beta1ScaleSpec(unittest.TestCase):
    """AppsV1beta1ScaleSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AppsV1beta1ScaleSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.apps_v1beta1_scale_spec.AppsV1beta1ScaleSpec()  # noqa: E501
        if include_optional :
            return AppsV1beta1ScaleSpec(
                replicas = 56
            )
        else :
            return AppsV1beta1ScaleSpec(
        )

    def testAppsV1beta1ScaleSpec(self):
        """Test AppsV1beta1ScaleSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
