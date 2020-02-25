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
from kubernetes_asyncio.client.models.v1_event_series import V1EventSeries  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1EventSeries(unittest.TestCase):
    """V1EventSeries unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1EventSeries
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1_event_series.V1EventSeries()  # noqa: E501
        if include_optional :
            return V1EventSeries(
                count = 56, 
                last_observed_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                state = '0'
            )
        else :
            return V1EventSeries(
        )

    def testV1EventSeries(self):
        """Test V1EventSeries"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
