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
from kubernetes_asyncio.client.models.v1beta1_daemon_set_status import V1beta1DaemonSetStatus  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1beta1DaemonSetStatus(unittest.TestCase):
    """V1beta1DaemonSetStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1DaemonSetStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1beta1_daemon_set_status.V1beta1DaemonSetStatus()  # noqa: E501
        if include_optional :
            return V1beta1DaemonSetStatus(
                collision_count = 56, 
                conditions = [
                    kubernetes_asyncio.client.models.v1beta1/daemon_set_condition.v1beta1.DaemonSetCondition(
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '0', 
                        reason = '0', 
                        status = '0', 
                        type = '0', )
                    ], 
                current_number_scheduled = 56, 
                desired_number_scheduled = 56, 
                number_available = 56, 
                number_misscheduled = 56, 
                number_ready = 56, 
                number_unavailable = 56, 
                observed_generation = 56, 
                updated_number_scheduled = 56
            )
        else :
            return V1beta1DaemonSetStatus(
                current_number_scheduled = 56,
                desired_number_scheduled = 56,
                number_misscheduled = 56,
                number_ready = 56,
        )

    def testV1beta1DaemonSetStatus(self):
        """Test V1beta1DaemonSetStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
