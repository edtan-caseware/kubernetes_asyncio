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
from kubernetes_asyncio.client.models.extensions_v1beta1_deployment_list import ExtensionsV1beta1DeploymentList  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestExtensionsV1beta1DeploymentList(unittest.TestCase):
    """ExtensionsV1beta1DeploymentList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExtensionsV1beta1DeploymentList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.extensions_v1beta1_deployment_list.ExtensionsV1beta1DeploymentList()  # noqa: E501
        if include_optional :
            return ExtensionsV1beta1DeploymentList(
                api_version = '0', 
                items = [
                    kubernetes_asyncio.client.models.extensions/v1beta1/deployment.extensions.v1beta1.Deployment(
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
                        spec = kubernetes_asyncio.client.models.extensions/v1beta1/deployment_spec.extensions.v1beta1.DeploymentSpec(
                            min_ready_seconds = 56, 
                            paused = True, 
                            progress_deadline_seconds = 56, 
                            replicas = 56, 
                            revision_history_limit = 56, 
                            rollback_to = kubernetes_asyncio.client.models.extensions/v1beta1/rollback_config.extensions.v1beta1.RollbackConfig(
                                revision = 56, ), 
                            selector = kubernetes_asyncio.client.models.v1/label_selector.v1.LabelSelector(
                                match_expressions = [
                                    kubernetes_asyncio.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                        key = '0', 
                                        operator = '0', 
                                        values = [
                                            '0'
                                            ], )
                                    ], 
                                match_labels = {
                                    'key' : '0'
                                    }, ), 
                            strategy = kubernetes_asyncio.client.models.extensions/v1beta1/deployment_strategy.extensions.v1beta1.DeploymentStrategy(
                                rolling_update = kubernetes_asyncio.client.models.extensions/v1beta1/rolling_update_deployment.extensions.v1beta1.RollingUpdateDeployment(
                                    max_surge = kubernetes_asyncio.client.models.max_surge.maxSurge(), 
                                    max_unavailable = kubernetes_asyncio.client.models.max_unavailable.maxUnavailable(), ), 
                                type = '0', ), 
                            template = kubernetes_asyncio.client.models.v1/pod_template_spec.v1.PodTemplateSpec(), ), 
                        status = kubernetes_asyncio.client.models.extensions/v1beta1/deployment_status.extensions.v1beta1.DeploymentStatus(
                            available_replicas = 56, 
                            collision_count = 56, 
                            conditions = [
                                kubernetes_asyncio.client.models.extensions/v1beta1/deployment_condition.extensions.v1beta1.DeploymentCondition(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            observed_generation = 56, 
                            ready_replicas = 56, 
                            replicas = 56, 
                            unavailable_replicas = 56, 
                            updated_replicas = 56, ), )
                    ], 
                kind = '0', 
                metadata = kubernetes_asyncio.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return ExtensionsV1beta1DeploymentList(
                items = [
                    kubernetes_asyncio.client.models.extensions/v1beta1/deployment.extensions.v1beta1.Deployment(
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
                        spec = kubernetes_asyncio.client.models.extensions/v1beta1/deployment_spec.extensions.v1beta1.DeploymentSpec(
                            min_ready_seconds = 56, 
                            paused = True, 
                            progress_deadline_seconds = 56, 
                            replicas = 56, 
                            revision_history_limit = 56, 
                            rollback_to = kubernetes_asyncio.client.models.extensions/v1beta1/rollback_config.extensions.v1beta1.RollbackConfig(
                                revision = 56, ), 
                            selector = kubernetes_asyncio.client.models.v1/label_selector.v1.LabelSelector(
                                match_expressions = [
                                    kubernetes_asyncio.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                        key = '0', 
                                        operator = '0', 
                                        values = [
                                            '0'
                                            ], )
                                    ], 
                                match_labels = {
                                    'key' : '0'
                                    }, ), 
                            strategy = kubernetes_asyncio.client.models.extensions/v1beta1/deployment_strategy.extensions.v1beta1.DeploymentStrategy(
                                rolling_update = kubernetes_asyncio.client.models.extensions/v1beta1/rolling_update_deployment.extensions.v1beta1.RollingUpdateDeployment(
                                    max_surge = kubernetes_asyncio.client.models.max_surge.maxSurge(), 
                                    max_unavailable = kubernetes_asyncio.client.models.max_unavailable.maxUnavailable(), ), 
                                type = '0', ), 
                            template = kubernetes_asyncio.client.models.v1/pod_template_spec.v1.PodTemplateSpec(), ), 
                        status = kubernetes_asyncio.client.models.extensions/v1beta1/deployment_status.extensions.v1beta1.DeploymentStatus(
                            available_replicas = 56, 
                            collision_count = 56, 
                            conditions = [
                                kubernetes_asyncio.client.models.extensions/v1beta1/deployment_condition.extensions.v1beta1.DeploymentCondition(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            observed_generation = 56, 
                            ready_replicas = 56, 
                            replicas = 56, 
                            unavailable_replicas = 56, 
                            updated_replicas = 56, ), )
                    ],
        )

    def testExtensionsV1beta1DeploymentList(self):
        """Test ExtensionsV1beta1DeploymentList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
