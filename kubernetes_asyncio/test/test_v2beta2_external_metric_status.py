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
from kubernetes_asyncio.client.models.v2beta2_external_metric_status import V2beta2ExternalMetricStatus  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV2beta2ExternalMetricStatus(unittest.TestCase):
    """V2beta2ExternalMetricStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V2beta2ExternalMetricStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v2beta2_external_metric_status.V2beta2ExternalMetricStatus()  # noqa: E501
        if include_optional :
            return V2beta2ExternalMetricStatus(
                current = kubernetes_asyncio.client.models.v2beta2/metric_value_status.v2beta2.MetricValueStatus(
                    average_utilization = 56, 
                    average_value = '0', 
                    value = '0', ), 
                metric = kubernetes_asyncio.client.models.v2beta2/metric_identifier.v2beta2.MetricIdentifier(
                    name = '0', 
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
                            }, ), )
            )
        else :
            return V2beta2ExternalMetricStatus(
                current = kubernetes_asyncio.client.models.v2beta2/metric_value_status.v2beta2.MetricValueStatus(
                    average_utilization = 56, 
                    average_value = '0', 
                    value = '0', ),
                metric = kubernetes_asyncio.client.models.v2beta2/metric_identifier.v2beta2.MetricIdentifier(
                    name = '0', 
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
                            }, ), ),
        )

    def testV2beta2ExternalMetricStatus(self):
        """Test V2beta2ExternalMetricStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
