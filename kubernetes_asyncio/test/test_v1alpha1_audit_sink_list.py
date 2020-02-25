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
from kubernetes_asyncio.client.models.v1alpha1_audit_sink_list import V1alpha1AuditSinkList  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1alpha1AuditSinkList(unittest.TestCase):
    """V1alpha1AuditSinkList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1AuditSinkList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1alpha1_audit_sink_list.V1alpha1AuditSinkList()  # noqa: E501
        if include_optional :
            return V1alpha1AuditSinkList(
                api_version = '0', 
                items = [
                    kubernetes_asyncio.client.models.v1alpha1/audit_sink.v1alpha1.AuditSink(
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
                        spec = kubernetes_asyncio.client.models.v1alpha1/audit_sink_spec.v1alpha1.AuditSinkSpec(
                            policy = kubernetes_asyncio.client.models.v1alpha1/policy.v1alpha1.Policy(
                                level = '0', 
                                stages = [
                                    '0'
                                    ], ), 
                            webhook = kubernetes_asyncio.client.models.v1alpha1/webhook.v1alpha1.Webhook(
                                kubernetes_asyncio.client_config = kubernetes_asyncio.client.models.v1alpha1/webhook_client_config.v1alpha1.WebhookClientConfig(
                                    ca_bundle = 'YQ==', 
                                    service = kubernetes_asyncio.client.models.v1alpha1/service_reference.v1alpha1.ServiceReference(
                                        name = '0', 
                                        namespace = '0', 
                                        path = '0', 
                                        port = 56, ), 
                                    url = '0', ), 
                                throttle = kubernetes_asyncio.client.models.v1alpha1/webhook_throttle_config.v1alpha1.WebhookThrottleConfig(
                                    burst = 56, 
                                    qps = 56, ), ), ), )
                    ], 
                kind = '0', 
                metadata = kubernetes_asyncio.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return V1alpha1AuditSinkList(
                items = [
                    kubernetes_asyncio.client.models.v1alpha1/audit_sink.v1alpha1.AuditSink(
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
                        spec = kubernetes_asyncio.client.models.v1alpha1/audit_sink_spec.v1alpha1.AuditSinkSpec(
                            policy = kubernetes_asyncio.client.models.v1alpha1/policy.v1alpha1.Policy(
                                level = '0', 
                                stages = [
                                    '0'
                                    ], ), 
                            webhook = kubernetes_asyncio.client.models.v1alpha1/webhook.v1alpha1.Webhook(
                                kubernetes_asyncio.client_config = kubernetes_asyncio.client.models.v1alpha1/webhook_client_config.v1alpha1.WebhookClientConfig(
                                    ca_bundle = 'YQ==', 
                                    service = kubernetes_asyncio.client.models.v1alpha1/service_reference.v1alpha1.ServiceReference(
                                        name = '0', 
                                        namespace = '0', 
                                        path = '0', 
                                        port = 56, ), 
                                    url = '0', ), 
                                throttle = kubernetes_asyncio.client.models.v1alpha1/webhook_throttle_config.v1alpha1.WebhookThrottleConfig(
                                    burst = 56, 
                                    qps = 56, ), ), ), )
                    ],
        )

    def testV1alpha1AuditSinkList(self):
        """Test V1alpha1AuditSinkList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
