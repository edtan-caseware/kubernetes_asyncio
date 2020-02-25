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
from kubernetes_asyncio.client.models.v1_persistent_volume_claim_spec import V1PersistentVolumeClaimSpec  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1PersistentVolumeClaimSpec(unittest.TestCase):
    """V1PersistentVolumeClaimSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1PersistentVolumeClaimSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1_persistent_volume_claim_spec.V1PersistentVolumeClaimSpec()  # noqa: E501
        if include_optional :
            return V1PersistentVolumeClaimSpec(
                access_modes = [
                    '0'
                    ], 
                data_source = kubernetes_asyncio.client.models.v1/typed_local_object_reference.v1.TypedLocalObjectReference(
                    api_group = '0', 
                    kind = '0', 
                    name = '0', ), 
                resources = kubernetes_asyncio.client.models.v1/resource_requirements.v1.ResourceRequirements(
                    limits = {
                        'key' : '0'
                        }, 
                    requests = {
                        'key' : '0'
                        }, ), 
                selector = kubernetes_asyncio.client.models.v1/label_selector.v1.LabelSelector(
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
                storage_class_name = '0', 
                volume_mode = '0', 
                volume_name = '0'
            )
        else :
            return V1PersistentVolumeClaimSpec(
        )

    def testV1PersistentVolumeClaimSpec(self):
        """Test V1PersistentVolumeClaimSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
