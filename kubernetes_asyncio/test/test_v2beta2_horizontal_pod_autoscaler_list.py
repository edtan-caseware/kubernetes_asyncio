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
from kubernetes_asyncio.client.models.v2beta2_horizontal_pod_autoscaler_list import V2beta2HorizontalPodAutoscalerList  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV2beta2HorizontalPodAutoscalerList(unittest.TestCase):
    """V2beta2HorizontalPodAutoscalerList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V2beta2HorizontalPodAutoscalerList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v2beta2_horizontal_pod_autoscaler_list.V2beta2HorizontalPodAutoscalerList()  # noqa: E501
        if include_optional :
            return V2beta2HorizontalPodAutoscalerList(
                api_version = '0', 
                items = [
                    kubernetes_asyncio.client.models.v2beta2/horizontal_pod_autoscaler.v2beta2.HorizontalPodAutoscaler(
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
                        spec = kubernetes_asyncio.client.models.v2beta2/horizontal_pod_autoscaler_spec.v2beta2.HorizontalPodAutoscalerSpec(
                            max_replicas = 56, 
                            metrics = [
                                kubernetes_asyncio.client.models.v2beta2/metric_spec.v2beta2.MetricSpec(
                                    external = kubernetes_asyncio.client.models.v2beta2/external_metric_source.v2beta2.ExternalMetricSource(
                                        metric = kubernetes_asyncio.client.models.v2beta2/metric_identifier.v2beta2.MetricIdentifier(
                                            name = '0', 
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
                                                    }, ), ), 
                                        target = kubernetes_asyncio.client.models.v2beta2/metric_target.v2beta2.MetricTarget(
                                            average_utilization = 56, 
                                            average_value = '0', 
                                            type = '0', 
                                            value = '0', ), ), 
                                    object = kubernetes_asyncio.client.models.v2beta2/object_metric_source.v2beta2.ObjectMetricSource(
                                        described_object = kubernetes_asyncio.client.models.v2beta2/cross_version_object_reference.v2beta2.CrossVersionObjectReference(
                                            api_version = '0', 
                                            kind = '0', 
                                            name = '0', ), 
                                        metric = kubernetes_asyncio.client.models.v2beta2/metric_identifier.v2beta2.MetricIdentifier(
                                            name = '0', ), 
                                        target = kubernetes_asyncio.client.models.v2beta2/metric_target.v2beta2.MetricTarget(
                                            average_utilization = 56, 
                                            average_value = '0', 
                                            type = '0', 
                                            value = '0', ), ), 
                                    pods = kubernetes_asyncio.client.models.v2beta2/pods_metric_source.v2beta2.PodsMetricSource(
                                        metric = kubernetes_asyncio.client.models.v2beta2/metric_identifier.v2beta2.MetricIdentifier(
                                            name = '0', ), 
                                        target = kubernetes_asyncio.client.models.v2beta2/metric_target.v2beta2.MetricTarget(
                                            average_utilization = 56, 
                                            average_value = '0', 
                                            type = '0', 
                                            value = '0', ), ), 
                                    resource = kubernetes_asyncio.client.models.v2beta2/resource_metric_source.v2beta2.ResourceMetricSource(
                                        name = '0', 
                                        target = kubernetes_asyncio.client.models.v2beta2/metric_target.v2beta2.MetricTarget(
                                            average_utilization = 56, 
                                            average_value = '0', 
                                            type = '0', 
                                            value = '0', ), ), 
                                    type = '0', )
                                ], 
                            min_replicas = 56, 
                            scale_target_ref = kubernetes_asyncio.client.models.v2beta2/cross_version_object_reference.v2beta2.CrossVersionObjectReference(
                                api_version = '0', 
                                kind = '0', 
                                name = '0', ), ), 
                        status = kubernetes_asyncio.client.models.v2beta2/horizontal_pod_autoscaler_status.v2beta2.HorizontalPodAutoscalerStatus(
                            conditions = [
                                kubernetes_asyncio.client.models.v2beta2/horizontal_pod_autoscaler_condition.v2beta2.HorizontalPodAutoscalerCondition(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            current_metrics = [
                                kubernetes_asyncio.client.models.v2beta2/metric_status.v2beta2.MetricStatus(
                                    type = '0', )
                                ], 
                            current_replicas = 56, 
                            desired_replicas = 56, 
                            last_scale_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            observed_generation = 56, ), )
                    ], 
                kind = '0', 
                metadata = kubernetes_asyncio.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return V2beta2HorizontalPodAutoscalerList(
                items = [
                    kubernetes_asyncio.client.models.v2beta2/horizontal_pod_autoscaler.v2beta2.HorizontalPodAutoscaler(
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
                        spec = kubernetes_asyncio.client.models.v2beta2/horizontal_pod_autoscaler_spec.v2beta2.HorizontalPodAutoscalerSpec(
                            max_replicas = 56, 
                            metrics = [
                                kubernetes_asyncio.client.models.v2beta2/metric_spec.v2beta2.MetricSpec(
                                    external = kubernetes_asyncio.client.models.v2beta2/external_metric_source.v2beta2.ExternalMetricSource(
                                        metric = kubernetes_asyncio.client.models.v2beta2/metric_identifier.v2beta2.MetricIdentifier(
                                            name = '0', 
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
                                                    }, ), ), 
                                        target = kubernetes_asyncio.client.models.v2beta2/metric_target.v2beta2.MetricTarget(
                                            average_utilization = 56, 
                                            average_value = '0', 
                                            type = '0', 
                                            value = '0', ), ), 
                                    object = kubernetes_asyncio.client.models.v2beta2/object_metric_source.v2beta2.ObjectMetricSource(
                                        described_object = kubernetes_asyncio.client.models.v2beta2/cross_version_object_reference.v2beta2.CrossVersionObjectReference(
                                            api_version = '0', 
                                            kind = '0', 
                                            name = '0', ), 
                                        metric = kubernetes_asyncio.client.models.v2beta2/metric_identifier.v2beta2.MetricIdentifier(
                                            name = '0', ), 
                                        target = kubernetes_asyncio.client.models.v2beta2/metric_target.v2beta2.MetricTarget(
                                            average_utilization = 56, 
                                            average_value = '0', 
                                            type = '0', 
                                            value = '0', ), ), 
                                    pods = kubernetes_asyncio.client.models.v2beta2/pods_metric_source.v2beta2.PodsMetricSource(
                                        metric = kubernetes_asyncio.client.models.v2beta2/metric_identifier.v2beta2.MetricIdentifier(
                                            name = '0', ), 
                                        target = kubernetes_asyncio.client.models.v2beta2/metric_target.v2beta2.MetricTarget(
                                            average_utilization = 56, 
                                            average_value = '0', 
                                            type = '0', 
                                            value = '0', ), ), 
                                    resource = kubernetes_asyncio.client.models.v2beta2/resource_metric_source.v2beta2.ResourceMetricSource(
                                        name = '0', 
                                        target = kubernetes_asyncio.client.models.v2beta2/metric_target.v2beta2.MetricTarget(
                                            average_utilization = 56, 
                                            average_value = '0', 
                                            type = '0', 
                                            value = '0', ), ), 
                                    type = '0', )
                                ], 
                            min_replicas = 56, 
                            scale_target_ref = kubernetes_asyncio.client.models.v2beta2/cross_version_object_reference.v2beta2.CrossVersionObjectReference(
                                api_version = '0', 
                                kind = '0', 
                                name = '0', ), ), 
                        status = kubernetes_asyncio.client.models.v2beta2/horizontal_pod_autoscaler_status.v2beta2.HorizontalPodAutoscalerStatus(
                            conditions = [
                                kubernetes_asyncio.client.models.v2beta2/horizontal_pod_autoscaler_condition.v2beta2.HorizontalPodAutoscalerCondition(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            current_metrics = [
                                kubernetes_asyncio.client.models.v2beta2/metric_status.v2beta2.MetricStatus(
                                    type = '0', )
                                ], 
                            current_replicas = 56, 
                            desired_replicas = 56, 
                            last_scale_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            observed_generation = 56, ), )
                    ],
        )

    def testV2beta2HorizontalPodAutoscalerList(self):
        """Test V2beta2HorizontalPodAutoscalerList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
