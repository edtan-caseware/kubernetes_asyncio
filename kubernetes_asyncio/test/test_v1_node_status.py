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
from kubernetes_asyncio.client.models.v1_node_status import V1NodeStatus  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1NodeStatus(unittest.TestCase):
    """V1NodeStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1NodeStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1_node_status.V1NodeStatus()  # noqa: E501
        if include_optional :
            return V1NodeStatus(
                addresses = [
                    kubernetes_asyncio.client.models.v1/node_address.v1.NodeAddress(
                        address = '0', 
                        type = '0', )
                    ], 
                allocatable = {
                    'key' : '0'
                    }, 
                capacity = {
                    'key' : '0'
                    }, 
                conditions = [
                    kubernetes_asyncio.client.models.v1/node_condition.v1.NodeCondition(
                        last_heartbeat_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '0', 
                        reason = '0', 
                        status = '0', 
                        type = '0', )
                    ], 
                config = kubernetes_asyncio.client.models.v1/node_config_status.v1.NodeConfigStatus(
                    active = kubernetes_asyncio.client.models.v1/node_config_source.v1.NodeConfigSource(
                        config_map = kubernetes_asyncio.client.models.v1/config_map_node_config_source.v1.ConfigMapNodeConfigSource(
                            kubelet_config_key = '0', 
                            name = '0', 
                            namespace = '0', 
                            resource_version = '0', 
                            uid = '0', ), ), 
                    assigned = kubernetes_asyncio.client.models.v1/node_config_source.v1.NodeConfigSource(), 
                    error = '0', 
                    last_known_good = kubernetes_asyncio.client.models.v1/node_config_source.v1.NodeConfigSource(), ), 
                daemon_endpoints = kubernetes_asyncio.client.models.v1/node_daemon_endpoints.v1.NodeDaemonEndpoints(
                    kubelet_endpoint = kubernetes_asyncio.client.models.v1/daemon_endpoint.v1.DaemonEndpoint(
                        port = 56, ), ), 
                images = [
                    kubernetes_asyncio.client.models.v1/container_image.v1.ContainerImage(
                        names = [
                            '0'
                            ], 
                        size_bytes = 56, )
                    ], 
                node_info = kubernetes_asyncio.client.models.v1/node_system_info.v1.NodeSystemInfo(
                    architecture = '0', 
                    boot_id = '0', 
                    container_runtime_version = '0', 
                    kernel_version = '0', 
                    kube_proxy_version = '0', 
                    kubelet_version = '0', 
                    machine_id = '0', 
                    operating_system = '0', 
                    os_image = '0', 
                    system_uuid = '0', ), 
                phase = '0', 
                volumes_attached = [
                    kubernetes_asyncio.client.models.v1/attached_volume.v1.AttachedVolume(
                        device_path = '0', 
                        name = '0', )
                    ], 
                volumes_in_use = [
                    '0'
                    ]
            )
        else :
            return V1NodeStatus(
        )

    def testV1NodeStatus(self):
        """Test V1NodeStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
