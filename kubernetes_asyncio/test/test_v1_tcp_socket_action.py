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
from kubernetes_asyncio.client.models.v1_tcp_socket_action import V1TCPSocketAction  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1TCPSocketAction(unittest.TestCase):
    """V1TCPSocketAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1TCPSocketAction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1_tcp_socket_action.V1TCPSocketAction()  # noqa: E501
        if include_optional :
            return V1TCPSocketAction(
                host = '0', 
                port = kubernetes_asyncio.client.models.port.port()
            )
        else :
            return V1TCPSocketAction(
                port = kubernetes_asyncio.client.models.port.port(),
        )

    def testV1TCPSocketAction(self):
        """Test V1TCPSocketAction"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
