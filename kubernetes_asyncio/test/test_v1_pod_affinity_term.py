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
from kubernetes_asyncio.client.models.v1_pod_affinity_term import V1PodAffinityTerm  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1PodAffinityTerm(unittest.TestCase):
    """V1PodAffinityTerm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1PodAffinityTerm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1_pod_affinity_term.V1PodAffinityTerm()  # noqa: E501
        if include_optional :
            return V1PodAffinityTerm(
                label_selector = kubernetes_asyncio.client.models.v1/label_selector.v1.LabelSelector(
                    match_expressions = [
                        kubernetes_asyncio.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                            key = '0', 
                            operator = '0', 
                            values = [
                                '0'
                                ], )
                        ], 
                    match_labels = {
                        'key' : '0'
                        }, ), 
                namespaces = [
                    '0'
                    ], 
                topology_key = '0'
            )
        else :
            return V1PodAffinityTerm(
                topology_key = '0',
        )

    def testV1PodAffinityTerm(self):
        """Test V1PodAffinityTerm"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
