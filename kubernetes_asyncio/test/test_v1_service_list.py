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
from kubernetes_asyncio.client.models.v1_service_list import V1ServiceList  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1ServiceList(unittest.TestCase):
    """V1ServiceList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ServiceList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1_service_list.V1ServiceList()  # noqa: E501
        if include_optional :
            return V1ServiceList(
                api_version = '0', 
                items = [
                    kubernetes_asyncio.client.models.v1/service.v1.Service(
                        api_version = '0', 
                        kind = '0', 
                        metadata = kubernetes_asyncio.client.models.v1/object_meta.v1.ObjectMeta(
                            annotations = {
                                'key' : '0'
                                }, 
                            cluster_name = '0', 
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_grace_period_seconds = 56, 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finalizers = [
                                '0'
                                ], 
                            generate_name = '0', 
                            generation = 56, 
                            initializers = kubernetes_asyncio.client.models.v1/initializers.v1.Initializers(
                                pending = [
                                    kubernetes_asyncio.client.models.v1/initializer.v1.Initializer(
                                        name = '0', )
                                    ], 
                                result = kubernetes_asyncio.client.models.v1/status.v1.Status(
                                    api_version = '0', 
                                    code = 56, 
                                    details = kubernetes_asyncio.client.models.v1/status_details.v1.StatusDetails(
                                        causes = [
                                            kubernetes_asyncio.client.models.v1/status_cause.v1.StatusCause(
                                                field = '0', 
                                                message = '0', 
                                                reason = '0', )
                                            ], 
                                        group = '0', 
                                        kind = '0', 
                                        name = '0', 
                                        retry_after_seconds = 56, 
                                        uid = '0', ), 
                                    kind = '0', 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', ), ), 
                            labels = {
                                'key' : '0'
                                }, 
                            managed_fields = [
                                kubernetes_asyncio.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '0', 
                                    fields = kubernetes_asyncio.client.models.fields.fields(), 
                                    manager = '0', 
                                    operation = '0', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '0', 
                            namespace = '0', 
                            owner_references = [
                                kubernetes_asyncio.client.models.v1/owner_reference.v1.OwnerReference(
                                    api_version = '0', 
                                    block_owner_deletion = True, 
                                    controller = True, 
                                    kind = '0', 
                                    name = '0', 
                                    uid = '0', )
                                ], 
                            resource_version = '0', 
                            self_link = '0', 
                            uid = '0', ), 
                        spec = kubernetes_asyncio.client.models.v1/service_spec.v1.ServiceSpec(
                            cluster_ip = '0', 
                            external_i_ps = [
                                '0'
                                ], 
                            external_name = '0', 
                            external_traffic_policy = '0', 
                            health_check_node_port = 56, 
                            load_balancer_ip = '0', 
                            load_balancer_source_ranges = [
                                '0'
                                ], 
                            ports = [
                                kubernetes_asyncio.client.models.v1/service_port.v1.ServicePort(
                                    name = '0', 
                                    node_port = 56, 
                                    port = 56, 
                                    protocol = '0', 
                                    target_port = kubernetes_asyncio.client.models.target_port.targetPort(), )
                                ], 
                            publish_not_ready_addresses = True, 
                            selector = {
                                'key' : '0'
                                }, 
                            session_affinity = '0', 
                            session_affinity_config = kubernetes_asyncio.client.models.v1/session_affinity_config.v1.SessionAffinityConfig(
                                kubernetes_asyncio.client_ip = kubernetes_asyncio.client.models.v1/kubernetes_asyncio.client_ip_config.v1.ClientIPConfig(
                                    timeout_seconds = 56, ), ), 
                            type = '0', ), 
                        status = kubernetes_asyncio.client.models.v1/service_status.v1.ServiceStatus(
                            load_balancer = kubernetes_asyncio.client.models.v1/load_balancer_status.v1.LoadBalancerStatus(
                                ingress = [
                                    kubernetes_asyncio.client.models.v1/load_balancer_ingress.v1.LoadBalancerIngress(
                                        hostname = '0', 
                                        ip = '0', )
                                    ], ), ), )
                    ], 
                kind = '0', 
                metadata = kubernetes_asyncio.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return V1ServiceList(
                items = [
                    kubernetes_asyncio.client.models.v1/service.v1.Service(
                        api_version = '0', 
                        kind = '0', 
                        metadata = kubernetes_asyncio.client.models.v1/object_meta.v1.ObjectMeta(
                            annotations = {
                                'key' : '0'
                                }, 
                            cluster_name = '0', 
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_grace_period_seconds = 56, 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finalizers = [
                                '0'
                                ], 
                            generate_name = '0', 
                            generation = 56, 
                            initializers = kubernetes_asyncio.client.models.v1/initializers.v1.Initializers(
                                pending = [
                                    kubernetes_asyncio.client.models.v1/initializer.v1.Initializer(
                                        name = '0', )
                                    ], 
                                result = kubernetes_asyncio.client.models.v1/status.v1.Status(
                                    api_version = '0', 
                                    code = 56, 
                                    details = kubernetes_asyncio.client.models.v1/status_details.v1.StatusDetails(
                                        causes = [
                                            kubernetes_asyncio.client.models.v1/status_cause.v1.StatusCause(
                                                field = '0', 
                                                message = '0', 
                                                reason = '0', )
                                            ], 
                                        group = '0', 
                                        kind = '0', 
                                        name = '0', 
                                        retry_after_seconds = 56, 
                                        uid = '0', ), 
                                    kind = '0', 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', ), ), 
                            labels = {
                                'key' : '0'
                                }, 
                            managed_fields = [
                                kubernetes_asyncio.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '0', 
                                    fields = kubernetes_asyncio.client.models.fields.fields(), 
                                    manager = '0', 
                                    operation = '0', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '0', 
                            namespace = '0', 
                            owner_references = [
                                kubernetes_asyncio.client.models.v1/owner_reference.v1.OwnerReference(
                                    api_version = '0', 
                                    block_owner_deletion = True, 
                                    controller = True, 
                                    kind = '0', 
                                    name = '0', 
                                    uid = '0', )
                                ], 
                            resource_version = '0', 
                            self_link = '0', 
                            uid = '0', ), 
                        spec = kubernetes_asyncio.client.models.v1/service_spec.v1.ServiceSpec(
                            cluster_ip = '0', 
                            external_i_ps = [
                                '0'
                                ], 
                            external_name = '0', 
                            external_traffic_policy = '0', 
                            health_check_node_port = 56, 
                            load_balancer_ip = '0', 
                            load_balancer_source_ranges = [
                                '0'
                                ], 
                            ports = [
                                kubernetes_asyncio.client.models.v1/service_port.v1.ServicePort(
                                    name = '0', 
                                    node_port = 56, 
                                    port = 56, 
                                    protocol = '0', 
                                    target_port = kubernetes_asyncio.client.models.target_port.targetPort(), )
                                ], 
                            publish_not_ready_addresses = True, 
                            selector = {
                                'key' : '0'
                                }, 
                            session_affinity = '0', 
                            session_affinity_config = kubernetes_asyncio.client.models.v1/session_affinity_config.v1.SessionAffinityConfig(
                                kubernetes_asyncio.client_ip = kubernetes_asyncio.client.models.v1/kubernetes_asyncio.client_ip_config.v1.ClientIPConfig(
                                    timeout_seconds = 56, ), ), 
                            type = '0', ), 
                        status = kubernetes_asyncio.client.models.v1/service_status.v1.ServiceStatus(
                            load_balancer = kubernetes_asyncio.client.models.v1/load_balancer_status.v1.LoadBalancerStatus(
                                ingress = [
                                    kubernetes_asyncio.client.models.v1/load_balancer_ingress.v1.LoadBalancerIngress(
                                        hostname = '0', 
                                        ip = '0', )
                                    ], ), ), )
                    ],
        )

    def testV1ServiceList(self):
        """Test V1ServiceList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
