# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.15.9
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.custom_objects_api import CustomObjectsApi  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestCustomObjectsApi(unittest.TestCase):
    """CustomObjectsApi unit test stubs"""

    def setUp(self):
        self.api = kubernetes_asyncio.client.api.custom_objects_api.CustomObjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_cluster_custom_object(self):
        """Test case for create_cluster_custom_object

        """
        pass

    def test_create_namespaced_custom_object(self):
        """Test case for create_namespaced_custom_object

        """
        pass

    def test_delete_cluster_custom_object(self):
        """Test case for delete_cluster_custom_object

        """
        pass

    def test_delete_namespaced_custom_object(self):
        """Test case for delete_namespaced_custom_object

        """
        pass

    def test_get_cluster_custom_object(self):
        """Test case for get_cluster_custom_object

        """
        pass

    def test_get_cluster_custom_object_scale(self):
        """Test case for get_cluster_custom_object_scale

        """
        pass

    def test_get_cluster_custom_object_status(self):
        """Test case for get_cluster_custom_object_status

        """
        pass

    def test_get_namespaced_custom_object(self):
        """Test case for get_namespaced_custom_object

        """
        pass

    def test_get_namespaced_custom_object_scale(self):
        """Test case for get_namespaced_custom_object_scale

        """
        pass

    def test_get_namespaced_custom_object_status(self):
        """Test case for get_namespaced_custom_object_status

        """
        pass

    def test_list_cluster_custom_object(self):
        """Test case for list_cluster_custom_object

        """
        pass

    def test_list_namespaced_custom_object(self):
        """Test case for list_namespaced_custom_object

        """
        pass

    def test_patch_cluster_custom_object(self):
        """Test case for patch_cluster_custom_object

        """
        pass

    def test_patch_cluster_custom_object_scale(self):
        """Test case for patch_cluster_custom_object_scale

        """
        pass

    def test_patch_cluster_custom_object_status(self):
        """Test case for patch_cluster_custom_object_status

        """
        pass

    def test_patch_namespaced_custom_object(self):
        """Test case for patch_namespaced_custom_object

        """
        pass

    def test_patch_namespaced_custom_object_scale(self):
        """Test case for patch_namespaced_custom_object_scale

        """
        pass

    def test_patch_namespaced_custom_object_status(self):
        """Test case for patch_namespaced_custom_object_status

        """
        pass

    def test_replace_cluster_custom_object(self):
        """Test case for replace_cluster_custom_object

        """
        pass

    def test_replace_cluster_custom_object_scale(self):
        """Test case for replace_cluster_custom_object_scale

        """
        pass

    def test_replace_cluster_custom_object_status(self):
        """Test case for replace_cluster_custom_object_status

        """
        pass

    def test_replace_namespaced_custom_object(self):
        """Test case for replace_namespaced_custom_object

        """
        pass

    def test_replace_namespaced_custom_object_scale(self):
        """Test case for replace_namespaced_custom_object_scale

        """
        pass

    def test_replace_namespaced_custom_object_status(self):
        """Test case for replace_namespaced_custom_object_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
