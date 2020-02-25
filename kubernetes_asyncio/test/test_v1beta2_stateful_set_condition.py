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
from kubernetes_asyncio.client.models.v1beta2_stateful_set_condition import V1beta2StatefulSetCondition  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1beta2StatefulSetCondition(unittest.TestCase):
    """V1beta2StatefulSetCondition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta2StatefulSetCondition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1beta2_stateful_set_condition.V1beta2StatefulSetCondition()  # noqa: E501
        if include_optional :
            return V1beta2StatefulSetCondition(
                last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                message = '0', 
                reason = '0', 
                status = '0', 
                type = '0'
            )
        else :
            return V1beta2StatefulSetCondition(
                status = '0',
                type = '0',
        )

    def testV1beta2StatefulSetCondition(self):
        """Test V1beta2StatefulSetCondition"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
