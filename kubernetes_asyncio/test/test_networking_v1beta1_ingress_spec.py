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
from kubernetes_asyncio.client.models.networking_v1beta1_ingress_spec import NetworkingV1beta1IngressSpec  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestNetworkingV1beta1IngressSpec(unittest.TestCase):
    """NetworkingV1beta1IngressSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NetworkingV1beta1IngressSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.networking_v1beta1_ingress_spec.NetworkingV1beta1IngressSpec()  # noqa: E501
        if include_optional :
            return NetworkingV1beta1IngressSpec(
                backend = kubernetes_asyncio.client.models.networking/v1beta1/ingress_backend.networking.v1beta1.IngressBackend(
                    service_name = '0', 
                    service_port = kubernetes_asyncio.client.models.service_port.servicePort(), ), 
                rules = [
                    kubernetes_asyncio.client.models.networking/v1beta1/ingress_rule.networking.v1beta1.IngressRule(
                        host = '0', 
                        http = kubernetes_asyncio.client.models.networking/v1beta1/http_ingress_rule_value.networking.v1beta1.HTTPIngressRuleValue(
                            paths = [
                                kubernetes_asyncio.client.models.networking/v1beta1/http_ingress_path.networking.v1beta1.HTTPIngressPath(
                                    backend = kubernetes_asyncio.client.models.networking/v1beta1/ingress_backend.networking.v1beta1.IngressBackend(
                                        service_name = '0', 
                                        service_port = kubernetes_asyncio.client.models.service_port.servicePort(), ), 
                                    path = '0', )
                                ], ), )
                    ], 
                tls = [
                    kubernetes_asyncio.client.models.networking/v1beta1/ingress_tls.networking.v1beta1.IngressTLS(
                        hosts = [
                            '0'
                            ], 
                        secret_name = '0', )
                    ]
            )
        else :
            return NetworkingV1beta1IngressSpec(
        )

    def testNetworkingV1beta1IngressSpec(self):
        """Test NetworkingV1beta1IngressSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
