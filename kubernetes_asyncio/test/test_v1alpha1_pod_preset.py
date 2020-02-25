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
from kubernetes_asyncio.client.models.v1alpha1_pod_preset import V1alpha1PodPreset  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException

class TestV1alpha1PodPreset(unittest.TestCase):
    """V1alpha1PodPreset unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1PodPreset
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes_asyncio.client.models.v1alpha1_pod_preset.V1alpha1PodPreset()  # noqa: E501
        if include_optional :
            return V1alpha1PodPreset(
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
                spec = kubernetes_asyncio.client.models.v1alpha1/pod_preset_spec.v1alpha1.PodPresetSpec(
                    env = [
                        kubernetes_asyncio.client.models.v1/env_var.v1.EnvVar(
                            name = '0', 
                            value = '0', 
                            value_from = kubernetes_asyncio.client.models.v1/env_var_source.v1.EnvVarSource(
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
                                    optional = True, ), ), )
                        ], 
                    env_from = [
                        kubernetes_asyncio.client.models.v1/env_from_source.v1.EnvFromSource(
                            config_map_ref = kubernetes_asyncio.client.models.v1/config_map_env_source.v1.ConfigMapEnvSource(
                                name = '0', 
                                optional = True, ), 
                            prefix = '0', 
                            secret_ref = kubernetes_asyncio.client.models.v1/secret_env_source.v1.SecretEnvSource(
                                name = '0', 
                                optional = True, ), )
                        ], 
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
                    volume_mounts = [
                        kubernetes_asyncio.client.models.v1/volume_mount.v1.VolumeMount(
                            mount_path = '0', 
                            mount_propagation = '0', 
                            name = '0', 
                            read_only = True, 
                            sub_path = '0', 
                            sub_path_expr = '0', )
                        ], 
                    volumes = [
                        kubernetes_asyncio.client.models.v1/volume.v1.Volume(
                            aws_elastic_block_store = kubernetes_asyncio.client.models.v1/aws_elastic_block_store_volume_source.v1.AWSElasticBlockStoreVolumeSource(
                                fs_type = '0', 
                                partition = 56, 
                                read_only = True, 
                                volume_id = '0', ), 
                            azure_disk = kubernetes_asyncio.client.models.v1/azure_disk_volume_source.v1.AzureDiskVolumeSource(
                                caching_mode = '0', 
                                disk_name = '0', 
                                disk_uri = '0', 
                                fs_type = '0', 
                                kind = '0', 
                                read_only = True, ), 
                            azure_file = kubernetes_asyncio.client.models.v1/azure_file_volume_source.v1.AzureFileVolumeSource(
                                read_only = True, 
                                secret_name = '0', 
                                share_name = '0', ), 
                            cephfs = kubernetes_asyncio.client.models.v1/ceph_fs_volume_source.v1.CephFSVolumeSource(
                                monitors = [
                                    '0'
                                    ], 
                                path = '0', 
                                read_only = True, 
                                secret_file = '0', 
                                user = '0', ), 
                            cinder = kubernetes_asyncio.client.models.v1/cinder_volume_source.v1.CinderVolumeSource(
                                fs_type = '0', 
                                read_only = True, 
                                volume_id = '0', ), 
                            config_map = kubernetes_asyncio.client.models.v1/config_map_volume_source.v1.ConfigMapVolumeSource(
                                default_mode = 56, 
                                items = [
                                    kubernetes_asyncio.client.models.v1/key_to_path.v1.KeyToPath(
                                        key = '0', 
                                        mode = 56, 
                                        path = '0', )
                                    ], 
                                name = '0', 
                                optional = True, ), 
                            csi = kubernetes_asyncio.client.models.v1/csi_volume_source.v1.CSIVolumeSource(
                                driver = '0', 
                                fs_type = '0', 
                                node_publish_secret_ref = kubernetes_asyncio.client.models.v1/local_object_reference.v1.LocalObjectReference(
                                    name = '0', ), 
                                read_only = True, 
                                volume_attributes = {
                                    'key' : '0'
                                    }, ), 
                            downward_api = kubernetes_asyncio.client.models.v1/downward_api_volume_source.v1.DownwardAPIVolumeSource(
                                default_mode = 56, ), 
                            empty_dir = kubernetes_asyncio.client.models.v1/empty_dir_volume_source.v1.EmptyDirVolumeSource(
                                medium = '0', 
                                size_limit = '0', ), 
                            fc = kubernetes_asyncio.client.models.v1/fc_volume_source.v1.FCVolumeSource(
                                fs_type = '0', 
                                lun = 56, 
                                read_only = True, 
                                target_ww_ns = [
                                    '0'
                                    ], 
                                wwids = [
                                    '0'
                                    ], ), 
                            flex_volume = kubernetes_asyncio.client.models.v1/flex_volume_source.v1.FlexVolumeSource(
                                driver = '0', 
                                fs_type = '0', 
                                options = {
                                    'key' : '0'
                                    }, 
                                read_only = True, ), 
                            flocker = kubernetes_asyncio.client.models.v1/flocker_volume_source.v1.FlockerVolumeSource(
                                dataset_name = '0', 
                                dataset_uuid = '0', ), 
                            gce_persistent_disk = kubernetes_asyncio.client.models.v1/gce_persistent_disk_volume_source.v1.GCEPersistentDiskVolumeSource(
                                fs_type = '0', 
                                partition = 56, 
                                pd_name = '0', 
                                read_only = True, ), 
                            git_repo = kubernetes_asyncio.client.models.v1/git_repo_volume_source.v1.GitRepoVolumeSource(
                                directory = '0', 
                                repository = '0', 
                                revision = '0', ), 
                            glusterfs = kubernetes_asyncio.client.models.v1/glusterfs_volume_source.v1.GlusterfsVolumeSource(
                                endpoints = '0', 
                                path = '0', 
                                read_only = True, ), 
                            host_path = kubernetes_asyncio.client.models.v1/host_path_volume_source.v1.HostPathVolumeSource(
                                path = '0', 
                                type = '0', ), 
                            iscsi = kubernetes_asyncio.client.models.v1/iscsi_volume_source.v1.ISCSIVolumeSource(
                                chap_auth_discovery = True, 
                                chap_auth_session = True, 
                                fs_type = '0', 
                                initiator_name = '0', 
                                iqn = '0', 
                                iscsi_interface = '0', 
                                lun = 56, 
                                portals = [
                                    '0'
                                    ], 
                                read_only = True, 
                                target_portal = '0', ), 
                            name = '0', 
                            nfs = kubernetes_asyncio.client.models.v1/nfs_volume_source.v1.NFSVolumeSource(
                                path = '0', 
                                read_only = True, 
                                server = '0', ), 
                            persistent_volume_claim = kubernetes_asyncio.client.models.v1/persistent_volume_claim_volume_source.v1.PersistentVolumeClaimVolumeSource(
                                claim_name = '0', 
                                read_only = True, ), 
                            photon_persistent_disk = kubernetes_asyncio.client.models.v1/photon_persistent_disk_volume_source.v1.PhotonPersistentDiskVolumeSource(
                                fs_type = '0', 
                                pd_id = '0', ), 
                            portworx_volume = kubernetes_asyncio.client.models.v1/portworx_volume_source.v1.PortworxVolumeSource(
                                fs_type = '0', 
                                read_only = True, 
                                volume_id = '0', ), 
                            projected = kubernetes_asyncio.client.models.v1/projected_volume_source.v1.ProjectedVolumeSource(
                                default_mode = 56, 
                                sources = [
                                    kubernetes_asyncio.client.models.v1/volume_projection.v1.VolumeProjection(
                                        secret = kubernetes_asyncio.client.models.v1/secret_projection.v1.SecretProjection(
                                            name = '0', 
                                            optional = True, ), 
                                        service_account_token = kubernetes_asyncio.client.models.v1/service_account_token_projection.v1.ServiceAccountTokenProjection(
                                            audience = '0', 
                                            expiration_seconds = 56, 
                                            path = '0', ), )
                                    ], ), 
                            quobyte = kubernetes_asyncio.client.models.v1/quobyte_volume_source.v1.QuobyteVolumeSource(
                                group = '0', 
                                read_only = True, 
                                registry = '0', 
                                tenant = '0', 
                                user = '0', 
                                volume = '0', ), 
                            rbd = kubernetes_asyncio.client.models.v1/rbd_volume_source.v1.RBDVolumeSource(
                                fs_type = '0', 
                                image = '0', 
                                keyring = '0', 
                                monitors = [
                                    '0'
                                    ], 
                                pool = '0', 
                                read_only = True, 
                                user = '0', ), 
                            scale_io = kubernetes_asyncio.client.models.v1/scale_io_volume_source.v1.ScaleIOVolumeSource(
                                fs_type = '0', 
                                gateway = '0', 
                                protection_domain = '0', 
                                read_only = True, 
                                secret_ref = kubernetes_asyncio.client.models.v1/local_object_reference.v1.LocalObjectReference(
                                    name = '0', ), 
                                ssl_enabled = True, 
                                storage_mode = '0', 
                                storage_pool = '0', 
                                system = '0', 
                                volume_name = '0', ), 
                            secret = kubernetes_asyncio.client.models.v1/secret_volume_source.v1.SecretVolumeSource(
                                default_mode = 56, 
                                optional = True, 
                                secret_name = '0', ), 
                            storageos = kubernetes_asyncio.client.models.v1/storage_os_volume_source.v1.StorageOSVolumeSource(
                                fs_type = '0', 
                                read_only = True, 
                                volume_name = '0', 
                                volume_namespace = '0', ), 
                            vsphere_volume = kubernetes_asyncio.client.models.v1/vsphere_virtual_disk_volume_source.v1.VsphereVirtualDiskVolumeSource(
                                fs_type = '0', 
                                storage_policy_id = '0', 
                                storage_policy_name = '0', 
                                volume_path = '0', ), )
                        ], )
            )
        else :
            return V1alpha1PodPreset(
        )

    def testV1alpha1PodPreset(self):
        """Test V1alpha1PodPreset"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
