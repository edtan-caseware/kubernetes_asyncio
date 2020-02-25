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
from kubernetes_asyncio.client.models.admissionregistration_v1beta1_service_reference import AdmissionregistrationV1beta1ServiceReference  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestAdmissionregistrationV1beta1ServiceReference(unittest.TestCase):
    """AdmissionregistrationV1beta1ServiceReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AdmissionregistrationV1beta1ServiceReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.admissionregistration_v1beta1_service_reference.AdmissionregistrationV1beta1ServiceReference()  # noqa: E501
        if include_optional :
            return AdmissionregistrationV1beta1ServiceReference(
                name = '0', 
                namespace = '0', 
                path = '0', 
                port = 56
            )
        else :
            return AdmissionregistrationV1beta1ServiceReference(
                name = '0',
                namespace = '0',
        )

    def testAdmissionregistrationV1beta1ServiceReference(self):
        """Test AdmissionregistrationV1beta1ServiceReference"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
