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
from kubernetes_asyncio.client.models.v1_container_state_terminated import V1ContainerStateTerminated  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1ContainerStateTerminated(unittest.TestCase):
    """V1ContainerStateTerminated unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ContainerStateTerminated
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1_container_state_terminated.V1ContainerStateTerminated()  # noqa: E501
        if include_optional :
            return V1ContainerStateTerminated(
                container_id = '0', 
                exit_code = 56, 
                finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                message = '0', 
                reason = '0', 
                signal = 56, 
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return V1ContainerStateTerminated(
                exit_code = 56,
        )

    def testV1ContainerStateTerminated(self):
        """Test V1ContainerStateTerminated"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
