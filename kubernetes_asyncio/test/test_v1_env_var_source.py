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
from kubernetes_asyncio.client.models.v1_env_var_source import V1EnvVarSource  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1EnvVarSource(unittest.TestCase):
    """V1EnvVarSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1EnvVarSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1_env_var_source.V1EnvVarSource()  # noqa: E501
        if include_optional :
            return V1EnvVarSource(
                config_map_key_ref = kubernetes_asyncio.client.models.v1/config_map_key_selector.v1.ConfigMapKeySelector(
                    key = '0', 
                    name = '0', 
                    optional = True, ), 
                field_ref = kubernetes_asyncio.client.models.v1/object_field_selector.v1.ObjectFieldSelector(
                    api_version = '0', 
                    field_path = '0', ), 
                resource_field_ref = kubernetes_asyncio.client.models.v1/resource_field_selector.v1.ResourceFieldSelector(
                    container_name = '0', 
                    divisor = '0', 
                    resource = '0', ), 
                secret_key_ref = kubernetes_asyncio.client.models.v1/secret_key_selector.v1.SecretKeySelector(
                    key = '0', 
                    name = '0', 
                    optional = True, )
            )
        else :
            return V1EnvVarSource(
        )

    def testV1EnvVarSource(self):
        """Test V1EnvVarSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
