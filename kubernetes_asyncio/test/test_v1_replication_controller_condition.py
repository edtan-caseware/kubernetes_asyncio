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
from kubernetes_asyncio.client.models.v1_replication_controller_condition import V1ReplicationControllerCondition  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1ReplicationControllerCondition(unittest.TestCase):
    """V1ReplicationControllerCondition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ReplicationControllerCondition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1_replication_controller_condition.V1ReplicationControllerCondition()  # noqa: E501
        if include_optional :
            return V1ReplicationControllerCondition(
                last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                message = '0', 
                reason = '0', 
                status = '0', 
                type = '0'
            )
        else :
            return V1ReplicationControllerCondition(
                status = '0',
                type = '0',
        )

    def testV1ReplicationControllerCondition(self):
        """Test V1ReplicationControllerCondition"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
